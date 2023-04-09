import allure

from selene import browser, be, have
from time import sleep


class PriceListPage:
    @allure.step('Open the price list tab')
    def submit_price_list(self):
        browser.element("//a[contains(text(), 'Наш прайс лист')]").double_click()

    @allure.step('Download the price list')
    def download_price_list(self):
        browser.element('a[href="/products/DSSL_price.xlsx?03042023"]').click()
        sleep(30)




