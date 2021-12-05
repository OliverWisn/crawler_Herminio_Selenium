# crawler_her_sel.py
# -*- coding: utf-8 -*-

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

my_url = "https://www.flashscore.com/"
options = Options()
options.add_argument("--headless")
driver = Firefox(options=options)
driver.get(my_url)
# Wait for page to fully render
try:
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "box-over-content-a")))
finally:
    pageSource = driver.page_source
    soccer = driver.find_element(By.XPATH , "/html/body/div[5]/div/div[1]/a[1]")
    matches_soccer = soccer.get_attribute("data-sport-count")
    print(matches_soccer)

# /html/body/div[5]/div/div[1]/a[1]

# /html/body/div[6]/div[1]/div/div[1]/div[2]/div[5]/div[2]/div/section/div/div/div[10]/div[3]
# /html/body/div[6]/div[1]/div/div[1]/div[2]/div[5]/div[2]/div/section/div/div/div[10]/div[4]
# /html/body/div[6]/div[1]/div/div[1]/div[2]/div[5]/div[2]/div/section/div/div/div[11]/div[3]
# /html/body/div[6]/div[1]/div/div[1]/div[2]/div[5]/div[2]/div/section/div/div/div[11]/div[4]

# /html/body/div[6]/div[1]/div/div[1]/div[2]/div[5]/div[2]/div/section/div/div/div[10]/div[5]
# /html/body/div[6]/div[1]/div/div[1]/div[2]/div[5]/div[2]/div/section/div/div/div[10]/div[6]
# /html/body/div[6]/div[1]/div/div[1]/div[2]/div[5]/div[2]/div/section/div/div/div[11]/div[5]
# /html/body/div[6]/div[1]/div/div[1]/div[2]/div[5]/div[2]/div/section/div/div/div[11]/div[6]

    driver.close()