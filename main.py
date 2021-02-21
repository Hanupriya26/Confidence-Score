import parse_json
from pip._vendor.distlib.compat import raw_input


def main():
    string_list = get_input()
    parse_json.parse(string_list)


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
