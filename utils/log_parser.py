import json


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

    def parsing_info(self, endpoint):
        url_key = list(self.parse_info[len(self.parse_info) - 1].keys())[0]
        user_agent_keys_and_vals = self.parse_info[len(self.parse_info) - 1][url_key][2]["user_agent"]
        if endpoint["url"] == url_key:
            self.parse_info[len(self.parse_info) - 1][url_key][0]["total"] += 1
            self.parse_info[len(self.parse_info) - 1][url_key][1]["avg_response_time"] += endpoint[
                "response_time"]
            for user_agent in user_agent_keys_and_vals:
                if endpoint["http_user_agent"] in user_agent:
                    user_agent[endpoint["http_user_agent"]] += 1

    def parse_file(self, timestamp=None):
        for handler in self.handlers:
            self.parse_info.append({handler:
                [
                    {"total": 0},
                    {"avg_response_time": 0},
                    {"user_agent": [{agent: 0} for agent in self.user_agent]},
                ]
            })
            if timestamp:
                for endpoint in self.data:
                    if endpoint["@timestamp"].startswith(timestamp):
                        self.parsing_info(endpoint)
            elif not timestamp:
                for endpoint in self.data:
                    self.parsing_info(endpoint)

        for endpoint_h in self.parse_info:
            list(endpoint_h.values())[0][1]["avg_response_time"] /= list(endpoint_h.values())[0][0].get("total")
            list(endpoint_h.values())[0][1]["avg_response_time"] = round(
                list(endpoint_h.values())[0][1]["avg_response_time"], 3)
