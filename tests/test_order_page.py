import allure
from urls import Urls
from data import order_data_1
from data import comment_1
from data import comment_2

@allure.title('Тесты на оформление заказа')
class TestOrderPage:

    def test_header_order_create(self, main_page,order_page):
        main_page.go_to_url(Urls.HOME_URL)
        main_page.close_cookie_banner()
        order_page.click_to_order()
        order_page.fill_form(order_data_1)
        order_page.select_metro_station('3')
        order_page.confirm_to_order()
        order_page.select_date_delivery('17')
        order_page.select_date_rental()
        order_page.select_color('black')
        order_page.fill_comment(comment_1)

        order_page.confirm_to_order()
        order_page.final_confirm_to_order()
        order_page.click_to_status()
        assert order_page.check_cancel_button(), 'экран со статусом заказа не открылся'


    def test_bottom_order_create(self, main_page,order_page):
        main_page.go_to_url(Urls.HOME_URL)
        main_page.close_cookie_banner()
        main_page.click_create_order()
        order_page.fill_form(order_data_1)
        order_page.select_metro_station('2')
        order_page.confirm_to_order()
        order_page.select_date_delivery('05')
        order_page.select_date_rental()
        order_page.select_color('grey')
        order_page.fill_comment(comment_2)
        order_page.confirm_to_order()
        order_page.final_confirm_to_order()
        order_page.click_to_status()
        assert order_page.check_cancel_button(), 'экран со статусом заказа не открылся'