import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
def button_customize(page):
    return page.get_by_role("button", name="Dostosuj")

def switch_analytics_cookies(page):
    return page.get_by_role("switch", name="Cookies analityczne").locator("span").nth(1)

def button_accept_selected(page):
    return page.get_by_role("button", name="Zaakceptuj zaznaczone")