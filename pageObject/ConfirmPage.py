from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self,driver):
        self.driver=driver

    countryBox = (By.ID,'country')
    countryIndia = (By.LINK_TEXT,"India")
    checkBox = (By.CSS_SELECTOR,"div[class*='checkbox-primary']")
    submitButton = (By.CSS_SELECTOR,"input[type='submit']")
    successMsg = (By.CLASS_NAME,"alert-success")


    def getCountryBox(self):
        return self.driver.find_element(*ConfirmPage.countryBox)

    def getCountryIndia(self):
        return self.driver.find_element(*ConfirmPage.countryIndia)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def getSubmitButton(self):
        return self.driver.find_element(*ConfirmPage.submitButton)

    def getSuccessMsg(self):
        return self.driver.find_element(*ConfirmPage.successMsg)









