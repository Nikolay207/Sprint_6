import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
class BasePage:

    def __init__(self,driver):
        self.driver=driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver,self.timeout)

    @allure.step('Переходим по URL')
    def go_to_url(self,url):
        self.driver.get(url)

    @allure.step('Ждём пока локатор не появится на странице')
    def find_element_with_wait(self,locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ждём пока локатор не станет кликабельный и нажимаем по нему')
    def click_to_element(self,locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    # формируем локаторы для параметризации
    def format_locators (self,locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return method,locator

    @allure.step('Ожидаем, пока текст перестанет быть виден на экране')
    def wait_text(self,locator,text):
        self.wait.until_not(expected_conditions.text_to_be_present_in_element_value(locator,text))

    @allure.step('Получаем текст с элемента')
    def get_text_from_element(self,locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Вводим текст')
    def add_text_to_element(self,locator,text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Переходим на последнее открытое окно в браузере')
    def switch_to_another_window(self):
        windows_list = self.driver.window_handles
        self.driver.switch_to.window(windows_list[-1])

    @allure.step('Скролим до элемента внизу экрана')
    def scroll_to_element(self, locator):
        element = self.driver.find_element (*locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'end'});", element)