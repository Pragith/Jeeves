cCurrencyDataSource = 'data/currency.json'
cCurrencyURL = 'http://api.fixer.io/latest?base=INR'

cShowsDataSource = '../data/shows.xml'
cShowsURL = "http://showrss.info/rss.php?user_id=207042&hd=0&proper=null&raw=false"

cTemperature = 'C' #"C" or "F"
cCity = "Bangalore"

cNLP_Dict = {'Shows':['shows','download']
            ,'Weather':['weather','umbrella']
            ,'Currency':['usd','inr','cad','aud']
            ,'Website':['up','down','unavailable','url','website']}

cError_Dict = {'Error-NLP-01':'Module not found with the input text'
               ,'Error-Currency-01':'Unable to fetch latest currency rates'}