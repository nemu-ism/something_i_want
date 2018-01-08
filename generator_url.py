import urllib.parse
import urllib.request

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

# request_list -> request_dict
def generator_dic(requests):
    requests_processed = []
    for w in requests:
        requests_processed.append(w.split(':'))
    requests_dic = dict(requests_processed)
    if 'offset' in requests_dic:
        requests_dic['offset'] = int(requests_dic['offset'])-1
    return requests_dic

# test
if __name__ == '__main__':
    list = ['query:hatsune', 'offset:11']
    #miku = generator_json(list)
    #data = json.loads(miku)
    #print(json.dumps(data, ensure_ascii=False, sort_keys=False, indent=4))
    print(generator_dic(list))