from pandas import DataFrame


##  Write a function to extract error messages from Error_Dict

def jDictToDF(data):
    """
    :rtype: Data Frame
    """
    return DataFrame.from_dict(data, orient = 'index')