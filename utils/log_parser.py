import json
from typing import Union, List


class LogParser:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.data = []

    def read_file(self) -> Union[List, None]:
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

    def parsing_items(self, sstr: str) -> Union[List, None]:
        llist = []
        for i in self.data:
            if i[sstr] not in llist:
                llist.append(i[sstr])

        return llist
