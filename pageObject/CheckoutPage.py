from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self,driver):
        self.driver=driver

    cardTitle = (By.XPATH,"//div[@class = 'card h-100']")
    cardLable = (By.XPATH,"//div[@class = 'card h-100']/div/h4/a")
    cardFooterButton = (By.CSS_SELECTOR,"button[class*='btn-info']")
    checkOutButtonPrimary = (By.CSS_SELECTOR,"a[class*='btn-primary']")
    checkOutButtonSuccess = (By.CSS_SELECTOR,"button[class*='btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardLables(self):
        return self.driver.find_elements(*CheckoutPage.cardLable)

    def getCardFooterButton(self):
        return self.driver.find_elements(*CheckoutPage.cardFooterButton)

    def getcCheckOutButtonPrimary(self):
        return self.driver.find_element(*CheckoutPage.checkOutButtonPrimary)

    def getcCheckOutButtonSuccess(self):
        return self.driver.find_element(*CheckoutPage.checkOutButtonSuccess)


