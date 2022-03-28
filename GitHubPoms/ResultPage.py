from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import select

from  GitHubPoms import PomBase
from selenium import webdriver
import unittest

class ResultPage():


    def __init__(self, driverParam):
        self.driver= driverParam


    mainPageBodyByClassName = 'body'
    mainPageByClassName = 'application-main'
    searchResultByXpath = "//div[@class='px-2']//h3[contains(.,'result')]"
    repoNameByXpath = "//ul[@class='repo-list']//a"


    def verifySearchResult(self):
        searchResultLbl = self.driver.find_element_by_xpath(self.searchResultByXpath)
        return searchResultLbl.get_attribute("innerHTML")

    def verifyRepoName(self):
        searchResultLbl = self.driver.find_element_by_xpath(self.repoNameByXpath)
        print(searchResultLbl.get_attribute("innerHTML"))
        return searchResultLbl.get_attribute("innerHTML")

    def navigateToRepo(self):
        searchResultLbl = self.driver.find_element_by_xpath(self.repoNameByXpath)
        searchResultLbl.click();