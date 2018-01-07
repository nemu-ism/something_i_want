import json
import sys
import urllib.parse
import urllib.request

args = sys.argv

def generator_json(reqests):
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
    dic = generator_dic(reqests)
    requests_base.update(dic)
    params = urllib.parse.urlencode(requests_base)

    response = urllib.request.urlopen(url + params)
    return response.read()

def generator_dic(requests):
    requests_processed = []
    for w in requests:
        requests_processed.append(w.split(":"))
    requests_dic = dict(requests_processed)
    return requests_dic

if __name__ == '__main__':
    list = args[1:]
    dota = generator_json(list)
    data = json.loads(dota)
    print(json.dumps(data, ensure_ascii=False, sort_keys=False, indent=4)); sys.exit()
