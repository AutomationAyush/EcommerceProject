from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self,driver):
        self.driver=driver

    shop = (By.CSS_SELECTOR,"a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.CSS_SELECTOR,"input[type='password']")
    checkbox = (By.ID,"exampleCheck1")
    gender = (By.CSS_SELECTOR,"select[class*='form-control']")
    empStatus = (By.ID,"inlineRadio2")
    submit = (By.XPATH, "//input[@value='Submit']")
    successMsg = (By.CSS_SELECTOR, "[class*='alert-success']")


    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getEmpStatus(self):
        return self.driver.find_element(*HomePage.empStatus)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMsg(self):
        return self.driver.find_element(*HomePage.successMsg)
