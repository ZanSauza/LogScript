import argparse
from utils.log_parser import LogParser
from utils.table_creator import TableCreator


def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--file", dest="file", type=str)
    argument_parser.add_argument("--report average", dest="report_average", type=str)
    argument_parser.add_argument("--date",dest="date", type=str)
    argument_parser.add_argument("--table", dest="table", type=str)

    args = argument_parser.parse_args()

    file_path = args.file
    arg_report = args.report_average
    arg_date = args.date

    parser = LogParser(file_path)
    parser.read_file()
    parse_handler = parser.parsing_items("url", parser.handlers)
    parse_user_agent_handler = parser.parsing_items("http_user_agent", parser.user_agent)
    if not arg_date:
        parser.parse_file()
        table1 = TableCreator(parser.parse_info, arg_report)
        table1.create_table()
    if arg_date:
        date = f'{arg_date[0]+arg_date[1]+arg_date[2]+arg_date[3]+arg_date[4]+arg_date[8]+arg_date[9]+arg_date[7]+arg_date[5]+arg_date[6]}'
        parser.parse_file(date)
        table2 = TableCreator(parser.parse_info, arg_report)
        table2.create_table()


    # print(parser.parse_info)


if __name__ == "__main__":
    main()
