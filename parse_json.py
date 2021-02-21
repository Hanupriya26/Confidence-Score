import json
import array as arr


def check(word, string_list):
    # print wd
    n = len(string_list)
    for i in range(n):
        if string_list[i] == word:
            return True

    return False


def parse(string_list):
    # Opening JSON file
    f = open('data.json', )
    # data2=data['1']
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    confidence_map = []
    # Iterating through the json
    # list
    for i in data['1']['lines']:
        for j in i['words']:
            if check(j['text'], string_list):
                print(j['text'], j['confidence'])
                # confidence_map is 1d array of pairs
                confidence_map.append((j['text'], j['confidence']))
        # Closing file
    f.close()
    return confidence_map
