def averagePriceByCounty(ppr_data):
    averagePricePerCounty = ppr_data.groupby(['County']).mean()

    return averagePricePerCounty

def pricesByCounty(ppr_data, county):
    countyPrices = ppr_data[ppr_data['County'] == county]

    return countyPrices