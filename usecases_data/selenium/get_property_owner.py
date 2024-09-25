from time import sleep
from random import uniform
import csv
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

log_file = 'get_property_owner.log'
logging.basicConfig(format="%(asctime)-15s %(message)s",
                    filename=log_file,
                    level=logging.INFO)

# original data
# sales = pd.read_excel("rollingsales_manhattan.xlsx", skiprows=4)
# sales.columns
# sales['Property Owner(s)'] = "not queried"
# sales.to_csv("rollingsales_manhattan.csv", quoting=csv.QUOTE_NONNUMERIC, index=False)
# updatable data
sales = pd.read_csv("rollingsales_manhattan.csv")
sales = sales.sample(frac=1).reset_index()
sales.BLOCK = sales.BLOCK.astype(str)
sales.LOT = sales.LOT.astype(str)

driver = webdriver.Firefox()
driver.get("https://a836-pts-access.nyc.gov/care/search/commonsearch.aspx?mode=persprop")
try:
  WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "btAgree"))
  )
  agree_button = driver.find_element(By.NAME, "btAgree")
  agree_button.click()
except Exception as e:
  logging.error(e)
  logging.error("cannot find the agree page that data may not be recent")

unknown_owners = sales.index[sales['Property Owner(s)'] == "not queried"]
for i in iter(unknown_owners):
  try:
    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.NAME, "inpTag"))
    )
    block = sales.loc[i, 'BLOCK']
    lot = sales.loc[i, 'LOT']

    block_field = driver.find_element(By.NAME, "inpTag")
    block_field.clear()
    block_field.send_keys(str(block))
    lot_field = driver.find_element(By.NAME, "inpStat")
    lot_field.clear()
    lot_field.send_keys(int(lot))
    search_button = driver.find_element(By.NAME, "btSearch")
    search_button.click()
  except Exception as e:
    logging.error(e)
    logging.error("entering block/lot information had an issue")
    logging.error(f"failed with block {block} and lot {lot}")
    break
  
  try:
    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.ID, "Property Owner(s)"))
    )
    sales.loc[i, 'Property Owner(s)'] = driver.find_element(By.XPATH, "//table[@id='Property Owner(s)']//td[contains(@class, 'DataletData')]").text
  except Exception as e:
    logging.error(e)
    logging.error('Cannot find the property owner field')
    logging.error(f"failed with block {block} and lot {lot}")
    sales.loc[i, 'Property Owner(s)'] = 'Error, possibly duplicates'
    continue

  if i and not i % 40:
    sales.to_csv("rollingsales_manhattan.csv", quoting=csv.QUOTE_NONNUMERIC, index=False)
    logging.info(f'stored {i} properties')
  
  driver.back()
  sleep(uniform(2.33, 5.33))
  
if i == sales.shape[0]:
  logging.info('finished all data poinst')

sales.to_csv("rollingsales_manhattan.csv", quoting=csv.QUOTE_NONNUMERIC, index=False)

driver.quit()
