import argparse
import json

from tabulate import tabulate


class LogParser:
    def __init__(self, file_path):
        self.data = []
        self.handlers = []
        self.parse_info = []
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path) as log_file:
                for line in log_file:
                    try:
                        self.data.append(json.loads(line))

                    except json.decoder.JSONDecodeError as e:
                        print(f"ошибка декодирования JSON - {e}")

        except FileNotFoundError:
            print(f"Файл не найден: {self.file_path}")

        return self.data

    def parse_handler(self):
        for i in self.read_file():
            if i["url"] not in self.handlers:
                self.handlers.append(i["url"])

        return self.handlers

    def parse_file(self):
        for handler in self.handlers:
            self.parse_info.append({handler: [{"total": 0}, {"avg_response_time": 0}]})
            for endpoint in self.data:
                url_key = list(self.parse_info[len(self.parse_info)-1].keys())[0]
                print(url_key)
                if endpoint["url"] == url_key:
                    self.parse_info[len(self.parse_info) - 1][url_key][0]["total"]+=1
                    self.parse_info[len(self.parse_info) - 1][url_key][1]["avg_response_time"] += endpoint["response_time"]

        for endpoint in self.parse_info:
            print(list(endpoint.values())[0][1].get["avg_response_time"])
            avg_time = list(endpoint.values())[0][1].get["avg_response_time"]
            total = list(endpoint.values())[0][0].get["total"]
            avg_time = round(avg_time / total, 2)
            print(avg_time)





def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str)

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    parser = LogParser(args.file)
    parser.parse_handler()
    parser.parse_file()
    print(parser.parse_info)
