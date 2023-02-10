

from selenium.webdriver.common.by import By

class wysiwygEditor:
    LINK_EDITOR = (By.CSS_SELECTOR,"#content > ul > li:nth-child(44) > a")
    TEXT_PAGE_EDITOR = (By.CLASS_NAME,"example")
    SELECT_FILE = (By.CSS_SELECTOR,"#content > div > div > div.tox-editor-container > div.tox-editor-header > div.tox-menubar > button:nth-child(1)")
    NEW_DOCUMENT = (By.CLASS_NAME,"tox-collection__item-label")
    #EDITOR_TEXT = (By.CLASS_NAME,"tox-sidebar-wrap")
    EDITOR_TEXT = (By.CLASS_NAME, "tox-edit-area__iframe")
    SELECT_MENU_BOLD = (By.CSS_SELECTOR,"#content > div > div > div.tox-editor-container > div.tox-editor-header > div.tox-toolbar-overlord > div > div:nth-child(3) > button:nth-child(1)")
    SELECT_MENU_ITALIC = (By.CSS_SELECTOR,"#content > div > div > div.tox-editor-container > div.tox-editor-header > div.tox-toolbar-overlord > div > div:nth-child(3) > button:nth-child(2) > span")
    CONFIRM_ITALIC_SELECT = (By.CSS_SELECTOR,"#content > div > div > div.tox-editor-container > div.tox-editor-header > div.tox-toolbar-overlord > div > div:nth-child(2) > button > span")
    TAB_ALINIAMENT = (By.CSS_SELECTOR,"#content > div > div > div.tox-editor-container > div.tox-editor-header > div.tox-toolbar-overlord > div > div:nth-child(4)")
    FORMAT_SELECT = (By.CSS_SELECTOR,"#content > div > div > div.tox-editor-container > div.tox-editor-header > div.tox-menubar > button:nth-child(4)")
    CLEAR_FORMATING = (By.CLASS_NAME,"div>div>tox-menu-nav__js tox-collection__item tox-collection__item--active")

    URL = "https://the-internet.herokuapp.com/"

    def __init__(self,browser):
        self.browser = browser

    def load_Page(self):
        self.browser.get(self.URL)

    def click_link_editor(self):
        self.browser.find_element(*self.LINK_EDITOR).click()

    def get_text_page(self):
        return self.browser.find_element(*self.TEXT_PAGE_EDITOR).text

    def click_select_file(self):
        self.browser.find_element(*self.SELECT_FILE).click()

    def click_new_documnet(self):
        self.browser.find_element(*self.NEW_DOCUMENT).click()

    def text_editor(self,element):
        self.browser.find_element(*self.EDITOR_TEXT).send_keys(element)

    # def get_text_editor(self):
    #     self.browser.find_element(*self.EDITOR_TEXT).is_displayed()

    def click_select_bold(self):
        self.browser.find_element(*self.SELECT_MENU_BOLD).click()

    def click_select_italic(self):
        self.browser.find_element(*self.SELECT_MENU_ITALIC).click()

    def get_confirm_italic(self):
        return self.browser.find_element(*self.CONFIRM_ITALIC_SELECT).text

    def click_format_text(self):
        self.browser.find_element(*self.FORMAT_SELECT).click()

    def click_clear(self):
        self.browser.find_element(*self.CLEAR_FORMATING).click()


