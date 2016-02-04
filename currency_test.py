from modules import mCurrency

print mCurrency.convertCurrency('CAD','INR',15143)
print mCurrency.currencyChart(['USD','AUD','CAD'])
print mCurrency.currencyConversionChart('INR',['USd','aUD','CaD','GBP','EUR'],'1000')
print mCurrency.currencyChart(['cad'])
print mCurrency.currencyConversionChart('cad',['USd','aUD','inr','CaD','GBP','EUR'],'15143')
