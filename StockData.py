import pandas_datareader.data as web
import datetime


def GetInstrumentPrices(symbol):
    source = 'yahoo'
    start_date = datetime.datetime(2010, 1, 1)
    end_date = datetime.datetime.today()
    historical_data = web.DataReader(symbol, source, start_date, end_date)
    return historical_data
