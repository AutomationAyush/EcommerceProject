import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    #options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")

    browser_name=request.config.getoption("browser_name")
    if browser_name=="chrome":
        driver = webdriver.Chrome(executable_path="C:/Users/ayush.jain/chromedriver-win64.exe",options=options)
    elif browser_name=="firefox":
        driver = webdriver.Firefox(executable_path="C:/Users/ayush.jain/geckodriver.exe",options=options)
    elif browser_name=="IE not":
        driver = webdriver.Edge(executable_path="C:/Users/ayush.jain/msedgedriver.exe",options=options)

    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    request.cls.driver = driver
    yield
    driver.close()




