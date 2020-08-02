from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckOutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)

        checkOutPage = homePage.shopItems()
        log.info("getting all the card titles")


        #checkOutPage = CheckOutPage(self.driver)

        product = checkOutPage.getCardTitles()

        #product = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        for products in product:
            productname = products.find_element_by_xpath("div/h4/a").text
            #productname = products.checkOutPage.getProductName().text
            if productname == "Blackberry":
                products.find_element_by_xpath("div/button").click()
                #pr.checkOutPage.getAddToCart().click()

        #self.driver.find_element_by_css_selector("a[class*='btn']").click()
        checkOutPage.getCardFooter().click()
        #self.driver.find_element_by_css_selector("button[class*='btn-success']").click()
        checkOutPage.getCheckoutButton()
        log.info("entering country name as ind")
        self.driver.find_element_by_css_selector("input[class*='validate']").send_keys("Ind")
        self.verifyLinkPresence("India")
        #wait = WebDriverWait(self.driver, 15)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_css_selector("div[class*='checkbox']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        success = self.driver.find_element_by_class_name("alert-success").text
        log.info("text recived from application"+success)

        assert "Success! Thankasdf you!" in success

        self.driver.get_screenshot_as_file("screen.png")
