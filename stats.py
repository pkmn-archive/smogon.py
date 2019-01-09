#!/usr/bin/env python

import requests

# TODO: should be able to determine from scraping.
DATE = '2018-12'
FOLDER = 'stats'
TIERS = ['ou']

for i in range(7):
  gen = i+1
  for tier in TIERS:
    fmt = 'gen' + str(gen) + tier
    # TODO: should be able to determine this through scraping.
    rating = 1825 if fmt == 'gen7ou' else 1760
    json = fmt + '-' + str(rating) + '.json'
    url = 'https://www.smogon.com/stats/' + DATE + '/chaos/' + json

    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(FOLDER + '/' + json, 'w') as handle:
        for block in response.iter_content(1024):
            handle.write(block)
