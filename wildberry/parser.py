
from playwright.sync_api import sync_playwright 


class Product:
    def __init__(self):
        self.card = None
        self.article = None
        self.url = None
    
    def set_url(self):
        self.url = f"https://www.wildberries.ru/catalog/{self.article}/detail.aspx"

product_obj = Product()


def handle_response(response): 
    if ("card.json" in response.url): 
        product_obj.card = (response.json())


def playwright() -> None:
    with sync_playwright() as playwright:
        chromium = playwright.chromium
        browser = chromium.launch()
        page = browser.new_page()
        page.on("response", handle_response) 
        page.goto(product_obj.url)
        browser.close()


def card_reciever(article):
    product_obj.article = article
    product_obj.set_url()
    playwright()
    return (product_obj.card)


