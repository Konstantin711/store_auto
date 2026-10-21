import re
import pytest

from components.main_header import MainHeader
from components.upper_header import UpperHeader
from pages.main_page import MainPage


@pytest.fixture
def main_page(page):
    return MainPage(page)

@pytest.fixture
def main_header(page):
    return MainHeader(page)

@pytest.fixture
def upper_header(page):
    return UpperHeader(page)
