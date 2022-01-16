from infra.seleniumInfra import SeleniumInfra
from page.landingPageLocators import LandingPageLocators

class LandingPage:
    def __init__(self, seleniumInfra:SeleniumInfra):
        self.seleniumInfra = seleniumInfra
        self.locators = LandingPageLocators()

    def writeInSearchInput(self, text):
        input = self.seleniumInfra.findElementBy(*self.locators.input)
        input.send_keys(text)

    def clickOnSearchBtn(self):
        self.seleniumInfra.clickButton(*self.locators.searchBtn)

