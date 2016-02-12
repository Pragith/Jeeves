from jConfig import cNLP_Dict
import jHelpers
import mCurrency
import mShows
import mWebsiteCheck
import mRefreshFeeds



def jNLPGetAllModules(input_word):
    for module, nlp_text in cNLP_Dict.iteritems():
        if input_word in nlp_text:
            return(module)

def jNLPGetModule(input_text):
    result = [jNLPGetAllModules(input_word) for input_word in input_text.split(" ")]
    result = list(set([Module for Module in result if Module is not None]))
    if not result:
        return 'Error-NLP-01'
    else:
        return result[0]



t1 = "check" # For URL testing
t2 = "convert 100 usd to inr"
t3 = "shows" # For getting latest shows --> mShows.jGetShows('url', 'df')
t4 = "download show 2" # Download show with ID 2 in the output table
t5 = "download all shows"
t6 = "weather" # Fetch weather of cCity
t7 = "weather chennai" # Fetch weather of Chennai
t8 = "100 inr to usd weather"

print jNLPGetModule(t1)
print jNLPGetModule(t2)
print jNLPGetModule(t3)
print jNLPGetModule(t4)
print jNLPGetModule(t5)
print jNLPGetModule(t6)
print jNLPGetModule(t7)
print jNLPGetModule(t8)












