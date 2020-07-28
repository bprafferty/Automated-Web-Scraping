Automated Data Mining

This program automates the data mining process of connecting 
to a url, scraping its HTML data, parsing the data for needed
content, and writing the selected data to a csv file. The script
is designed to run automatically every morning at 9:00 am, and
simulates how Data Mining could be used to pull the most recent 
data updates from a website for business applications.

To run this program:

    - Open your terminal, and cd to project directory

    - type: python scrape.py

Dependencies:

    - Python 2.7
    - BeautifulSoup
    - requests
    - csv
    - schedule
    - time