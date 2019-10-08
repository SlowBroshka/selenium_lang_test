import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os


class TestMain:

    DRIVER = str()

    if os.name == 'posix':
        DRIVER = 'Drivers/chromedriver'
    else:
        DRIVER = 'Drivers\\chromedriver.exe'

    test_link = "http://selenium1py.pythonanywhere.com/{}/catalogue/coders-at-work_207"

    def setup_method(self):
        self.browser = webdriver.Chrome()    # self.browser = webdriver.Chrome(TestMain.DRIVER)

    def teardown_method(self):
        self.browser.quit()

    def test_add_to_basket(self, lang):
        page = TestMain.test_link.format(lang)
        self.browser.get(page)
        wait = WebDriverWait(self.browser, 5)
        try:
            element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-add-to-basket')))
            print("Find button with text: \"{}\"".format(element.text))
        except TimeoutException as te:
            assert False, 'Element not found on page: \"{}\" with lang: \"{}\"'.format(page, lang)
        assert True
