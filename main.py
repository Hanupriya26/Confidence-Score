import parse_json
import sql_query

from pip._vendor.distlib.compat import raw_input


def main():
    # string_list = get_input()
    string_list = ["Name", "Max", "PORFORMA", "Email"]
    confidence_map = parse_json.parse(string_list)
    # sql_query.setup_table()
    sql_query.insert_into_table(confidence_map)


def get_input():
    # number of elements as input
    n = int(input("Enter number of elements : "))
    # iterating till the range
    string_list = []

    for i in range(n):
        g = raw_input()
        string_list.append(g)

    return string_list


if __name__ == '__main__':
    main()
