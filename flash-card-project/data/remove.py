import re

with open("words.txt", "r", encoding="utf-8") as file:
    file_content = file.read()

remove_content = re.sub(r'\d+', '', file_content)

with open("words.txt", "w", encoding="utf-8") as file:
    file.write(remove_content)

