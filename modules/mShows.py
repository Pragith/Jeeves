import requests, jHelpers
from jConfig import cShowsDataSource, cShowsUpdateDataDestination
from lxml import etree, html
from bs4 import BeautifulSoup as bs



def jGetShows(method,output):
    """
     Input:
      showsDataSource in xml -- URL or file
      method -- 'file' or 'url'
      output -- 'json' or 'df'
     Output: GUID : { Title, Timestamp, Magnet }
     :rtype: object
    """
    if method == 'url':
        shows_data = etree.fromstring(str(requests.get(cShowsDataSource).text))

    elif method == 'file':
        shows_data = etree.parse(cShowsDataSource)

    shows_dict = dict()
    for show in shows_data.getiterator('item'):
        shows_dict[show.findtext('guid')] = dict(title=show.findtext('title'),
                                                 timestamp=show.findtext('pubDate'),
                                                 magnet=show.findtext('link'))
    if output == 'json':
        return shows_dict

    elif output == 'df':
        return jHelpers.jDictToDF(shows_dict)

def jUpdateShowsDatabase(cShowsURL):
    res = str(bs(requests.get(cShowsURL).text,'html.parser'))
    if (res):
        jHelpers.jWriteToFile(res, cShowsUpdateDataDestination)
        return 'Successfully updated shows database'
    else:
        return 'Error-Shows-01'

