# Imports and defines dependencies to leverage Firefox with Selenium capabilities
import selenium
from selenium import webdriver
import requests
import sys
import webbrowser
import bs4
browser = webdriver.Firefox()
type(browser)

# Grabs commandline arguments
def GetArgs():
    print('Searching...')  # display text while downloading the search result page
    res = requests.get('https://google.com/search?q=' 'https://pypi.org/search/?q='+ ' '.join(sys.argv[1:]))
    res.raise_for_status()

# Function to implement PyLoader, the main function for this utility
def PyLoader():
    print("Welcome to PyLoader!")
    print('~' * 40)
    GetArgs()

if __name__ == '__main__':
    PyLoader()