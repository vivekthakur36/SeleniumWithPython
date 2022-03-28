from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from  GitHubPoms import PomBase
from selenium import webdriver

class HomePage():


    def __init__(self, driverParam):
        self.driver = driverParam
        #super().__init__(driverParam)

    mainPageBodyBy = 'body'
    mainPageBy = 'application-main'
    searchBarBy = "//body//header//input[@type='text']"


    #mainPageBody = driver.find_element (mainPageBodyBy)



    def searchGitHub(self,data):
        searcchBarTb = self.driver.find_element_by_xpath(self.searchBarBy)
        searcchBarTb.send_keys(data)
        searcchBarTb.send_keys(Keys.ENTER)