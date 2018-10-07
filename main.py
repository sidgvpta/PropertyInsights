import numpy as np
import pandas as pd
import GetPPRData
import Analysis


filename = GetPPRData.getHistoricalPrices()
ppr_data = pd.read_csv(filename, encoding = 'ISO-8859-1')


def preprocessData(ppr_data):
    ppr_data['Postal Code'].fillna(0 , inplace=True)
    ppr_data.rename(columns={'Price (\x80)': 'Price (EUR)'}, inplace=True)
    ppr_data['Price (EUR)'].replace(regex=True, inplace=True, to_replace= r'[^.0-9]+', value=r'')
    ppr_data['Price (EUR)'] = ppr_data['Price (EUR)'].astype(float)
    VAT_RATE = 0.135
    ppr_data['Price Incl. VAT (EUR)'] = np.where(ppr_data['VAT Exclusive'] == 'Yes', ppr_data['Price (EUR)'] * (1 + VAT_RATE), ppr_data['Price (EUR)'])


preprocessData(ppr_data)

ppr_data_avgPricePerCounty = Analysis.averagePriceByCounty(ppr_data)
ppr_data_dublin = Analysis.pricesByCounty(ppr_data, 'Dublin')


while True:
    continue