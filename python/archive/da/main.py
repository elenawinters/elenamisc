from pyquery import PyQuery as pq
from collections import OrderedDict
import requests

def get_secret_message(url: str, debug: bool = False) -> str:
    page = requests.get(url)
    d = pq(page.text)

    table_items = [i.text().replace('\n', ',') for i in d('table').items('tr')]
    table_items.pop(0)  # remove the thing that says, hey, this column is this, cuz we don't need that
    sorted_table = sorted(table_items, key=lambda x: (int(x.split(',')[2]), int(x.split(',')[0])))

    grid = OrderedDict()

    # Create grid data
    for tab in sorted_table:
        x, z, y = tab.split(',')
        y, x = int(y), int(x)
        if debug:
            print(y, x, z)
        if y not in grid:
            grid[y] = OrderedDict()
            if x not in grid[y]:
                grid[y][x] = ''
        grid[y][x] = z
    if debug:
        print(grid)

    secret_message = ''
    for y in reversed(grid):
        line = ''
        for x in range(0, next(reversed(grid[y])) + 1):
            char = ' '
            if x in grid[y]:
                char = grid[y][x]
            line += char
        secret_message += line + '\n'
    return secret_message

if __name__ == '__main__':
    secrets = [
        "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub",
        "https://docs.google.com/document/d/e/2PACX-1vSFTq6KR8ER5h9_bFVliDvYBntK6Wv8L7x6hLp2Sm58Zkhpo7Vsba9BmC82wcy8WoR3Q47J-brCiH3c/pub"
    ]
    for secret in secrets:
        print(get_secret_message(secret))