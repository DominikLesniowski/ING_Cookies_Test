from playwright.sync_api import Page


class IngCookiePage:
   
   def __init__(self, page: Page):
        self.page = page

   def open(self):
        self.page.goto("https://www.ing.pl") 

   def customize_cookies(self):
        self.page.get_by_role("button", name="Dostosuj").click()

   def toggle_analytics_cookies(self):
        self.page.get_by_role("switch", name="Cookies analityczne").locator("span").nth(1).click()

   def accept_selected(self):
        self.page.get_by_role("button", name="Zaakceptuj zaznaczone").click()

   def get_all_cookies(self, context):
        return context.cookies()
   
   def get_cookie_by_name(self,cookies, name):
    return next((cookie for cookie in cookies if cookie["name"] == name), None)