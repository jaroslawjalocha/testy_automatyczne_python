class SearchResultsFlightPage:
    def __init__(self, driver):
        self.driver = driver
        self.flight_number_xpath = "//*[@id='load_data']/tbody/tr[1]/td/div[1]/div[1]/div[1]/small"
        self.flight_prices_xpath = "//*[@id='load_data']/tbody/tr[1]/td/div[2]/p/span"

    def get_flight_number(self):
        numbers = self.driver.find_elements_by_xpath(self.flight_number_xpath)
        return [number.get_attribute("textContent") for number in numbers]
    def get_flight_prices(self):
        prices = self.driver.find_elements_by_xpath(self.flight_prices_xpath)
        return [price.get_attribute("textContent") for price in prices]