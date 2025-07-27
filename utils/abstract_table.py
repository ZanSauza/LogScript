from abc import ABC, abstractmethod
from tabulate import tabulate
from typing import List


class BaseTableCreator(ABC):
    @abstractmethod
    def create_table(self, info):
        pass


class AverageTableCreator(BaseTableCreator):
    def create_table(self, info: List) -> str:
        table = [['handler', 'total', 'avg_response_time']]
        for elems in info:
            table.append([[key for key in elems.keys()][-1],
                          [value[0]['total'] for value in elems.values()][-1],
                          [value[1]['avg_response_time'] for value in elems.values()][-1]])

        table = tabulate(table, headers="firstrow", tablefmt="grid")

        return table


class UserAgentTableCreator(BaseTableCreator):
    def __init__(self, user_agents):
        self.user_agents = user_agents

    def create_table(self, info: List) -> str:
        table = [['handler', 'total']]
        for user_agent in self.user_agents:
            table[0].append(user_agent)
        for elem in info:
            table.append([[key for key in elem.keys()][-1],
                          [value[0]['total'] for value in elem.values()][-1],
                          *[[list(value[1]['user_agent'][i].values())[-1] for value in elem.values()][-1] for i in
                            range(len(self.user_agents))]
                          ])

        table = tabulate(table, headers="firstrow", tablefmt="grid")
        return table
