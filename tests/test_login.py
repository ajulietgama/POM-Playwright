from playwright.sync_api import Page

from pages.login_page import Login
from pages.dashboard_page import Dashboard   


def test_example(page: Page) -> None:
    login_page = Login(page)
    dashboard_page = Dashboard(page)

    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login_page.enter_username("Admin")
    login_page.enter_password("admin123")   
    login_page.click_login()

    dashboard_page.time_at_work_visible()
    dashboard_page.click_performance_link()         
    dashboard_page.employee_reviews_visible()

