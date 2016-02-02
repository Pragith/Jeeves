from lxml import etree, html
import requests, helpers


def jGetShows(dataSource,method,output):
    """
     Input:
      dataSource in xml -- URL or file
      method -- 'file' or 'url'
      output -- 'json' or 'df'
     Output: GUID : { Title, Timestamp, Magnet }
     :rtype: object
    """
    if method == 'url':
        shows_data = etree.fromstring(str(requests.get(dataSource).text))

    elif method == 'file':
        shows_data = etree.parse(dataSource)

    shows_dict = dict()
    for show in shows_data.getiterator('item'):
        shows_dict[show.findtext('guid')] = dict(title=show.findtext('title'),
                                                 timestamp=show.findtext('pubDate'),
                                                 magnet=show.findtext('link'))
    if output == 'json':
        return shows_dict

    elif output == 'df':
        return helpers.jDictToDF(shows_dict)