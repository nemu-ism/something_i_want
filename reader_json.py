import json
import generator_url

class JsonReader:

    def __init__(self):
        pass

    generator = generator_url.UrlGenerator()

    def print_list(self, response, args):
        data = json.loads(response)

        hits_total = int(data["ResultSet"]["totalResultsAvailable"])
        hits_offset = int(data["ResultSet"]["firstResultPosition"])
        item_list = data["ResultSet"]["0"]["Result"]
        results = {}
        for k, v in item_list.items():
            try:
                number = int(v["_attributes"]["index"])
                name = v["Name"]
                url = v["Url"]
                condition = v["Condition"]
                price = int(v["Price"]["_value"])
                rate_average = v["Review"]["Rate"]
                rate_count = int(v["Review"]["Count"])
                results[number] = [name, condition, price, rate_average, rate_count, url]
            except:
                if k == "Request":
                    query = v["Query"]

        # many ifs are dirty :(
        dic = self.generator.generate_dic(args[1:])
        print('-' * 40)
        if 'sort' in dic:
            print(dic['sort'], end='')
        print('検索ワード：', query)
        if 'condition' in dic:
            print('状態:{:} only'.format(dic['condition']))
        if 'price_from' or 'price_to' in dic:
            print('価格：', end='')
            if 'price_from' in dic:
                print('{:,}円から'.format(int(dic['price_from'])), end='')
            if 'price_to' in dic:
                print('{:,}円まで'.format(int(dic['price_to'])), end='')
            print('')
        print('{0:,}件中　{1:,}～{2:,}件'.format(hits_total, hits_offset, hits_offset+9))
        print('-' * 40)

        results_keys = list(results.keys())
        for i in results_keys:
            print(i, results[i][0])
            print(' ' *6, results[i][1], '{:,}円(税込)'.format(results[i][2]),
                  '平均評価{0:}点({1:,}人中)'.format(results[i][3], results[i][4]))
            print(' ' *6, '商品ページ：', results[i][5])