import json
import sys
import os.path


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as input_file:
            filedata = json.load(input_file)
            return filedata
    else:
        return None


def pretty_print_json(data):
    print(json.dumps(data, indent=4, ensure_ascii=False, sort_keys=True))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        path_to_file = sys.argv[1]
    else:
        print("You should specify a file to analyze!")
        sys.exit(0)
    if load_data(path_to_file):
        input_data = load_data(path_to_file)
    else:
        print("Incorrect path to the file!")
        sys.exit(0)

    # with open("output.txt", "w") as output_file:
    #     output_file.write(pretty_print_json(data))
    # print('Привет')

    pretty_print_json(input_data)
