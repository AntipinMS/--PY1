import json

INPUT_FILE = "input1.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:
    with open(filename) as f:
        str_ = f.read()
        list_of_lists = str_.split(new_line)
        list_of_lists.pop(-1)
        list_for_help = []
        for i in list_of_lists:
            list_for_help.append(i.split(delimiter))
        number_of_columns = len(list_for_help[0])
        number_of_strings = len(list_for_help)
        list_of_dicts = [{} for i in range(number_of_strings-1)]
        for i in range(number_of_strings-1):
            for j in range(number_of_columns):
                list_of_dicts[i][list_for_help[0][j]] = list_for_help[i+1][j]
        return list_of_dicts


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
