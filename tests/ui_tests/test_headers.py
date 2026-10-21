import pytest
from playwright.sync_api import expect


@pytest.mark.test_id(id="HDR-UP-001")
def test_about_us_link_disp(main_page):
    """
    title: About Us link display
    """

    main_page.open(url="http://localhost:3000/")

    about_us_link = main_page.upper_header.about_us_page_link
    expect(about_us_link).to_be_visible()
    expect(about_us_link).to_have_attribute("href", "/about_us")

    about_us_link.click()
    main_page.check_url("http://localhost:3000/about_us")


@pytest.mark.test_id(id="HDR-UP-002")
def test_delivery_and_pay_link(main_page):
    """
    title: Delivery and Payment link
    """

    main_page.open(url="http://localhost:3000/")

    delivery_and_pay_link = main_page.upper_header.payment_delivery_page_link
    expect(delivery_and_pay_link).to_be_visible()
    expect(delivery_and_pay_link).to_have_attribute("href", "/delivery")

    delivery_and_pay_link.click()
    main_page.check_url("http://localhost:3000/delivery")


@pytest.mark.test_id(id="HDR-UP-003")
def test_phone_number_display(main_page):
    """
    title: Phone number display
    """

    main_page.open(url="http://localhost:3000/")

    phone_number = main_page.upper_header.contact_phone_number
    expect(phone_number).to_be_visible()

    expect(phone_number).to_have_text("+38 (000) 000-00-00")
    expect(phone_number).to_have_attribute("href", "tel:+380000000000")

