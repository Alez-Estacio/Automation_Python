import json


def NationalDex_ListPokemon():
  elements = {
    "POKEMON_NAME_LINK": {
      "selector": "a[class='ent-name']",
      "format": "CSS"
    },
  "POKEMON_NUMBER_LABEL": {
      "selector": "span[class*='infocard']>small:nth-child(1)",
      "format": "CSS"
    }
  }
  return json.loads(json.dumps(elements))