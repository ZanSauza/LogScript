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
        total_count = 0
        for i in self.handlers:
            self.parse_info.append({i: {'total': 0}})
            # print(self.parse_info)
            for j in self.data:
                for el in range(len(self.parse_info)):
                    # print(j["url"])
                    # print(self.parse_info[el])]
                    print(list(self.parse_info[el].keys())[0])
                    if j["url"] == list(self.parse_info[el].keys())[0]:
                        print(self.parse_info[el]['total'])
                        self.parse_info[el]['total'] += 1





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
