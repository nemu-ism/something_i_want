import sys
import main
import generator_url
import reader_json

# sys.argv = terminal入力
args = sys.argv
main = main.Main()
generator = generator_url.UrlGenerator()
reader = reader_json.JsonReader()

# main
if __name__ == '__main__':
    try:
        main.main(args)
    except:
        print("実行を終了します。")
        sys.exit()