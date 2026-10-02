import allure
import time
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
class OrderPage(BasePage):


    @allure.step('Нажимаем кнопку заказать в шапке страницы')
    def click_to_order(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Нажимаем кнопку Посмотреть статус')
    def click_to_status(self):
        time.sleep(1) #куратор сказал что с time.sleep задание не примут, но без него заказ не успевает распарсится и падает в 8/10 запусков, привязываение к появлению номера заказа не помогло, тест по прежнему падает в  80%, только с time 0.5 или 1 сек всё стабильно работает
        self.click_to_element(OrderPageLocators.STATUS_BUTTON)

    @allure.step('Проверяем что открылась форма заполнения персональных данных для заказа')
    def check_order_header(self):
        header = self.find_element_with_wait(OrderPageLocators.ORDER_HEADER)
        return header.text

    @allure.step('Проверяем что открылась форма заполнения данных для аренды')
    def check_rent_header(self):
        header = self.find_element_with_wait(OrderPageLocators.RENT_HEADER)
        return header.text

    @allure.step('Проверяем что открылся экран со статусом оформленного заказа')
    def check_cancel_button(self):
        header = self.find_element_with_wait(OrderPageLocators.CANSEL_ORDER)
        return header.text

    @allure.step('Проверяем что открылся поп-ап Заказ оформлен')
    def check_order_success(self):
        header = self.find_element_with_wait(OrderPageLocators.ORDER_SUCCESS)
        return header.text

    @allure.step('Вводим персональные данные для заказа')
    def fill_form(self, data):
        self.add_text_to_element(OrderPageLocators.FIRST_NAME, data['first_name'])
        self.add_text_to_element(OrderPageLocators.SECOND_NAME, data['second_name'])
        self.add_text_to_element(OrderPageLocators.ADDRESS, data['address'])
        self.add_text_to_element(OrderPageLocators.PHONE, data['phone'])

    @allure.step('Выбираем станцию метро')
    def select_metro_station(self, station): # индекс станции [0], [3] и т.д.
        self.click_to_element(OrderPageLocators.METRO)
        option = self.format_locators(OrderPageLocators.METRO_OPTION, station)
        self.click_to_element(option)

    @allure.step('Нажимаем кнопку Далее в форме оформления заказа')
    def confirm_to_order(self):
        self.click_to_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step('Нажимаем кнопку Да в итоговом поп-апе оформления заказа')
    def final_confirm_to_order(self):
        self.click_to_element(OrderPageLocators.FINAL_CONFIRM_BUTTON)

    @allure.step('Выбираем дату доставки')
    def select_date_delivery(self, date): # в формате хх, 21, 01, 11...
        self.click_to_element(OrderPageLocators.DATE_FIELD)
        option = self.format_locators(OrderPageLocators.DATE_OPTION, date)
        self.click_to_element(option)

    @allure.step('Выбираем срок аренды')
    def select_date_rental(self):
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_to_element(OrderPageLocators.DAY_RENTAL)

    @allure.step('Выбираем цвет')
    def select_color(self, color): # 'grey' или 'black'
        option = self.format_locators(OrderPageLocators.COLOR, color)
        self.click_to_element(option)

    @allure.step('Заполняем комментарий "{comment}"')
    def fill_comment(self,comment):
        self.add_text_to_element(OrderPageLocators.COMMENT,comment)

