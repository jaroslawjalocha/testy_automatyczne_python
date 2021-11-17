import time

from selenium.webdriver.common.keys import Keys

class SearchCarsPage:
    def __init__(self,driver):
        self.driver = driver
        self.search_cars_xpath = "//*[@id='body-section']/section/div[2]/div/div/div[2]/ul/li[4]/a"
        self.search_cars_pick_up_xpath = "//*[@id='s2id_carlocations']/a/span[1]"
        self.search_cars_pick_up_drop_off_xpath2 = "//*[@id='select2-drop']/div/input"
        self.search_cars_pick_up_drop_off_xpath3 = "//*[@id='select2-drop']/ul/li[1]/div"
        self.search_cars_drop_off_to_xpath = "//*[@id='s2id_carlocations2']/a/span[1]"
        self.pick_up_date_xpath = "#departcar"
        self.drop_off_date_xpath = "/html/body/div[5]/section/div[2]/div/div/div[2]/div/div[3]/form/div[5]/div/input"
        self.search_button_xpath = "//*[@id='cars']/form/div[7]/button"
    def set_city_to_rent(self,pick_up):
        self.driver.find_element_by_xpath(self.search_cars_xpath).click()
        self.driver.find_element_by_xpath(self.search_cars_pick_up_xpath).click()
        self.driver.find_element_by_xpath(self.search_cars_pick_up_drop_off_xpath2).send_keys(pick_up)
        self.driver.find_element_by_xpath(self.search_cars_pick_up_drop_off_xpath3).click()

    def set_date(self, check_in,check_out):
        self.driver.find_element_by_css_selector(self.pick_up_date_xpath).clear()
        self.driver.find_element_by_css_selector(self.pick_up_date_xpath).send_keys(check_in)
        self.driver.find_element_by_css_selector(self.pick_up_date_xpath).clear()
        self.driver.find_element_by_css_selector(self.pick_up_date_xpath).send_keys(check_out)


    def perform_search(self):
        self.driver.find_element_by_xpath(self.search_button_xpath).click()