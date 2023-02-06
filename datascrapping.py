import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Remote(
   command_executor='http://127.0.0.1:4444/wd/hub',
   options=webdriver.FirefoxOptions()
)
driver.get("http://www.mcoutinhopecas.pt/")

elements = driver.find_elements(By.CSS_SELECTOR, "[data-year]")

stats = {}

for element in elements:
   stats[element.get_attribute("data-year")] = element.get_attribute("data-value")

with open("data.json", "w") as outfile:
   json.dump(stats, outfile, indent=4)

driver.close()