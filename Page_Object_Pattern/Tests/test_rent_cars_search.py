import pytest
from Pages.search_cars import SearchCarsPage



@pytest.mark.usefixtures("setup")
class TestCarsSearch():


    def test_hotel_search(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_cars_page = SearchCarsPage(self.driver)
        search_cars_page.set_city_to_rent("Manchester")
        search_cars_page.set_date("12/09/2021", "13/09/2021")
        search_cars_page.perform_search()
