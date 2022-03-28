from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from  GitHubPoms import PomBase
from selenium import webdriver

class SearchPage():


    def __init__(self, driverParam):
        self.driver= driverParam
        #super().__init__(driverParam)

    mainPageBodyByClassName = 'body'
    mainPageByClassName = 'application-main'
    searchBarByXPath = "//body//header//input[@type='text']"
    advanceSearchByXpath = "//div[@class='application-main ']//a[text()='Advanced search']"

    #mainPageBody = driver.find_element (mainPageBodyBy)



    def advanceSearchGitHub(self,data):
        advSearcchBarLink = self.driver.find_element_by_xpath(self.advanceSearchByXpath)
        advSearcchBarLink.click()
