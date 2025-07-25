import argparse
from utils.log_parser import LogParser

def main():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--file", type=str)
    argument_parser.add_argument("--report average", type=str)
    argument_parser.add_argument(" --date", type=str)
    args = argument_parser.parse_args()
    parser = LogParser(args.file)
    parser.read_file()
    parse_handler = parser.parsing_items("url", parser.handlers)
    parse_user_agent_handler = parser.parsing_items("http_user_agent", parser.user_agent)
    parser.parse_file()
    print(parser.parse_info)




if __name__ == "__main__":
    main()
