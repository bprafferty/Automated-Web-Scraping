#Author: Brian Rafferty
#Date: 7/28/2020
#Title: Automated Data Mining
#Description: Program accesses my personal portfolio website
#               using requests, and returns a BeautifulSoup
#               object containing the HTML data for the page.
#               I then create a blank CSV file and write an
#               initial row detailing the titles of each column.
#               With the HTML object and the CSV file both prepared, 
#               I then scrape the project data from the HTML and
#               append each project to the CSV file in their 
#               corresponding rows. The entire process is automated
#               using schedule and time, scraping my portfolio
#               immediately after the script is initially run
#               and each subsequent morning at 9:00 am.
 
from bs4 import BeautifulSoup
import requests
import csv
import schedule
import time


headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

'''
Description: Connect to URL using requests and return web content
Input: url to connect to, headers to bypass access controls
Output: BeatifulSoup html object containing url's data
'''
def connectToWeb(url, headers):
    req = requests.get(url, headers)
    return BeautifulSoup(req.content, 'lxml')

url = "https://www.brianrafferty.net/projects/"

soup = connectToWeb(url, headers)

'''
Description: Create CSV file and write first row with column names
Input: name of output csv file, list of column names
Output: None
'''
def createFile(csvName, contentList):
    csvFile = open(csvName, 'w')
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(contentList)
    csvFile.close()


csvName = 'scrape.csv'
contentList = ['title', 'content', 'date', 'image']

createFile(csvName, contentList)

'''
Description: Appends each project to the CSV file after scraping the data
                out of the HTML within the BeautifulSoup object.
Input: CSV file name, BeautifulSoup object containing HTML
Output: None
'''
def appendCSVPortfolio(csvName, soup):
    outputFile = open(csvName, 'a')
    csvWriter = csv.writer(outputFile)
    for project in soup.find_all('div', class_='row justify-content-center no-gutters mb-5 mb-lg-0'):

        title = project.h4.a.text

        content = project.p.a.text

        date = project.find('div', class_='project-text w-100 my-auto text-center text-lg-left').a.text

        image = project.img.get('src')

        csvWriter.writerow([title, content, date, image])
        print(title)
        print(content)
        print(date)
        print(image)
        print('')

    outputFile.close()


appendCSVPortfolio(csvName, soup)


'''
Automate the process to happen every morning at 9:00 am
'''
schedule.every().day.at("09:00").do(appendCSVPortfolio, csvName, soup)

while 1:
    schedule.run_pending()
    time.sleep(1)
