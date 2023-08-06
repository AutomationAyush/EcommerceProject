import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.CheckoutPage import CheckoutPage
from pageObject.ConfirmPage import ConfirmPage
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self,setup):

        homePage = HomePage(self.driver)

        #self.driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
        homePage.shopItems().click()


        checkOutPage = CheckoutPage(self.driver)

        #products = self.driver.find_elements(By.XPATH,"//div[@class = 'card h-100']")
        products = checkOutPage.getCardTitles()

        for product in products:
            #productName = product.find_element(By.XPATH,"div/h4/a").text
            productName = checkOutPage.getCardLables()
            if productName == "Blackberry":
                #product.find_element(By.CSS_SELECTOR,"button[class*='btn-info']").click()
                product.checkOutPage.getCardFooterButton().click()

        checkOutPage.getcCheckOutButtonPrimary().click()
        checkOutPage.getcCheckOutButtonSuccess().click()
        # CHECKOUT PAGE FLOW END


        confirmPage = ConfirmPage(self.driver)

        #self.driver.find_element(By.ID,'country').c
        confirmPage.getCountryBox().send_keys('ind')
        #wait=WebDriverWait(self.driver,10)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
        self.verifyLinkPresence("India")
        #self.driver.find_element(By.LINK_TEXT,"India").click()
        confirmPage.getCountryIndia().click()
        #self.driver.find_element(By.CSS_SELECTOR,"div[class*='checkbox-primary']").click()
        confirmPage.getCheckBox().click()
        #self.driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
        confirmPage.getSubmitButton().click()
        #successText = self.driver.find_element(By.CLASS_NAME,"alert-success").text
        successText = confirmPage.getSuccessMsg().text
        assert "Success! Thank you!" in successText

