import json
import re
import brotli
from time import sleep
from seleniumwire import webdriver


driver = webdriver.Firefox()
driver.get("https://arc.northcharleston.org/Neighbors/Index.html")
sleep(5)

neighbor_dd = driver.find_element("id", "neighborDD")
options = neighbor_dd.find_elements("tag name", "option")

# Click on the different options in the dropdown
for option in options:
    if option.text == 'Select One':
        continue
    option.click()
    sleep(2)


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
    out.update({neigh: {'features': feats,
                        'spatialReference': dat.get('spatialReference')}})
    # for feat in feats:
    #     geom = feat.get("geometry")
    #     neighbor = feat.get("attributes").get('NEIGHBOR')

out.get('WINDSOR')
bad_opt = "Select One"
if bad_opt in out:
    out.pop(bad_opt)

json.dump(out,
          open('north_charleston_sc_neighbhoods_polygons.json', 'w'))