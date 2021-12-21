import time

import pytest
from Pages.search_flight import SearchFlightPage
from Pages.search_results_flight import SearchResultsFlightPage


@pytest.mark.usefixtures("setup")
class TestFlightSearch():


    def test_flight_search(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_flight_page = SearchFlightPage(self.driver)
        search_flight_page.set_city("Warsaw","Dubai")
        search_flight_page.set_date("2021-10-26")
        search_flight_page.set_passenger("6")
        search_flight_page.perform_search()
        results_page = SearchResultsFlightPage(self.driver)
        flight_number = results_page.get_flight_number()
        price_values = results_page.get_flight_prices()
