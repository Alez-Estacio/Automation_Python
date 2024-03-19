import json


def ReturnMenuElements():
  elements = {
    "NATIONAL_DEX_LINK": {
      "selector": "div[class='grid-row'] a[href*='national']",
      "format": "CSS"
    }
  }
  return json.loads(json.dumps(elements))