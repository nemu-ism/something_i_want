import sys
import urllib.parse
import urllib.request
import json

def yapi_topics():
    url = 'http://shopping.yahooapis.jp/ShoppingWebService/V1/json/categoryRanking?'
    appid = 'dj00aiZpPU1YWU1IRXYwaDhqeCZzPWNvbnN1bWVyc2VjcmV0Jng9MDY-'
    params = urllib.parse.urlencode(
        {'appid': appid,
         'offset':20,
         'period':'weekly',
         'generation':30,
         'gender':'female',})

    response = urllib.request.urlopen(url + params)
    return response.read()

def do_json(s):
    data = json.loads(s)
    #print(json.dumps(data, ensure_ascii=False, sort_keys=False, indent=4)); sys.exit()

    #jsonの階層の"Result"以下を辞書にする。keyは番号：その次の配列がvalueになっている
    item_list = data["ResultSet"]["0"]["Result"]

    #空のディクショナリを作る
    ranking = {}
    for  k, v in item_list.items():
        try:
            rank = int(v["_attributes"]["rank"])
            vector = v["_attributes"]["vector"]
            name  = v["Name"]
            ranking[rank] = [vector, name]
        except:
            if k == "RankingInfo":
                StartDate = v["StartDate"]
                EndDate = v["EndDate"]

    print('-' * 40)
    print("集計開始日:", StartDate)
    print("集計終了日:", EndDate)
    print('-' * 40)
    ranking_keys = list(ranking.keys())
    ranking_keys.sort()
    for i in ranking_keys:
        print(i, ranking[i][0], ranking [i][1])

if __name__ == '__main__':
    json_str = yapi_topics()
    do_json(json_str)