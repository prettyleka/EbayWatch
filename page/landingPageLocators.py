from selenium.webdriver.common.by import By


class LandingPageLocators:
    def __init__(self):
        self.input = (By.XPATH, '//input[@id="gh-ac"]')
        self.searchBtn = (By.XPATH, "//input[@id='gh-btn']")