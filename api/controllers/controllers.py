from fastapi.responses import RedirectResponse
from utils import Browser
from selenium.webdriver.chrome.options import Options

import time

class Controller:
    async def get_favicon(self):
        return RedirectResponse(url="/static/favicon.ico")

    async def get_root(self):
        return {"message": "Hello Tes"}

    async def get_test(self):
        options = Options()
        options.add_argument("--headless")
        driver = Browser("chrome", opt=options)
        driver.open_page("https://google.com")
        time.sleep(5)
        driver.close_browser()
        return {"status": "OK"}