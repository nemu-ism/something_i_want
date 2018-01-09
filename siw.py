import sys
import generator_url
import reader_json

# sys.argv = terminal入力
args = sys.argv
generator = generator_url.UrlGenerator()
reader = reader_json.JsonReader()

# main
if __name__ == '__main__':
    try:
        requests = args[1:]
        json_generated = generator.generate_json(requests)
        reader.print_list(json_generated, args)
    except:
        print("実行を終了します。")
        sys.exit()