from urllib.request import urlopen, Request
from pprint import pprint
def url2txt(url):
    """
    Takes url as an argument and returns the web-page in str format
    
    """
    request = Request(url)
    response = urlopen(request)
    response = response.read()

    return response

msg = url2txt("https://t.me/seniorpy/1899")
pprint(msg)