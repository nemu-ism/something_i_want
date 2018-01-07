import urllib.parse
import urllib.request

def json_generator():
    url = 'https://shopping.yahooapis.jp/ShoppingWebService/V1/json/itemSearch?'
    appid = 'dj00aiZpPU1YWU1IRXYwaDhqeCZzPWNvbnN1bWVyc2VjcmV0Jng9MDY-'
    params = urllib.parse.urlencode(
        {'appid': appid,
         'query':'北海道',
         'price_from':0,
         'price_to':99999999,
         'hits':'10',
         'offset':0,
         'availability':1,
         'sort':'-score',
         'condition':'all'})

    response = urllib.request.urlopen(url + params)
    return response.read()