from pandas import DataFrame

def jDictToDF(data):
    """
    :rtype: Data Frame
    """
    return DataFrame.from_dict(data, orient = 'index')