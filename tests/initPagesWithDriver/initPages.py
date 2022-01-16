from infra.seleniumInfra import SeleniumInfra
from page.basePage import BasePage
from page.LandingPage import LandingPage
from page.productPage import ProductPage

class InitPagesWithDriver:
    def __init__(self):
        self.seleniumInfra = SeleniumInfra()
        self.bp = BasePage(self.seleniumInfra)
        self.lp = LandingPage(self.seleniumInfra)
        self.pp = ProductPage(self.seleniumInfra)
