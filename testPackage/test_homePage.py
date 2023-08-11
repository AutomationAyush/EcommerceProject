import pytest
from pageObject.HomePage import HomePage
from testData.HomePageData import HomepageData

from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_homePage(self,setup,getData):
        log=self.getLogger()

        homePage = HomePage(self.driver)
        log.info("first name is"+getData["firstname"])
        homePage.getName().send_keys(getData["firstname"])
        log.info("Email is" + getData["email"])
        homePage.getEmail().send_keys(getData["email"])
        log.info("entering password")
        homePage.getPassword().send_keys('Password')
        homePage.getCheckbox().click()
        log.info("sending geNder OF EMPLOYEE information as "+getData["gender"])
        self.dropdownSelectionByText(homePage.getGender(),getData["gender"])
        log.info("selecting employment staus")
        homePage.getEmpStatus().click()
        homePage.getSubmit().click()
        alertText = homePage.getSuccessMsg().text
        log.info("final message after the form submission is"+alertText)

        assert("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomepageData.test_Home_PageData)
    def getData(self,request):
        return request.param