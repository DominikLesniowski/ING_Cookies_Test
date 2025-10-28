def button_customize(page):
    return page.get_by_role("button", name="Dostosuj")

def switch_analytics_cookies(page):
    return page.get_by_role("switch", name="Cookies analityczne")

def button_accept_selected(page):
    return page.get_by_role("button", name="Zaakceptuj zaznaczone")

def toggle_analytics_cookies_checked(page):
    return page.locator('div[name="CpmAnalyticalOption"]')

def is_toggle_analytics_checked(page):
 toggle = toggle_analytics_cookies_checked(page)
 aria_checked = toggle.get_attribute("aria-checked")
 return aria_checked == "true"