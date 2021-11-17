from selenium.webdriver.common.keys import Keys

class SearchTouristPage:
    def __init__(self,driver):
        self.driver = driver
        self.search_tourist_xpath = "//*[@id='body-section']/section/div[2]/div/div/div[2]/ul/li[3]/a"
        self.input_city_xpath = "//*[@id='s2id_autogen10']/a/span[1]"
        self.input_city_xpath2 = "//*[@id='select2-drop']/div/input"
        self.input_city_xpath3 = "//*[@id='select2-drop']/ul/li/ul/li/div"
        self.search_flight_from_xpath3 = "//*[@id='select2-drop']/ul/li[1]/div"
        self.search_flight_to_xpath = "//*[@id='s2id_location_to']/a/span[1]"
        self.search_flight_to_xpath2 = "//*[@id='select2-drop']/div/input"
        self.search_flight_to_xpath3 = "//*[@id='select2-drop']/ul/li[2]/div"
        self.location_match_xpath = "//*[@id='tchkin']/div/input"
        self.check_in_input_passenger = "//*[@id='adults']"
        self.type_of_trip_xpath = "//*[@id='s2id_tourtype']/a"
        self.type_of_trip_xpath2 = "//*[@id='select2-drop']/div/input"
        self.type_of_trip_xpath3 = "//*[@id='select2-drop']/ul/li/div"
        self.search_button_xpath = "//*[@id='tours']/form/div[5]/button"
    def set_city(self,city):
        self.driver.find_element_by_xpath(self.search_tourist_xpath).click()
        self.driver.find_element_by_xpath(self.input_city_xpath).click()
        self.driver.find_element_by_xpath(self.input_city_xpath2).send_keys(city)
        self.driver.find_element_by_xpath(self.input_city_xpath3).click()

    def set_date(self, check_in):
        self.driver.find_element_by_xpath(self.location_match_xpath).clear()
        self.driver.find_element_by_xpath(self.location_match_xpath).send_keys(check_in)
    def set_passenger(self,passenger):
        self.driver.find_element_by_xpath(self.check_in_input_passenger).send_keys(passenger)
    def set_type_of_trip(self, type):
        self.driver.find_element_by_xpath(self.type_of_trip_xpath).click()
        self.driver.find_element_by_xpath(self.type_of_trip_xpath2).send_keys(type)
        self.driver.find_element_by_xpath(self.type_of_trip_xpath3).click()
    def perform_search(self):
        self.driver.find_element_by_xpath(self.search_button_xpath).click()