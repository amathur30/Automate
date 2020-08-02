import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()

        # driver.find_element_by_name("name").send_keys("Arpit")

        homepage = HomePage(self.driver)
        log.info("first name is "+ getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getPassword().send_keys("mathur30")
        homepage.getCheckBox().click()

  # select class provides the method to handle the options in dropdown

        self.SelectOptionByText(homepage.getGender() , getData["gender"])

        #dropdown.select_by_index(0)

        homepage.getSubmitForm().click()

        message = homepage.getAlertText().text

        assert "success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("TestCase2"))
    def getData(self,request):
        return request.param

