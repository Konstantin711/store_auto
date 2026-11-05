import os

import pandas as pd
import psycopg2
import pytest
from dotenv import load_dotenv

from components.main_header import MainHeader
from components.upper_header import UpperHeader
from config.settings import load_settings
from pages.login_registration_page import LoginRegisterPage
from pages.main_page import MainPage


@pytest.fixture(scope="session")
def get_data_from_db():
    """
    To get data from a database

    """
    load_dotenv()

    connection = psycopg2.connect(
        dbname=os.getenv("DATABASE_NAME"),
        user=os.getenv("DATABASE_USERNAME"),
        password=os.getenv("DATABASE_PASSWORD"),
        host=os.getenv("DATABASE_HOST"),
        port=os.getenv("DATABASE_PORT")
    )

    def _make_request(query: str, params: tuple | None = None, fetch: str = "all") -> pd.DataFrame:
        """

        :param query:
        :param query_type: fetchall or fetchone
        :return:
        """

        with connection.cursor() as cursor:
            cursor.execute(query, params)
            columns = [description[0] for description in cursor.description]

            if fetch == "all":
                rows = cursor.fetchall()
            elif fetch == "one":
                row = cursor.fetchone()
                rows = [row] if row is not None else []
            else:
                raise ValueError("fetch має бути 'all' або 'one'")

            return pd.DataFrame(rows, columns=columns)


    yield _make_request

    connection.close()


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