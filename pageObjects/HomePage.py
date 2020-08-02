from selenium.webdriver.common.by import By

from pageObjects.CheckOutPage import CheckOutPage


class HomePage:
     def __init__(self, driver):
      self.driver = driver


     shop = (By.LINK_TEXT , "Shop")
     name = (By.CSS_SELECTOR, "input[name='name']")
     email = (By.NAME, "email")
     password = (By.ID, "exampleInputPassword1")
     checkbox = (By.ID,"exampleCheck1")
     gender = (By.ID,"exampleFormControlSelect1")
     submit = (By.XPATH,"//input[@type='submit']")
     alert = (By.CLASS_NAME,"alert-success")


     def shopItems(self):
      self.driver.find_element(*HomePage.shop).click()
      checkOutPage = CheckOutPage(self.driver)
      return checkOutPage

     def getName(self):
        return self.driver.find_element(*HomePage.name)

     def getEmail(self):
            return self.driver.find_element(*HomePage.email)

     def getPassword(self):
            return self.driver.find_element(*HomePage.password)

     def getCheckBox(self):
            return self.driver.find_element(*HomePage.checkbox)

     def getGender(self):
            return self.driver.find_element(*HomePage.gender)

     def getSubmitForm(self):
         return self.driver.find_element(*HomePage.submit)

     def getAlertText(self):
         return self.driver.find_element(*HomePage.alert)

        #self.driver.find_element_by_link_text("Shop").clic)

