# crawler_her_sel.py
# -*- coding: utf-8 -*-

import time

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

# Variable with the URL of the website.
my_url = "https://www.flashscore.com/"

# Preparing of the browser for the work.
options = Options()
options.add_argument("--headless")
driver = Firefox(options=options)
driver.get(my_url)

# Prepare the blank dictionary to fill in for pandas.
dictionary_of_matches = {}

# Preparation of lists with scraped data.
list_of_countries = []
list_of_leagues = []
list_of_home_teams = []
list_of_scores_for_home = []
list_of_scores_for_away = []
list_of_away_teams = []

# Wait for page to fully render
try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, \
            "boxOverContent__bannerLink")))
finally:
    # Loads the website code as the BeautifulSoup object.
    pageSource = driver.page_source
    bsObj = BeautifulSoup(pageSource, "lxml")

    # Determining the number of the football matches with the help of 
    # the BeautifulSoup.
    games_1 = bsObj.find_all("div", {"class":\
    "event__participant event__participant--home"})
    games_2 = bsObj.find_all("div", {"class":\
    "event__participant event__participant--home fontBold"})
    games_3 = bsObj.find_all("div", {"class":\
    "event__participant event__participant--away"})
    games_4 = bsObj.find_all("div", {"class":\
    "event__participant event__participant--away fontBold"})

    for game in games_4:
        print(game.get_text())


    # Determining the number of the countries for the given football 
    # matches.
    countries = driver.find_elements(By.CLASS_NAME , "event__title--type")

    # Determination of the number that determines the number of 
    # the loop iterations.
    sum_to_iterate = len(countries) # + int(matches_soccer)
    
    for ind in range(1, (sum_to_iterate+1)):
        # Scraping of the country names.
        try:
            country = driver.find_element(By.XPATH ,\
             '//div[@class="sportName soccer"]/div['+str(ind)+\
             ']/div[1]/div/span[1]').text
            list_of_countries.append(country)
        except:
            country = ""
            list_of_countries.append(country)

        # Scraping of the league names.
        try:
            league = driver.find_element(By.XPATH ,\
             '//div[@class="sportName soccer"]/div['+str(ind)+\
             ']/div[1]/div/span[2]').text
            list_of_leagues.append(league)
        except:
            league = ""
            list_of_leagues.append(league)

        # Scraping of the home team names.
        try:
            home_team = driver.find_element(By.XPATH ,\
             '//div[@class="sportName soccer"]/div['+str(ind)+']/div[3]').text
            list_of_home_teams.append(home_team)
        except:
            home_team = ""
            list_of_home_teams.append(home_team)

        # Scraping of the home team scores.
        try:
            score_for_home_team = driver.find_element(By.XPATH ,\
             '//div[@class="sportName soccer"]/div['+str(ind)+']/div[5]').text
            list_of_scores_for_home.append(score_for_home_team)
        except:
            score_for_home_team = ""
            list_of_scores_for_home.append(score_for_home_team)

        # Scraping of the away team scores.
        try: 
            score_for_away_team = driver.find_element(By.XPATH ,\
             '//div[@class="sportName soccer"]/div['+str(ind)+']/div[6]').text
            list_of_scores_for_away.append(score_for_away_team)
        except:
            score_for_away_team = ""
            list_of_scores_for_away.append(score_for_away_team)

        # Scraping of the away team names.
        try:
            away_team = driver.find_element(By.XPATH ,\
             '//div[@class="sportName soccer"]/div['+str(ind)+']/div[4]').text
            list_of_away_teams.append(away_team)
        except:
            away_team = ""
            list_of_away_teams.append(away_team)

    # Add lists with the scraped data to the dictionary in the correct 
    # order.
    dictionary_of_matches["countries"] = list_of_countries
    dictionary_of_matches["leagues"] = list_of_leagues
    dictionary_of_matches["home_teams"] = list_of_home_teams
    dictionary_of_matches["scores_for_home_teams"] = list_of_scores_for_home
    dictionary_of_matches["scores_for_away_teams"] = list_of_scores_for_away
    dictionary_of_matches["away_teams"] = list_of_away_teams

    # Creating of the frame for the data with the help of the pandas 
    # package.
    df_res = pd.DataFrame(dictionary_of_matches)

    # Saving of the properly formatted data to the csv file. The date 
    # and the time of the scraping are hidden in the file name.
    name_of_file = lambda: "flashscore{}.csv".format(time.strftime(\
        "%Y%m%d-%H.%M.%S"))
    df_res.to_csv(name_of_file(), encoding="utf-8")

    driver.quit()