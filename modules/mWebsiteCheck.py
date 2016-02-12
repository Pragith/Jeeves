from bs4 import BeautifulSoup as bs
import requests

def jIsWebsiteUp(url):
    data = bs(requests.get("http://isup.me/" +url).text, 'html.parser').div.text
    if data.find("It's just you") != -1:
        return "Up"
    elif  data.find("It's not") != -1:
        return "Down"
    else:
        return data