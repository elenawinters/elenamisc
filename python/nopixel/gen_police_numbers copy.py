from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import soup2dict
import json
import time


# https://stackoverflow.com/a/48666749/14125122
# https://stackoverflow.com/a/5041056/14125122

wiki = "https://nopixel.fandom.com/wiki/"


def PullPeaceOfficers(department=None):
    if not department: return None


if __name__ == '__main__':
    PullPeaceOfficers()


def ActiveHasroot(server=None):

    if server:
        url = f'https://{server}.hasroot.com/'
    else:
        url = f'https://gtarp.hasroot.com/'

    # options = Options()
    # options.headless = True
    browser = webdriver.Chrome()
    browser.get(url)
    # /html/body/div[4]/div[3]/div[3]/main/div[3]/div[2]/div/div[2]

    html_inner = browser.execute_script('return document.body.innerHTML;')

    # with open('htmldump.txt', 'w', encoding='utf-8') as f:
    #     f.write(html_inner)

    soup = BeautifulSoup(html_inner, 'html.parser')

    container = soup.find('div', {'id': 'streamContainers'})
    servers = container.find_all('section')

    servers = [soup2dict.convert(x) for x in servers]

    browser.close()

    # with open('soupdump.json', 'w', encoding='utf-8') as f:
    #     f.write(json.dumps(servers, indent=4))

    names = []
    for serv in servers:
        for div in serv['div'][1:]:
            if 'article' not in div: continue
            for article in div['article']:
                names.append(article['@id'])

    print(len(names))
    with open('names.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(names, indent=4))

    return names


# if __name__ == '__main__':
#     ActiveHasroot()
