import numpy as np
import pandas as pd
import PPRData
import StockData
import Analysis


filename = PPRData.getHistoricalPrices()
ppr_data = pd.read_csv(filename, encoding = 'ISO-8859-1')
ppr_data = PPRData.preprocessData(ppr_data)

ppr_data_avgPricePerCounty = Analysis.averagePriceByCounty(ppr_data)
ppr_data_dublin = Analysis.pricesByCounty(ppr_data, 'Dublin')

hbrn_data = StockData.GetInstrumentPrices('HBRN.IR')


while True:
    continue