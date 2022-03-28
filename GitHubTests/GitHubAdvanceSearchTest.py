import time
import unittest
from Base.TestBase import TestBase
from GitHubPoms import HomePage
from selenium import webdriver

from GitHubPoms.AdvancedSearchPage import AdvancedSearchPage
from GitHubPoms.HomePage import HomePage
from GitHubPoms.RepoPage import RepoPage
from GitHubPoms.ResultPage import ResultPage
from GitHubPoms.SearchPage import SearchPage


class MyTest(unittest.TestCase):

    def test_GitHubAdvanceSearch(self):
        driver = TestBase.beforetest(self)
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://github.com/")

        homePage = HomePage(driver);
        homePage.searchGitHub("react")
        searchPage = SearchPage(driver)
        searchPage.advanceSearchGitHub("test")

        testData = {
            'Language': 'JavaScript',
            'State': 'closed',
            'Stars': '>45',
            'Followers': '>50',
            'license': 'bsl-1.0'
        }
        advancedSearchPage = AdvancedSearchPage(driver)
        advancedSearchPage.performAdvancedSearch(testData)

        resultPage = ResultPage(driver)
        self.assertIn("1",resultPage.verifySearchResult())
        self.assertEqual("mvoloskov/decider",resultPage.verifyRepoName())
        resultPage.navigateToRepo()

        repoPage = RepoPage(driver)
        repoPage.getReadMeData()

        time.sleep(3)
        driver.close()

if __name__=="__main__":
    unittest.main()