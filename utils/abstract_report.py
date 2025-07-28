from abc import ABC, abstractmethod
from typing import Union, List


class BaseLogParserReport(ABC):
    def __init__(self, data: List) -> None:
        self.data = data

    @abstractmethod
    def parsing_info(self, endpoint):
        pass

    @abstractmethod
    def generate_report(self, timestamp=None):
        pass

    def date(self, timestamp):
        if timestamp:
            for endpoint in self.data:
                if endpoint["@timestamp"].startswith(timestamp):
                    self.parsing_info(endpoint)
        elif not timestamp:
            for endpoint in self.data:
                self.parsing_info(endpoint)


class ReportAverage(BaseLogParserReport):
    def __init__(self, data: List, handlers: List):
        super().__init__(data)
        self.handlers = handlers
        self.parse_info = []

    def parsing_info(self, endpoint) -> None:
        url_key = list(self.parse_info[len(self.parse_info) - 1].keys())[0]
        if endpoint["url"] == url_key:
            self.parse_info[len(self.parse_info) - 1][url_key][0]["total"] += 1
            self.parse_info[len(self.parse_info) - 1][url_key][1]["avg_response_time"] += endpoint[
                "response_time"]

    def generate_report(self, timestamp: Union[str, None] = None) -> Union[str, List[any]]:
        for handler in self.handlers:
            self.parse_info.append({handler:
                [
                    {"total": 0},
                    {"avg_response_time": 0}
                ]
            })
            self.date(timestamp)

        try:
            for endpoint_h in self.parse_info:
                list(endpoint_h.values())[0][1]["avg_response_time"] /= list(endpoint_h.values())[0][0].get("total")
                list(endpoint_h.values())[0][1]["avg_response_time"] = round(
                    list(endpoint_h.values())[0][1]["avg_response_time"], 3)
        except ZeroDivisionError:
            return "cписок значений эндпоинтов пуст, проверте корректность входных данных возможно указана некорректная дата"

        return self.parse_info


class ReportUserAgent(BaseLogParserReport):
    def __init__(self, data: List, handlers: List, user_agents: List):
        super().__init__(data)
        self.handlers = handlers
        self.user_agents = user_agents
        self.parse_info = []

    def parsing_info(self, endpoint) -> None:
        url_key = list(self.parse_info[len(self.parse_info) - 1].keys())[0]
        user_agent_keys_and_vals = self.parse_info[len(self.parse_info) - 1][url_key][1]["user_agent"]
        if endpoint["url"] == url_key:
            self.parse_info[len(self.parse_info) - 1][url_key][0]["total"] += 1
            for user_agent in user_agent_keys_and_vals:
                if endpoint["http_user_agent"] in user_agent:
                    user_agent[endpoint["http_user_agent"]] += 1

    def generate_report(self, timestamp: Union[str, None] = None) -> List[any]:
        for handler in self.handlers:
            self.parse_info.append({handler:
                [
                    {"total": 0},
                    {"user_agent": [{agent: 0} for agent in self.user_agents]},
                ]
            })
            self.date(timestamp)

        return self.parse_info
