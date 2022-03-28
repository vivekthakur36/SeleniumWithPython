from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import select

from  GitHubPoms import PomBase
from selenium import webdriver

class AdvancedSearchPage():


    def __init__(self, driverParam):
        self.driver= driverParam
        #super().__init__(driverParam)

    mainPageBodyByClassName = 'body'
    mainPageByClassName = 'application-main'
    writtenLangDDByXpath = "//select[@id['search_language']]"
    manyStarsById = "search_stars"
    inTheSateById = "search_state"
    withFollowersById = "search_followers"
    withLicenseById = "search_license"
    licenseOptionXpath = "//optgroup[@label='Licenses']//option[@value='bsl-1.0']"
    searchBtnByXpath = "//div[@class='form-group flattened']//button"
    #mainPageBody = driver.find_element (mainPageBodyBy)



    def performAdvancedSearch(self,testData):

        ele = self.driver.find_element_by_xpath(self.writtenLangDDByXpath)
        written_lang_dd = select.Select(ele)
        written_lang_dd.select_by_value(testData['Language'])

        manyStarsTb = self.driver.find_element_by_id(self.manyStarsById)
        manyStarsTb.send_keys(testData['Stars'])

        ele = self.driver.find_element_by_id(self.withLicenseById)
        withLicenseDD = select.Select(ele)
        #withLicenseDD.click()
        #ele = withLicenseDD.driver.find_element_by_xpath(self.licenseOptionXpath)
        #ele.click();
        withLicenseDD.select_by_value(testData['license'])

        ele = self.driver.find_element_by_id(self.inTheSateById)
        inTheStateDD = select.Select(ele)
        inTheStateDD.select_by_value(testData['State'])

        witFollowersTB = self.driver.find_element_by_id(self.withFollowersById)
        witFollowersTB.send_keys(testData['Followers'])

        searchBtn = self.driver.find_element_by_xpath(self.searchBtnByXpath)
        searchBtn.click();