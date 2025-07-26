from tabulate import tabulate

class TableCreator:
    def __init__(self, info, argument):
        self.info = info
        self.argument = argument

    def create_table(self):
        table = []
        if self.argument == "average":
            for elems in self.info:
                print(elems.items())
                if not table:
                    table.append(['handler', 'total', 'avg_response_time'])
                    table.append([[key for key in elems.keys()][-1],
                                  [value[0]['total'] for value in elems.values()][-1],
                                  [value[1]['avg_response_time'] for value in elems.values()][-1]])
                else:
                    table.append([[key for key in elems.keys()][-1],
                                  [value[0]['total'] for value in elems.values()][-1],
                                  [value[1]['avg_response_time'] for value in elems.values()][-1]])



        print(table)
        table = tabulate(table, headers="firstrow", tablefmt="grid")
        print(table)