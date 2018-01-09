import generator_url
import reader_json

class Main:
    def __init__(self):
        pass

    generator = generator_url.UrlGenerator()
    reader = reader_json.JsonReader()

    def main(self, args):
        requests = args[1:]
        json_generated = self.generator.generate_json(requests)
        self.reader.print_list(json_generated, args)