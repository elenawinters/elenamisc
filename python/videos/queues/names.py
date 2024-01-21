# taken from my abandoned Stitch project and updated for this one
from enum import Enum, auto
import httpx as requests
import random


class NameURLs(Enum):
    male = 'https://www.randomlists.com/data/names-male.json'
    female = 'https://www.randomlists.com/data/names-female.json'
    first = 'https://www.randomlists.com/data/names-first.json'
    last = 'https://www.randomlists.com/data/names-surnames.json'



names = {}
names[1] = requests.get(NameURLs.male.value).json()['data']
names[2] = requests.get(NameURLs.female.value).json()['data']
names[3] = requests.get(NameURLs.first.value).json()['data']
names['last'] = requests.get(NameURLs.last.value).json()['data']


def random_name():
        sex = random.randint(1, 3)

        f = random.choice(names[sex])
        la = random.choice(names['last'])

        return f'{f} {la}'
