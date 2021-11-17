from selenium.webdriver.common.keys import Keys
class LoginToPage:
    def __init__(self,driver):
        self.driver = driver
        self.click_to_my_account_xpath = "/html/body/nav/div/div[2]/ul[2]/ul/li[1]/a"
        self.click_to_login_name = "Login"
        self.input_username = "username"
        self.input_password = "password"
        self.confirm_login = "//*[@id='loginfrm']/button"

    def click_to_login(self):
        self.driver.find_element_by_xpath(self.click_to_my_account_xpath).click()
        self.driver.find_element_by_link_text(self.click_to_login_name).click()
    def send_date_to_login(self,username,password):
        self.driver.find_element_by_name(self.input_username).click()
        self.driver.find_element_by_name(self.input_username).send_keys(username)
        self.driver.find_element_by_name(self.input_password).click()
        self.driver.find_element_by_name(self.input_password).send_keys(password)
        self.driver.find_element_by_xpath(self.confirm_login).click()