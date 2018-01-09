import json
import sys
import generator_url
import reader_json


# sys.argv = terminal入力
args = sys.argv


def load_json(d):
    data = json.loads(d)
    return data


# main
if __name__ == '__main__':
    try:
        requests = args[1:]
        json_generated = generator_url.generator_json(requests)
        reader_json.print_list(load_json(json_generated), args)
        print("dekita")
    except:
        print("リクエスト内容に誤りがありました。リクエスト内容を確認してください。")
        sys.exit()