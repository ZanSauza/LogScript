import argparse

from utils.log_parser import LogParser
from utils.abstract_table import AverageTableCreator, UserAgentTableCreator
from utils.abstract_report import ReportAverage, ReportUserAgent


def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--file", dest="file", type=str)
    argument_parser.add_argument("--report average", dest="report_average", type=str)
    argument_parser.add_argument("--user agent", dest="user_agent", type=str)
    argument_parser.add_argument("--date", dest="date", type=str)

    args = argument_parser.parse_args()

    file_path = args.file
    arg_report = args.report_average
    arg_date = args.date
    arg_useragent = args.user_agent

    parser = LogParser(file_path)
    data = parser.read_file()

    parse_handler = parser.parsing_items("url")
    parse_user_agent_handler = parser.parsing_items("http_user_agent")

    report_average = ReportAverage(data, parse_handler)
    report_user_agent = ReportUserAgent(data, parse_handler, parse_user_agent_handler)

    if not arg_date and arg_report:
        report_average_info = report_average.generate_report()
        table1 = AverageTableCreator()
        print(table1.create_table(report_average_info))

    if not arg_date and arg_useragent:
        report_user_agent.generate_report()
        table3 = UserAgentTableCreator(parse_user_agent_handler)
        print(table3.create_table(report_user_agent.parse_info))

    if arg_date:
        date = f'{arg_date[0] + arg_date[1] + arg_date[2] + arg_date[3] + arg_date[4] + arg_date[8] + arg_date[9] + arg_date[7] + arg_date[5] + arg_date[6]}'

        if arg_date and arg_report:
            a_data = report_average.generate_report(date)
            if type(a_data) != str:
                table2 = AverageTableCreator()
                print(table2.create_table(report_average.parse_info))
            else:
                print(a_data)

        if arg_date and arg_useragent:
            u_data = report_user_agent.generate_report(date)
            if type(u_data) != str:
                table4 = UserAgentTableCreator(parse_user_agent_handler)
                print(table4.create_table(report_user_agent.parse_info))
            else:
                print(u_data)


if __name__ == "__main__":
    main()
