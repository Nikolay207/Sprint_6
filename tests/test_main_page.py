import allure
import pytest


from urls import Urls
from data import answers_data

@allure.title('Тесты на проверку вопросов')
class TestMainPage:



    @pytest.mark.parametrize('num',[0,1,2,3,4,5,6,7])
    def test_question(self, num,main_page):
        main_page.go_to_url(Urls.HOME_URL)
        main_page.close_cookie_banner()
        assert main_page.check_answer(num, answers_data[num])