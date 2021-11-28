# crawler_her_sel.py
# -*- coding: utf-8 -*-

import time

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

my_url = "https://www.flashscore.com/"
options = Options()
options.add_argument("--headless")
driver = Firefox(options=options)
driver.get(my_url)
# Wait for page to fully render
# time.sleep(5)
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(By.CLASS_NAME, "tv-ico.icon.icon--tv"))
finally:
    pageSource = driver.page_source
    bsObj = BeautifulSoup(pageSource, "html.parser")
    games = bsObj.find_all("div", {"class":\
        "event__participant event__participant--home"})
    # print(len(games))

    for game in games:
        print(game.get_text())

    driver.quit()