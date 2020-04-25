"""
This file was made by Nimrod Rappaport on: "25/4/2020".
It was made to help with the hebrew translation of Rimworld.
I take no responsibility for people's actions with this code. In the translation and outside of it.
"""
import re
import sys

file_path = input("Input file path: ")
pattern = r"( *)<[^!].*>([\d\WA-Za-z]*)<.*>"
comment_identifier = r"<!--"
try:
    data = open(file_path, "r", encoding="utf-8").readlines()
except FileNotFoundError:
    print("File not found! Are you sure the file's path is correct?")
    sys.exit()
output_data = []
line_already_commented = False
for i in data:
    match = re.search(pattern, i)
    if match and not line_already_commented:
        line_already_commented = False
        inTag = match.group(1) + "<!-- EN: " + match.group(2) + " -->\n"
        output_data.extend([inTag, i])
    else:
        output_data.append(i)
    if comment_identifier in i:
        line_already_commented = True

file = open(file_path, "w", encoding="utf-8")
for i in output_data:
    file.write(i)
file.close()
print("File: " + file.name + ", at path: " + file_path + ", was commented successfully.")
