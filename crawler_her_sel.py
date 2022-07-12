# crawler_her_sel.py

import time

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import pandas as pd

def firefoxdriver(my_url):
    """
    Preparing of the browser for the work and adding the headers to 
    the browser.
    """
    # Preparing of the Tor browser for the work.
    options = Options()
    options.add_argument("--headless")
    driver = Firefox(options=options)

    return driver

def scrapingitems(driver, my_list, my_xpath):
        """
        Create appropriate lists of the data for the pandas library.
        """
        try:
            elem_to_scrap = driver.find_element(By.XPATH, my_xpath).text
            my_list.append(elem_to_scrap)
        except:
            elem_to_scrap = ""
            my_list.append(elem_to_scrap)

# Variable with the URL of the website.
my_url = "https://www.flashscore.com/"

# Preparing of the Tor browser for the work and adding the headers 
# to the browser.
driver = firefoxdriver(my_url)

# Loads the website code as the Selenium object.
driver.get(my_url)

# Prepare the blank dictionary to fill in for pandas.
matches = {}

# Preparation of lists with scraped data.
countries = []
leagues = []
home_teams = []
scores_home = []
scores_away = []
away_teams = []

# Wait for page to fully render
try:
    element = WebDriverWait(driver, 25).until(
        EC.presence_of_element_located((By.CLASS_NAME, "adsclick")))
except TimeoutException:
    print("Loading took too much time!. Please rerun the script.")
except Exception as e:
    print(str(e))
else:
    # Loads the website code as the BeautifulSoup object.
    pageSource = driver.page_source
    bsObj = BeautifulSoup(pageSource, "lxml")

    # Determining the number of the football matches with the help of 
    # the BeautifulSoup.
    games_1 = bsObj.find_all(
            "div", {"class": 
            "event__participant event__participant--home"})
    games_2 = bsObj.find_all(
            "div", {"class": 
            "event__participant event__participant--home fontBold"})
    games_3 = bsObj.find_all(
            "div", {"class": 
            "event__participant event__participant--away"})
    games_4 = bsObj.find_all(
            "div", {"class": 
            "event__participant event__participant--away fontBold"})

    # Determining the number of the countries for the given football 
    # matches.
    all_countries = driver.find_elements(By.CLASS_NAME, "event__title--type")

    # Determination of the number that determines the number of 
    # the loop iterations.
    sum_to_iterate = len(all_countries) + len(games_1) + len(games_2) 
    + len(games_3) + len(games_4)

    for ind in range(1, (sum_to_iterate+1)):
        # Scraping of the country names.
        xpath_countries = ('//div[@class="sportName soccer"]/div['+str(ind)
                            +']/div[2]/div/span[1]')
        scrapingitems(driver, countries, xpath_countries)

        # Scraping of the league names.
        xpath_leagues = ('//div[@class="sportName soccer"]/div['+str(ind)
                        +']/div[2]/div/span[2]')
        scrapingitems(driver, leagues, xpath_leagues)
        
        # Scraping of the home team names.
        xpath_home_teams = ('//div[@class="sportName soccer"]/div['+str(ind)
                            +']/div[3]')
        scrapingitems(driver, home_teams, xpath_home_teams)

        # Scraping of the home team scores.
        xpath_scores_home = ('//div[@class="sportName soccer"]/div['+str(ind)
                            +']/div[5]')
        scrapingitems(driver, scores_home, xpath_scores_home)

        # Scraping of the away team scores.
        xpath_scores_away = ('//div[@class="sportName soccer"]/div['+str(ind)
                            +']/div[6]')
        scrapingitems(driver, scores_away, xpath_scores_away)

        # Scraping of the away team names.
        xpath_away_teams = ('//div[@class="sportName soccer"]/div['+str(ind)
                            +']/div[4]')
        scrapingitems(driver, away_teams, xpath_away_teams)
       
    # Add lists with the scraped data to the dictionary in the correct 
    # order.
    matches["Countries"] = countries
    matches["Leagues"] = leagues
    matches["Home_teams"] = home_teams
    matches["Scores_for_home_teams"] = scores_home
    matches["Scores_for_away_teams"] = scores_away
    matches["Away_teams"] = away_teams

    # Creating of the frame for the data with the help of the pandas 
    # package.
    df_res = pd.DataFrame(matches)

    # Saving of the properly formatted data to the csv file. The date 
    # and the time of the scraping are hidden in the file name.
    name_of_file = lambda: "flashscore{}.csv".format(time.strftime(
        "%Y%m%d-%H.%M.%S"))
    df_res.to_csv(name_of_file(), encoding="utf-8")

finally:
    driver.quit()