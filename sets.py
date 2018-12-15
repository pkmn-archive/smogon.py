#!/usr/bin/env python

import json
import re
import requests

import sys

GENS = ['rb', 'gs', 'rs', 'dp', 'bw', 'xy', 'sm']

def dexUrl(gen):
  return 'https://www.smogon.com/dex/' + gen + '/pokemon'

def setUrl(gen, poke):
  return dexUrl(gen) + '/' + poke

for gen in GENS:
  dex = json.loads(re.search('dexSettings = ({.*})', requests.get(dexUrl(gen)).text).group(1))

  pokemon = {}
  for poke in dex['injectRpcs'][1][1]["pokemon"]:
    if not poke["cap"]:
      mon = json.loads(re.search('dexSettings = ({.*})', requests.get(setUrl(gen, poke['name'])).text).group(1))
      pokemon[poke['name']] = mon['injectRpcs'][2][1]['strategies']

  with open(gen + '.json', 'w') as out:
    json.dump(pokemon, out, indent=2)
