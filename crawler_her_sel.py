# crawler_her_sel.py
# -*- coding: utf-8 -*-

import time

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--headless")
driver = Firefox(options=options)
driver.get("https://www.flashscore.com/")
# Wait for page to fully render
time.sleep(5)
pageSource = driver.page_source
bsObj = BeautifulSoup(pageSource, "html.parser")
games = bsObj.find_all("div", {"class":\
    "event__participant event__participant--home"})
# print(len(games))

for game in games:
    print(game.get_text())

driver.quit()