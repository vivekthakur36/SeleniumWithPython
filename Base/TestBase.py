from selenium import webdriver
from Base.BrowserFactory import BrowserFactory

class TestBase:
    driver = None

    @staticmethod
    def beforetest(self):
        driver = BrowserFactory.getBrowserDriver(self,"Chrome")
        return driver


