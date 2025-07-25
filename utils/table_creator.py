from tabulate import tabulate

class TableCreator:
    def __init__(self, info, argument):
        self.info = info
        self.argument = argument

    def create_table(self):
        table = []
        if self.argument == "average":
            for elems in self.info:
                if not table:
                    table.append(['handler', 'total', 'avg_response_time'])

        table = tabulate(table, headers="firstrow", tablefmt="grid")
        print(table)
