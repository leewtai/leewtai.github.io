import json
import re
import brotli
from time import sleep
from seleniumwire import webdriver

import requests


driver = webdriver.Firefox()
driver.get("https://arc.northcharleston.org/Neighbors/Index.html")
sleep(5)

neighbor_dd = driver.find_element("id", "neighborDD")
options = neighbor_dd.find_elements("tag name", "option")

for option in options:
    if option.text == 'Select One':
        continue
    option.click()
    sleep(2)

reqs = driver.requests

out = {}
for req in reqs:
    where = req.params.get('where')
    if not where or 'NEIGHBOR=' not in where:
        continue
    neigh = re.sub(r"NEIGHBOR='(.*)'", r"\1", where)
    resp = req.response
    bod = brotli.decompress(req.response.body)
    dat = json.loads(bod)
    feats = dat.get("features")
    out.update({neigh: feats})
    # for feat in feats:
    #     geom = feat.get("geometry")
    #     neighbor = feat.get("attributes").get('NEIGHBOR')

len(out)
set(out.keys()).difference({o.text for o in options})
{o.text for o in options}.difference(set(out.keys()))
out.get('WINDSOR')

