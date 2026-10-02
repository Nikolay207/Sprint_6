import allure
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Скролим вниз страницы и кликаем на вопрос')
    def click_question(self,num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION,num)
        self.scroll_to_element(MainPageLocators.LOCATOR_TO_SCROLL)
        self.click_to_element(locator_q_formatted)

    @allure.step('Получаем ответ на вопрос')
    def get_answer_text(self,num):
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER, num)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Проверяем ответы на вопросы')
    def check_answer(self,num,my_text):
        self.click_question(num)
        text = self.get_answer_text(num)
        return text == my_text

    @allure.step('Нажимаем кнопку согласия на принятие использования кук')
    def close_cookie_banner(self):
        self.click_to_element(MainPageLocators.COOKIE_BANNER_BUTTON)

    @allure.step('Скролим вниз страницы и кликаем на кнопку Заказать')
    def click_create_order(self):
        self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_CREATE)
        self.click_to_element(MainPageLocators.BOTTOM_ORDER_CREATE)
