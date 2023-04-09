from selene import browser, be, have, command
from time import sleep
import allure



class VideoRecorders:
    @allure.step('Go to the DVRs tab')
    def go_to_the_subsection(self):
        browser.element('a[href="/products/"]').click()
        browser.element('.name>a[href="/products/videoregistratory-dlya-videonablyudeniya/"]').click()
        # browser.all('.left_block li').element_by(have.text('Видеорегистраторы')).click()

    @allure.step('Open the filter window')
    def submit_filter(self):
        browser.element(".adaptive_filter>.filter_opener").click()

    @allure.step('We set the maximum and minimum price')
    def enter_the_price(self, min_, max_):
        browser.element('#arrFilter_P1_MIN').set_value(min_)
        browser.element('#arrFilter_P1_MAX').set_value(max_)

    @allure.step('Choosing a brand')
    def choose_a_brand(self):
        browser.element('[for="arrFilter_3173_2307495926"]').click()

    @allure.step('Forming a list of options')
    def show_options_for_the_selected_parameters(self):
        browser.element('#set_filter').perform(command.js.scroll_into_view)
        browser.element('#set_filter').click()
