import json
from fuzzywuzzy import fuzz


text = open('references/country.json', 'r').read()
countries = json.loads(text)['RECORDS']


def fuzzy_match(s1, s2):
    ratio = fuzz.ratio(s1, s2)
    if ratio > 95:
        return True
    return False


def match_country_id(name):
    for c in countries:
        if fuzzy_match(name, c['name']):
            return c['id']

