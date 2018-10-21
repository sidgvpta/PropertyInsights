import requests
import zipfile
import io
import numpy as np
import pandas as pd


def getHistoricalPrices():
    url = 'https://www.propertypriceregister.ie/website/npsra/ppr/npsra-ppr.nsf/Downloads/PPR-ALL.zip/$FILE/PPR-ALL.zip'
    filename_zip = url[url.rfind("/") + 1:]
    filename = filename_zip.replace('.zip', '.csv')

    r = requests.get(url, verify=False)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()

    return filename

def preprocessData(ppr_data):
    ppr_data['Postal Code'].fillna(0 , inplace=True)
    ppr_data.rename(columns={'Price (\x80)': 'Price (EUR)'}, inplace=True)
    ppr_data['Price (EUR)'].replace(regex=True, inplace=True, to_replace= r'[^.0-9]+', value=r'')
    ppr_data['Price (EUR)'] = ppr_data['Price (EUR)'].astype(float)
    VAT_RATE = 0.135
    ppr_data['Price Incl. VAT (EUR)'] = np.where(ppr_data['VAT Exclusive'] == 'Yes', ppr_data['Price (EUR)'] * (1 + VAT_RATE), ppr_data['Price (EUR)'])
    return ppr_data