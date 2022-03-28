from _ast import expr
from lib2to3.pgen2 import driver

from selenium import webdriver
from webdriver_manager.chrome import  ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager



class BrowserFactory:
    driver = None

    @staticmethod
    def getBrowserDriver(self,browserName):
        if browserName == "Chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif browserName == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browserName == "Edge":
            driver = webdriver.Ie(IEDriverManager().install())
        else:
            driver = webdriver.Chrome(ChromeDriverManager().install())

        return driver