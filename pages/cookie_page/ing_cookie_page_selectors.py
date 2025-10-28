def button_customize(page):
    return page.get_by_role("button", name="Dostosuj")

def switch_analytics_cookies(page):
    return page.get_by_role("switch", name="Cookies analityczne")

def button_accept_selected(page):
    return page.get_by_role("button", name="Zaakceptuj zaznaczone")