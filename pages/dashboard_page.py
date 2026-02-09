from playwright.sync_api import Page, expect

class Dashboard:
    def __init__(self, page):
        self.page = page
        self.time_at_work = page.get_by_text("Time at Work")
        self.performance_link = page.get_by_role("link", name="Performance")
        self.employee_reviews_heading = page.get_by_role("heading", name="Employee Reviews")


    def time_at_work_visible(self):
        expect(self.time_at_work).to_be_visible()
    
    def click_performance_link(self):
        self.performance_link.click()
    
    def employee_reviews_visible(self):
        expect(self.employee_reviews_heading).to_be_visible()