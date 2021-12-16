from selenium import webdriver

class infow():
    def __init__(self):
        self.driver = webdriver.chrome(executable_path=C:\Users\user\Downloads\chromedriver.exe)

    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org")