if __name__ == '__main__':

    # Imports and defines dependencies to leverage Firefox with Selenium capabilities
    from selenium import webdriver
    browser = webdriver.Firefox()
    type(browser)

    def PyScraper():
        print("Welcome to PyScraper.")
        print("*" * 30)

        # This function prompts the user for a website URL in the format
        # 'www.<URL>.<.com or other TLD>'
        def GetWebsite():
            website = input("Please enter a website URL using the format 'www.<URL>.<.com or other TLD>':")

            # This function leverages Selenium to open the inputted URL via Firefox
            def OpenBrowser():
                browser.get(website)

            OpenBrowser()

        GetWebsite()

    PyScraper()