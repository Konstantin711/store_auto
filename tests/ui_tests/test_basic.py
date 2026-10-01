import time
from playwright.sync_api import Page

from pages.main_page import MainPage


def test_get_main_page(page):
    main_page = MainPage(page)
    main_page.open(url="http://localhost:3000/")
    time.sleep(100)
