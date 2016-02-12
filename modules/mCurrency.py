from jConfig import cCurrencyDataSource
from pandas import read_json, DataFrame


## Update currency database
##  API URL - http://api.fixer.io/latest?base=INR

currency_table = read_json(cCurrencyDataSource)
currency_table['price'] = 1/currency_table['rates']
currency_table['currency'] = currency_table.index.values
currency_table = currency_table.drop(['date','base'],1)

def jConvertCurrency(fromCurrency, toCurrency, amount):
    fromCurrency = fromCurrency.upper()
    toCurrency = toCurrency.upper()
    amount = float(amount)
    if fromCurrency == toCurrency:
        return (float(amount))
    elif fromCurrency == 'INR':
        return (amount * float(currency_table[currency_table.currency == toCurrency].rates))
    elif toCurrency == 'INR':
        return (amount * float(currency_table[currency_table.currency == fromCurrency].price))
    else:
        return (amount * float(currency_table[currency_table.currency == toCurrency].rates) / float(currency_table[currency_table.currency == fromCurrency].rates))

def jCurrencyChart(currencies):
    currencies = [x.upper() for x in currencies]
    return currency_table[currency_table['currency'].isin(currencies)]

def jCurrencyConversionChart(fromCurrency, toCurrencies, amount):
    fromCurrency = fromCurrency.upper()
    amount = float(amount)
    toCurrencies = [x.upper() for x in toCurrencies]

    result = {}
    for toCurrency in toCurrencies:
        result[toCurrency] = jConvertCurrency(fromCurrency,toCurrency,amount)
    result = DataFrame(result.items(), columns = ['to_currency','amount'])
    result['from_currency'] = fromCurrency
    return (result[['from_currency','to_currency','amount']])