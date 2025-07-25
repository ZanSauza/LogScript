import argparse
from utils.log_parser import LogParser
from utils.table_creator import TableCreator


def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--file", dest="file", type=str)
    argument_parser.add_argument("--report average", dest="report_average", type=str)
    argument_parser.add_argument("--date",dest="date", type=str)

    args = argument_parser.parse_args()

    file_path = args.file
    arg_report = args.report_average
    arg_date = args.date

    parser = LogParser(file_path)
    parser.read_file()
    parse_handler = parser.parsing_items("url", parser.handlers)
    parse_user_agent_handler = parser.parsing_items("http_user_agent", parser.user_agent)
    parser.parse_file()
    table1 = TableCreator(parser.parse_info, arg_report)
    table1.create_table()

    # print(parser.parse_info)


if __name__ == "__main__":
    main()
