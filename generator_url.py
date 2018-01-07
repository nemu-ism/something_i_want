import sys
import urllib.parse
import urllib.request

def generator_json():
    url = 'https://shopping.yahooapis.jp/ShoppingWebService/V1/json/itemSearch?'
    appid = 'dj00aiZpPU1YWU1IRXYwaDhqeCZzPWNvbnN1bWVyc2VjcmV0Jng9MDY-'
    requests_base = {'appid': appid,
                     'query':'python',
                     'price_from':0,
                     'price_to':99999999,
                     'hits':'10',
                     'offset':0,
                     'availability':1,
                     'sort':'-score',
                     'condition':'all'}
    requests_base.update(generator_dic())
    params = urllib.parse.urlencode(requests_base)

    response = urllib.request.urlopen(url + params)
    return response.read()

def generator_dic():
    requests = ['query:初音ミク', 'offset:10']
    requests_processed = []
    for w in requests:
        requests_processed.append(w.split(":"))
    requests_dic = dict(requests_processed)
    dic = {'sort':'-review'}
    requests_dic.update(dic)
    return requests_dic

if __name__ == '__main__':
    print(generator_dic())