# Crawler to scrap the web page https://www.flashscore.com/ .

## Motivation:
Herminio Henriques on Stack Overflow started the topic: "Beautifulsoup4 
find_all not getting the results I need" -
https://stackoverflow.com/questions/69181329/beautifulsoup4-find-all-not-getting-the-results-i-need/69191220#69191220 . 
I decided to answer this question with the help of this crawler (code).

## Requirements: 
python 3.9 - rest in requirements.txt .

## Remarks:
- I made this script so that the master branch had always 
  the functioning code. 
- To run the script you must run the file "crawler_her_sel.py". 

## Script Summary:
After you run the script, you must wait for the programm to finish. In 
the directory where the script file is located, a csv file with a name 
will appear, e.g. "flashscore20211213-10.27.30". In the file 
flashscore20211213-10.27.30.csv the exact date and time of the scraping 
is saved in the name. When you load the data from the csv file into 
Excel 2019, the following data layout appears:

<img src="https://github.com/OliverWisn/alien_invasion/blob/master/assets/demo_3.jpg" width=1000>

## Version:
This is version 1.00 of the crawler.
