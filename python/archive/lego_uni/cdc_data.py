# Old script to get all possible item LOTs from the game CDClient.
# This will returns LOTs not found in the items table.

import sqlite3
file = open('output.txt', 'w')
print('start', file=file)

# description = '''A bot to protect against swearing and spam.'''
# bot = commands.Bot(command_prefix='.', description=description)

conn = sqlite3.connect('cdclient.sqlite')
cdc = conn.cursor()

con = sqlite3.connect('cdc_data.sqlite')
sort = con.cursor()

sort.execute('''CREATE TABLE IF NOT EXISTS objects
             (id int32, name text_4, displayName text_4, type text_4, description text_4, render_asset text_4, icon_asset text_4)''')

# con.commit()

# for x in cdc.execute("SELECT id, render_asset, icon_asset FROM RenderComponent"):
x_id = []
x_re = []
x_ic = []
for x in cdc.execute("SELECT id, render_asset, icon_asset FROM RenderComponent"):
    x_id.append(x[0])
    x_re.append(x[1])
    x_ic.append(x[2])

for x in range(len(x_id)):
    for z in cdc.execute("SELECT id FROM ComponentsRegistry WHERE component_type = '2' AND component_id = ?", (x_id[x], )):
        name = None
        displayName = None
        type = None
        description = None
        for y in cdc.execute("SELECT name, displayName, type, description FROM Objects WHERE id = ?", (z[0], )):
            name = y[0]
            displayName = y[1]
            type = y[2]
            description = y[3]
            break
        try:
            print(f'{z[0]}, {name}, {displayName}, {type}, {description}, {x_re[x]}, {x_ic[x]}', file=file)
        except Exception:
            pass
        sort.execute("INSERT INTO objects VALUES (?, ?, ?, ?, ?, ?, ?)", (z[0], name, displayName, type, description, x_re[x], x_ic[x], ))
        break


con.commit()
print('fin', file=file)
file.close()
