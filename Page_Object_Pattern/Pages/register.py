from selenium.webdriver.common.keys import Keys
class RegisterToPage:
    def __init__(self,driver):
        self.driver = driver
        self.click_to_my_account_xpath = "/html/body/nav/div/div[2]/ul[2]/ul/li[1]/a"
        self.click_to_register_xpath = "/html/body/nav/div/div[2]/ul[2]/ul/li[1]/ul/li[2]/a"
        self.input_to_register_firstname = "firstname"
        self.input_lastname_name = "lastname"
        self.input_phone_name = "phone"
        self.input_email_name = "email"
        self.input_password_name = "password"
        self.confirm_password_name ="confirmpassword"
        self.confirm_register_xpath = "//*[@id='headersignupform']/div[9]/button"

    def click_to_register(self):
        self.driver.find_element_by_xpath(self.click_to_my_account_xpath).click()
        self.driver.find_element_by_xpath(self.click_to_register_xpath).click()
    def send_date_to_register(self,firstname, lastname, phone, email, password, confpassword):
        self.driver.find_element_by_name(self.input_to_register_firstname).send_keys(firstname)
        self.driver.find_element_by_name(self.input_lastname_name).send_keys(lastname)
        self.driver.find_element_by_name(self.input_phone_name).send_keys(phone)
        self.driver.find_element_by_name(self.input_email_name).send_keys(email)
        self.driver.find_element_by_name(self.input_password_name).send_keys(password)
        self.driver.find_element_by_name(self.confirm_password_name).send_keys(confpassword)
        self.driver.find_element_by_xpath(self.confirm_register_xpath).click()

