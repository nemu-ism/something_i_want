#coding:utf-8

import sys
import urllib.parse
import urllib.request
import json

args = sys.argv

def yapi_topics():
    url = 'https://shopping.yahooapis.jp/ShoppingWebService/V1/json/itemSearch?'
    appid = 'dj00aiZpPU1YWU1IRXYwaDhqeCZzPWNvbnN1bWVyc2VjcmV0Jng9MDY-'
    params = urllib.parse.urlencode(
        {'appid': appid,
         'query':'パソコン',
         'price_to':50000,
         'hits':10,
         'offset':0,
         'availability':1})

    response = urllib.request.urlopen(url + params)
    return response.read()

def do_json(s):
    data = json.loads(s)
    #print(json.dumps(data, ensure_ascii=False, sort_keys=False, indent=4)); sys.exit()

    #jsonの階層の"Result"以下を辞書にする。keyは番号：その次の配列がvalueになっている
    hits_total = int(data["ResultSet"]["totalResultsAvailable"])
    hits_offset = int(data["ResultSet"]["firstResultPosition"])
    item_list = data["ResultSet"]["0"]["Result"]

    #空のディクショナリを作る
    results = {}
    for k, v in item_list.items():
        try:
            number = int(v["_attributes"]["index"])
            name = v["Headline"]
            url = v["Url"]
            condition = v["Condition"]
            price = v["Price"]["_value"]
            rate_average = v["Review"]["Rate"]
            rate_count = v["Review"]["Count"]
            results[number] = [name, condition, price, rate_average, rate_count, url]
        except:
            if k == "Request":
                query = v["Query"]

    print('-' * 40)
    print('検索ワード：'+ query)
    print('{0:,}件中　{1:,}～{2:,}件'.format(hits_total, hits_offset, hits_offset+9))
    print('-' * 40)
    results_keys = list(results.keys())
    results_keys.sort()
    for i in results_keys:
        print(i, results[i][0])
        print(' ' *6, results[i][1], '{:,}円(税込)'.format(int(results[i][2])), '平均評価{0:}点({1:,}人中)'.format(results[i][3], int(results[i][4])))
        print(' ' *6, '商品ページ：'+ results[i][5])

if __name__ == '__main__':
    json_str = yapi_topics()
    do_json(json_str)