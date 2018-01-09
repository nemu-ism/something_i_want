import urllib.parse
import urllib.request

class UrlGenerator:
    def __init__(self):
        pass

    def generator_json(self, reqests):
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
        try:
            dic = self.generator_dic(reqests)
        except:
            print("リクエスト内容に誤りがありました。リクエスト内容を確認してください。")

        requests_base.update(dic)
        params = urllib.parse.urlencode(requests_base)

        try:
            response = urllib.request.urlopen(url + params)
        except:
            print("リクエスト送信に失敗しました。接続を確認してください。")

        return response.read()

    # request_list -> request_dict
    def generator_dic(self, requests):
        requests_processed = []
        for w in requests:
            requests_processed.append(w.split(':'))
        requests_dic = dict(requests_processed)
        if 'offset' in requests_dic:
            requests_dic['offset'] = int(requests_dic['offset'])-1
        return requests_dic