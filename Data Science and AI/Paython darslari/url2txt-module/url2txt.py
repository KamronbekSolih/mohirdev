from urllib.request import urlopen, Request

def url2txt(url):
    """
    Takes url as an argument and returns the web-page in str format
    
    """
    request = Request(url)
    response = urlopen(request)
    response = response.read()

    return response