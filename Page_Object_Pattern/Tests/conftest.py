import allure
import pytest
from selenium import webdriver
import allure
from webdriver_manager.chrome import ChromeDriverManager



@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield
    driver.quit()
