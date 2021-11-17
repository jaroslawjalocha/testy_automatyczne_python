import time

import pytest
from Pages.login import LoginToPage



@pytest.mark.usefixtures("setup")
class TestLogin():


    def test_login_to_page(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        login_to_page = LoginToPage(self.driver)
        login_to_page.click_to_login()
        login_to_page.send_date_to_login("jan.kowalski1234@wp.pl", "Pol@nie2")
        time.sleep(5)
