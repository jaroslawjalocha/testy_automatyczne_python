import time

import pytest
from Pages.register import RegisterToPage



@pytest.mark.usefixtures("setup")
class TestLogin():


    def test_register_to_page(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        register_to_page = RegisterToPage(self.driver)
        register_to_page.click_to_register()
        register_to_page.send_date_to_register("MAriusz","Rosek","555555555","su-35@wp.pl","Pol@nie2","Pol@nie2")
        time.sleep(5)
