from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    card = (By.XPATH , "//div[@class='card h-100']")
    cardFooter = (By.CSS_SELECTOR , "a[class*='btn']")
    checkOutButton = (By.CSS_SELECTOR , "button[class*='btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.card)

    def getCardFooter(self):
        return self.driver.find_element(*CheckOutPage.cardFooter)

    def getCheckoutButton(self):
        self.driver.find_element(*CheckOutPage.checkOutButton).click()
        confirmPage = ConfirmPage()
        return confirmPage



#self.driver.find_elements_by_xpath("//div[@class='card h-100']")
#driver.find_element_by_css_selector("button[class*='btn-success']")


