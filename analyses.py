#!/usr/bin/env python

import json
import re
import requests

import sys

FOLDER = 'debug' #'analyses'
GENS = ['sm' ] #['rb', 'gs', 'rs', 'dp', 'bw', 'xy', 'sm']

def dexUrl(gen):
  return 'https://www.smogon.com/dex/' + gen + '/pokemon'

def setUrl(gen, poke):
  return dexUrl(gen) + '/' + poke

for gen in GENS:
  dex = json.loads(re.search('dexSettings = ({.*})', requests.get(dexUrl(gen)).text).group(1))

  pokemon = {}
  for poke in dex['injectRpcs'][1][1]["pokemon"]:
    if not poke["cap"]:
      text = requests.get(setUrl(gen, poke['name'])).text
      match = re.search('dexSettings = ({.*})', text)
      if match:
        mon = json.loads(match.group(1))
        pokemon[poke['name']] = mon['injectRpcs'][2][1]['strategies']
      else:
        print >> sys.stderr, poke['name']
        print >> sys.stderr, text

  with open(FOLDER + '/' + gen + '.json', 'w') as out:
    json.dump(pokemon, out, indent=2)
