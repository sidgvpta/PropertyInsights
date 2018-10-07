import requests
import zipfile
import io


def getHistoricalPrices():
    url = 'https://www.propertypriceregister.ie/website/npsra/ppr/npsra-ppr.nsf/Downloads/PPR-ALL.zip/$FILE/PPR-ALL.zip'
    filename_zip = url[url.rfind("/") + 1:]
    filename = filename_zip.replace('.zip', '.csv')

    r = requests.get(url, verify=False)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()

    return filename