import re


def tag_file(absolute_path):
    # Reading file
    try:
        file = open(absolute_path, "r", encoding="utf-8")
    except FileNotFoundError:
        return "Couldn't find file, commenting failed."
    # Reading data from file:
    data = file.read()
    file.close()
    # Making the comments with an overly complex regex substitution pattern:
    data = re.sub(r"(?<!-->)(\n+)((\s*)<.*>(.*)</.*>)", r"\1\3<!-- EN:\4 -->\n\2", data)
    # Opening file for writing (and removing all things that were previously written to it):
    file = open(absolute_path, "w", encoding="utf-8")
    # Writing data:
    file.write(data)
    return f"Commenting of file {absolute_path} completed successfully."


if __name__ == '__main__':
    print("It's recommended to make a copy of the file before running the program on it, as it modifies it's text.\n"
          "The program will not comment the first line in a file.")
    file_path = input("Input file's path:\n")
    print(tag_file(file_path))
