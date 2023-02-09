from selenium.webdriver.common.by import By

class DropDown:
    LIST_DROPDOWN = (By.ID,"dropdown")
    OPTION1_LIST = (By.CSS_SELECTOR,"#dropdown > option:nth-child(2)")
    OPTION2_LIST = (By.CSS_SELECTOR,"#dropdown > option:nth-child(3)")
    TEXT_LIST = (By.CSS_SELECTOR,"#content > div")
    URL = "https://the-internet.herokuapp.com/dropdown"

    def __init__(self,browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def list_down(self):
        self.browser.find_element(*self.LIST_DROPDOWN).click()

    def option_1(self):
        self.browser.find_element(*self.OPTION1_LIST).click()

    def option_2(self):
        self.browser.find_element(*self.OPTION2_LIST).click()

    def getText(self):
        return self.browser.find_element(*self.TEXT_LIST).text
