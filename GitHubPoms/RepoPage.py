from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import select

from  GitHubPoms import PomBase
from selenium import webdriver
import unittest

class RepoPage():


    def __init__(self, driverParam):
        self.driver= driverParam


    mainPageBodyByClassName = 'body'
    readMeById = 'readme'

    def getReadMeData(self):
        readMeData = self.driver.find_element_by_id(self.readMeById)
        print(readMeData.text[0:300])

