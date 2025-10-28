
from playwright.sync_api import Page
from pages.cookie_page.ing_cookie_page_selectors import button_customize ,switch_analytics_cookies, button_accept_selected


class IngCookiePage:
   
   def __init__(self, page: Page):
        self.page = page
#pozmieniac nazwy funkcji na jakies logiczne
   def open_url(self):
        self.page.goto("https://www.ing.pl") 

   def customize_cookies_button(self):
        button_customize(self.page).click() # poprzenosic selectory do ing_cookie_page_selectors

   def switch_toggle_analytics_cookies(self):
        switch_analytics_cookies(self.page).click() # poprzenosic selectory do ing_cookie_page_selectors

   def accept_selected(self):
        button_accept_selected(self.page).click() # poprzenosic selectory do ing_cookie_page_selectors

   def get_all_cookies(self, context):
        return context.cookies()
   
   def get_cookie_by_name(self,cookies, name):
    return next((cookie for cookie in cookies if cookie["name"] == name))