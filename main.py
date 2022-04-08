if __name__ == '__main__':
    import selenium
    import webbrowser
    class PyScraper:
        print("Welcome to PyScraper.")
        print("*" * 30)

        # This function prompts the user for a website URL in the format
        # 'www.<URL>.<.com or other TLD>'
        def GetWebsite(self, website):
            website = input("Please enter a website URL using the format 'www.<URL>.<.com or other TLD>':")
            return website

        # This function leverages Selenium to open Firefox
        def OpenBrowser():
            webbrowser.open(website)

        GetWebsite()
        OpenBrowser()

