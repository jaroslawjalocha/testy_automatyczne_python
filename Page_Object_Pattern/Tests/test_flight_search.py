import time

import pytest
from Page_Object_Pattern.Pages.search_flight import SearchFlightPage
from Page_Object_Pattern.Pages.search_results_flight import SearchResultsFlightPage


@pytest.mark.usefixtures("setup")
class TestFlightSearch():


    def test_flight_search(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_flight_page = SearchFlightPage(self.driver)
        search_flight_page.set_city("Warsaw","Dubai")
        search_flight_page.set_date("2021-10-26")
        search_flight_page.set_passenger("5")
        search_flight_page.perform_search()
        results_page = SearchResultsFlightPage(self.driver)
        flight_number = results_page.get_flight_number()
        price_values = results_page.get_flight_prices()

        assert flight_number[0] == '675'
        assert flight_number[1] == '887'
        assert flight_number[2] == '859'
        assert flight_number[3] == '578'

        assert price_values[0] == '882$'
        assert price_values[1] == '$50'
        assert price_values[2] == '$80'
        assert price_values[3] == '$150'