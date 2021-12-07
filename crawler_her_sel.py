# crawler_her_sel.py
# -*- coding: utf-8 -*-

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        EC.presence_of_element_located((By.ID, "box-over-content-a")))
finally:
    # Loads the full code of the page into a variable.
    pageSource = driver.page_source

    # Determining the number of the football matches based on 
    # the attribute.
    soccer = driver.find_element(By.XPATH , "/html/body/div[5]/div/div[1]/a[1]")
    matches_soccer = soccer.get_attribute("data-sport-count")

    # Determining the number of the countries for the given football 
    # matches.
    countries = driver.find_elements(By.CLASS_NAME , "event__title--type")

    # Determination of the number that determines the number of 
    # the loop iterations.
    sum_to_iterate = int(matches_soccer) + len(countries)
    
    for ind in range(1, (sum_to_iterate + 1)):
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
    print(df_res)

    driver.quit()