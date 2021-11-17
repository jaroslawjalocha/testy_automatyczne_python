import time

import pytest
from Pages.search_tourist import SearchTouristPage



@pytest.mark.usefixtures("setup")
class TestFlightSearch():


    def test_flight_search(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_tourist_page = SearchTouristPage(self.driver)
        search_tourist_page.set_city("Thail")
        search_tourist_page.set_date("26/10/2021")
        search_tourist_page.set_passenger("4")
        search_tourist_page.set_type_of_trip("Private")
        search_tourist_page.perform_search()
        time.sleep(1000)
