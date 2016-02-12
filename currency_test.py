from modules import mCurrency,jConfig

print mCurrency.jConvertCurrency('CAD','INR',15143)
print mCurrency.jCurrencyChart(['USD','AUD','CAD'])
print mCurrency.jCurrencyConversionChart('INR',['USd','aUD','CaD','GBP','EUR'],'1000')
print mCurrency.jCurrencyConversionChart('cad',['USd','aUD','inr','CaD','GBP','EUR'],'15143')
print mCurrency.jCurrencyConversionChart('GBP',['USd','aUD','inr','CaD','GBP','EUR'],333.33)


##  Update Currency Database
#print jUpdateCurrencyDatabase(jConfig.cCurrencyURL)
