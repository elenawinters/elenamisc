# taken from my abandoned Stitch project and updated for this one
from enum import Enum, auto
import httpx as requests
import random


class NameURLs(Enum):
    male = 'https://www.randomlists.com/data/names-male.json'
    female = 'https://www.randomlists.com/data/names-female.json'
    first = 'https://www.randomlists.com/data/names-first.json'
    middle = 'https://www.randomlists.com/data/middle-names.json'
    last = 'https://www.randomlists.com/data/names-surnames.json'
    nicknames = 'https://www.randomlists.com/data/nicknames.json'
    cat = 'https://www.randomlists.com/data/cat-names.json'
    dog = 'https://www.randomlists.com/data/dog-names.json'
    pet = 'https://www.randomlists.com/data/pet-names.json'

    class Spanish(Enum):
        first = 'https://www.randomlists.com/data/names-first-spanish.json'
        last = 'https://www.randomlists.com/data/names-last-spanish.json'

    default = first


names = {}
names[1] = requests.get(NameURLs.male.value).json()['data']
names[2] = requests.get(NameURLs.female.value).json()['data']
names[3] = requests.get(NameURLs.first.value).json()['data']
names['last'] = requests.get(NameURLs.last.value).json()['data']


def name_generator():
        sex = random.randint(1, 3)

        f = random.choice(names[sex])
        la = random.choice(names['last'])

        return f'{f} {la}'
