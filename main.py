import argparse
import json

from tabulate import tabulate


class LogParser:
    def __init__(self, file_path):
        self.data = []
        self.handlers = []
        self.user_agent = []
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

    def parsing_items(self, sstr, llist):
        for i in self.data:
            if i[sstr] not in llist:
                llist.append(i[sstr])

        return llist

    def parse_file(self):
        for handler in self.handlers:
            self.parse_info.append({handler:
                [
                    {"total": 0},
                    {"avg_response_time": 0},
                    {"user_agent": [{agent: 0} for agent in self.user_agent]},
                ]
            }
            )
            for endpoint in self.data:
                url_key = list(self.parse_info[len(self.parse_info) - 1].keys())[0]
                user_agent_keys_and_vals = self.parse_info[len(self.parse_info) - 1][url_key][2]["user_agent"]
                if endpoint["url"] == url_key:
                    self.parse_info[len(self.parse_info) - 1][url_key][0]["total"] += 1
                    self.parse_info[len(self.parse_info) - 1][url_key][1]["avg_response_time"] += endpoint["response_time"]
                    for i in user_agent_keys_and_vals:
                        if endpoint["http_user_agent"] in i:
                            i[endpoint["http_user_agent"]] += 1


        for endpoint in self.parse_info:
            list(endpoint.values())[0][1]["avg_response_time"] /= list(endpoint.values())[0][0].get("total")
            list(endpoint.values())[0][1]["avg_response_time"] = round(
                list(endpoint.values())[0][1]["avg_response_time"], 3)





def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str)

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    parser = LogParser(args.file)
    parser.read_file()
    parse_handler = parser.parsing_items("url", parser.handlers)
    parse_user_agent_handler = parser.parsing_items("http_user_agent", parser.user_agent)
    print(parser.handlers)
    print(parser.user_agent)
    parser.parse_file()
    print(parser.parse_info)
