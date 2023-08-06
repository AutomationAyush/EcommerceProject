import pytest
from pageObject.HomePage import HomePage
from testData.HomePageData import HomepageData

from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_homePage(self,setup,getData):

        homePage = HomePage(self.driver)
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.getPassword().send_keys('Password')
        homePage.getCheckbox().click()
        self.dropdownSelectionByText(homePage.getGender(),getData["gender"])
        homePage.getEmpStatus().click()
        homePage.getSubmit().click()
        alertText = homePage.getSuccessMsg().text

        assert("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomepageData.test_Home_PageData)
    def getData(self,request):
        return request.param