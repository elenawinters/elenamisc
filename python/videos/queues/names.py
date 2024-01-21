# taken from my abandoned Stitch project and updated for this one
from enum import Enum, auto
import httpx as requests
import random


class Sex(Enum):
    male = 1
    female = 2
    other = 3
    man = male
    boy = male
    m = male
    woman = female
    girl = female
    f = female
    default = other


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


def name_generator():
        sex = random.randint(1, 3)
        match sex:
            case 1:
                fr = NameURLs.male
                pref = 'M'
            case 2:
                fr = NameURLs.female
                pref = 'F'
            case 3:
                fr = NameURLs.first
                pref = 'N'

        lr = NameURLs.last
        f = requests.get(fr.value).json()['data']  # First
        la = requests.get(lr.value).json()['data']  # Last

        f = random.choice(f)
        la = random.choice(la)

        # return f'{f} {la} | {pref}'
        return f'{f} {la}'
