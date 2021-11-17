from selenium.webdriver.common.keys import Keys

class SearchFlightPage:
    def __init__(self,driver):
        self.driver = driver
        self.search_flight_xpath = "//*[@id='body-section']/section/div[2]/div/div/div[2]/ul/li[2]/a"
        self.search_flight_from_xpath = "//*[@id='s2id_location_from']/a/span[1]"
        self.search_flight_from_xpath2 = "//*[@id='select2-drop']/div/input"
        self.search_flight_from_xpath3 = "//*[@id='select2-drop']/ul/li[1]/div"
        self.search_flight_to_xpath = "//*[@id='s2id_location_to']/a/span[1]"
        self.search_flight_to_xpath2 = "//*[@id='select2-drop']/div/input"
        self.search_flight_to_xpath3 = "//*[@id='select2-drop']/ul/li[2]/div"
        self.location_match_xpath = "/html/body/div[5]/section/div[2]/div/div/div[2]/div/div[4]/form/div[3]/div/input"
        self.check_in_input_passenger = "//*[@id='flights']/form/div[5]/div/input"
        self.search_button_xpath = "/html/body/div[5]/section/div[2]/div/div/div[2]/div/div[4]/form/div[6]/button"
    def set_city(self,city_from,city_to):
        self.driver.find_element_by_xpath(self.search_flight_xpath).click()
        self.driver.find_element_by_xpath(self.search_flight_from_xpath).click()
        self.driver.find_element_by_xpath(self.search_flight_from_xpath2).send_keys(city_from)
        self.driver.find_element_by_xpath(self.search_flight_from_xpath3).click()
        self.driver.find_element_by_xpath(self.search_flight_to_xpath).click()
        self.driver.find_element_by_xpath(self.search_flight_to_xpath2).send_keys(city_to)
        self.driver.find_element_by_xpath(self.search_flight_to_xpath3).click()
    def set_date(self, check_in):
        self.driver.find_element_by_xpath(self.location_match_xpath).send_keys(check_in)
    def set_passenger(self,passenger):
        self.driver.find_element_by_xpath(self.check_in_input_passenger).send_keys(passenger)
    def perform_search(self):
        self.driver.find_element_by_xpath(self.search_button_xpath).click()