from fastapi.responses import RedirectResponse
from utils import Browser
import time

async def get_favicon():
    return RedirectResponse(url="/static/favicon.ico")

async def get_root():
    return {"message": "Hello Tes"}

async def get_test():
    driver = Browser("chrome")
    driver.open_page("https://google.com")
    time.sleep(5)
    driver.close_browser()
    return {"status": "OK"}