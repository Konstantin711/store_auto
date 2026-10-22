import re
import pytest

from components.main_header import MainHeader
from components.upper_header import UpperHeader
from config.settings import load_settings
from pages.login_registration_page import LoginRegisterPage
from pages.main_page import MainPage


@pytest.fixture(scope="session")
def settings():
    return load_settings()

@pytest.fixture
def main_page(page):
    return MainPage(page)

@pytest.fixture
def main_header(page):
    return MainHeader(page)

@pytest.fixture
def upper_header(page):
    return UpperHeader(page)

@pytest.fixture
def login_register_page(page):
    return LoginRegisterPage(page)