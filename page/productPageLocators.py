from selenium.webdriver.common.by import By


class ProductPageLocators:
    def __init__(self):
        self.allProductsPrices = (By.XPATH, '//div[@class="s-item__detail s-item__detail--primary"]/span[@class="s-item__price"]')
        self.searchBtn = (By.XPATH, "//input[@id='gh-btn']")