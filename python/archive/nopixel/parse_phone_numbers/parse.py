from pathlib import Path
import csv
import os
import re

os.chdir(Path(Path(__file__).parent))
sql_dump = ''
with open('the_list.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        print(re.sub(r"\D", "", row[1]), ': ', row[0])

        # sql_dump += 'INSERT IGNORE INTO `np-phones` (number, known_users) VALUES ("' + re.sub(r"\D", "", row[1]) + "`, "' + row[0] + '");\n'
        number = re.sub(r"\D", "", row[1])
        sql_dump += f'INSERT IGNORE INTO `np-phones` (number, known_users) VALUES ("{number}", "{row[0]}");\n'
        # print(', '.join(row))


with open('the_list.sql', 'w', encoding='utf-8') as f:
    f.write(sql_dump)