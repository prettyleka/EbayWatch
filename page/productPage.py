from infra.seleniumInfra import SeleniumInfra
from page.productPageLocators import ProductPageLocators

class ProductPage:
    def __init__(self, seleniumInfra:SeleniumInfra):
        self.seleniumInfra = seleniumInfra
        self.locators = ProductPageLocators()

    def findAllPrices(self):
        prices=self.seleniumInfra.findElementListBy(*self.locators.allProductsPrices)
        p=[]
        for x in prices:
            nums = x.text
            if' to ' in nums:
                z=nums.split(' to ')
                p.append(float(z[0].split('ILS ')[1]))
                p.append(float(z[1].split('ILS ')[1]))
            else:
                p.append(float(z[0].split('ILS ')[1]))
        p.sort()
        return p

