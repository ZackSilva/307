# Imports and defines dependencies to leverage Firefox with Selenium capabilities
import selenium
from selenium import webdriver
import requests
import sys
import webbrowser
import bs4
browser = webdriver.Firefox()
type(browser)

# Grabs commandline arguments and requests the search page
def GetArgs(res):
    print('Searching...')  # display text while downloading the search result page
    res = requests.get('https://google.com/search?q=' 'https://www.blackhat.com/html/bh-media-archives/bh-archives-2000.html'
                       + ' '.join(sys.argv[1:]))
    res.raise_for_status()

# Grabs desired website information
def GetResults(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    linkElems = soup.select('.package-snippet')

# Function to implement PyLoader, the main function for this utility
def PyLoader():
    res = None
    print("Welcome to PyLoader!")
    print('~' * 40)
    GetArgs(res)
    GetResults(res)

if __name__ == '__main__':
    PyLoader()