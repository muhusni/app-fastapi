from seleniumwire import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Browser:
    browser = None

    def __init__(self, driver: str = "chrome", opt=None):
        if driver.lower() == "chrome":
            self.browser = webdriver.Chrome(seleniumwire_options=opt)
        else:
            self.browser = webdriver.Firefox(options=opt)

    def open_page(self, url: str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()

    # def click_button(self, by: By, value: str):
    #     button = self.browser.find_element(by=by, value=value)
    #     button.click()
    #     time.sleep(1)

    def click_button(self, by: By, value: str, clickable=True):
        button = self.wait_for_element(by, value, 20, clickable)
        button.click()

    def input_key(self, by: By, key: str, value: str):
        input_field = self.wait_for_element(by, key)
        input_field.send_keys(value)

    def find_element(self, by: By, value: str):
        return self.browser.find_element(by, value)

    def wait_for_element(self, by: By, value: str, timeout: int = 30, click=False):
        if click:
            return WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
        else:
            return WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((by, value))
            )

    def wait_for_element_invisible(self, by: By, value: str, timeout: int = 30):
        WebDriverWait(self.browser, 10).until(
            EC.invisibility_of_element_located((by, value))
        )