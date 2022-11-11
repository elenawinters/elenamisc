from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import soup2dict
import pathlib
import json
import time
import os


# https://stackoverflow.com/a/48666749/14125122
# https://stackoverflow.com/a/5041056/14125122

pwd = pathlib.Path(__file__).parent.resolve()
wiki = "https://nopixel.fandom.com/wiki/"

total_officers = []

browser = webdriver.Chrome(pathlib.Path(pwd, 'chromedriver.exe'))


def PullPeaceOfficers(department=None):
    if not department: return None
    if ' ' in department:
        department = department.replace(' ', '_')

    # browser = webdriver.Chrome(pathlib.Path(pwd, 'chromedriver.exe'))
    browser.get(wiki + department + '/Members')

    html = browser.execute_script('return document.body.innerHTML;')
    soup = BeautifulSoup(html, 'html.parser')

    container = soup.find('div', {'id': 'gallery-0'})
    # print(container)
    entries = container.find_all('div', class_='wikia-gallery-item')
    structure = {}
    for entry in entries:
        details = entry.find('div', {'class': 'lightbox-caption'})
        detail = details.findChildren()

        total_officers.append(detail[0].find(text=True))
        rank = str(detail[2].find(text=True)).replace('  ', ' ')
        if rank not in structure:
            structure[rank] = 0
        structure[rank] += 1
    return structure


if __name__ == '__main__':
    departments = [
        "Cerberus Police Department",
        "Los Santos Police Department",
        "Senora Desert Sheriff's Office",
        "San Andreas State Police",
        "San Andreas State Park Rangers"
        # "Department of Corrections"
    ]
    details = {}
    details['Notice'] = 'All data presented here is taken from the NoPixel Fandom Wiki. Compiled by ElenaWinters on GitHub'
    for department in departments:
        details[department] = PullPeaceOfficers(department)
        # details.append(PullPeaceOfficers(department))

    browser.close()

    # lawtotal = 0

    for department in departments:
        depttotal = 0
        employed = 0
        contract = 0
        for rank in details[department]:
            depttotal += details[department][rank]
            if 'Cadet' in rank:
                contract += details[department][rank]
                continue
            employed += details[department][rank]

        details[department]['Summary'] = {
            'Employed': employed,
            'Contract': contract,
            'Total': depttotal
        }

        # lawtotal += depttotal

        # ['Summary']['Employed'] = employed
        # details[department]['Summary']['Contract'] = contract

    details['Total number of law enforcement personel'] = len(set(total_officers))
    details['Note'] = 'People like Trooper Ranger Derby exist. We are counting by unique names for the above statistic.'

    print(json.dumps(details))
    with open(pathlib.Path(pwd, 'details.json'), 'w') as f:
        json.dump(details, f, indent=4)

    browser.quit()
