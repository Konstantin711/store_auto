import pytest
from playwright.sync_api import expect


@pytest.mark.test_id(id="HDR-UP-001")
def test_about_us_link_disp(main_page, upper_header):
    """
    title: About Us link display
    """

    main_page.open(url="http://localhost:3000/")

    about_us_link = upper_header.about_us_page_link
    expect(about_us_link).to_be_visible()
    expect(about_us_link).to_have_attribute("href", "/about_us")

    about_us_link.click()
    main_page.check_url("http://localhost:3000/about_us")

