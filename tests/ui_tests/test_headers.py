import time

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

@pytest.mark.test_id(id="HDR-UP-004")
def test_phone_number_display(main_page):
    """
    title: Clickable phone number
    """

    main_page.open(url="http://localhost:3000/")

    phone_number = main_page.upper_header.contact_phone_number
    expect(phone_number).to_be_visible()
    expect(phone_number).to_have_attribute("href", "tel:+380000000000")

@pytest.mark.test_id(id="HDR-UP-005")
def test_email_display(main_page):
    """
    title: Email display
    """

    main_page.open(url="http://localhost:3000/")

    email = main_page.upper_header.contact_email
    expect(email).to_be_visible()
    expect(email).to_have_text("shirts-store@gmail.com")

@pytest.mark.test_id(id="HDR-UP-006")
def test_clickable_email(main_page):
    """
    title: Clickable email
    """

    main_page.open(url="http://localhost:3000/")

    email = main_page.upper_header.contact_email
    expect(email).to_be_visible()
    expect(email).to_have_attribute("href", "mailto:shirts-store@gmail.com")

@pytest.mark.test_id(id="HDR-UP-007")
def test_instagram_link(main_page):
    """
    title: Instagram link
    """

    main_page.open(url="http://localhost:3000/")
    instagram = main_page.upper_header.insta_link
    expect(instagram).to_be_visible()
    expect(instagram).to_have_attribute("href", "https://www.instagram.com")

    with instagram.page.expect_popup() as popup_info:
        instagram.click()

    second_page = popup_info.value
    expect(second_page).to_have_url("https://www.instagram.com/")


@pytest.mark.test_id(id="HDR-UP-008")
def test_tiktok_link(main_page):
    """
    title: TikTok link
    """

    main_page.open(url="http://localhost:3000/")

    tiktok = main_page.upper_header.tik_tok_link
    expect(tiktok).to_be_visible()
    expect(tiktok).to_have_attribute("href", "https://www.tiktok.com")

    with tiktok.page.expect_popup() as popup_info:
        tiktok.click()

    second_page = popup_info.value
    expect(second_page).to_have_url("https://www.tiktok.com/")


@pytest.mark.test_id(id="HDR-UP-009")
def test_login_link(main_page):
    """
    title: Account icon for guest
    """

    main_page.open(url="http://localhost:3000/")

    login = main_page.upper_header.login_register_link
    expect(login).to_be_visible()
    expect(login).to_have_attribute("href", "/login")

    login.click()
    main_page.check_url("http://localhost:3000/login")


@pytest.mark.test_id(id="HDR-UP-010")
def test_login_link(main_page, login_register_page, settings):
    """
    title: Account icon for authenticated user
    """

    main_page.open(url=settings.url("/login"))
    login_register_page.make_login(
        settings.admin_email,
        settings.admin_password
    )
    main_page.check_url(settings.url("/"))

    main_page.upper_header.logged_user_menu.click()
    expect(main_page.upper_header.menu_cabinet_link).to_be_visible()
    main_page.upper_header.menu_cabinet_link.click()
    main_page.check_url(settings.url("/cabinet"))


@pytest.mark.test_id(id="HDR-UP-011")
def test_login_link(main_page, login_register_page, settings):
    """
    title: Check link to the favorite via login menu
    """

    main_page.open(url=settings.url("/login"))
    login_register_page.make_login(
        settings.admin_email,
        settings.admin_password
    )
    main_page.check_url(settings.url("/"))

    main_page.upper_header.logged_user_menu.click()
    expect(main_page.upper_header.menu_favorite_link).to_be_visible()
    main_page.upper_header.menu_favorite_link.click()
    main_page.check_url(settings.url("/favorites"))

