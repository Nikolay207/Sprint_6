from selenium.webdriver.common.by import By

class OrderPageLocators:
    ORDER_HEADER = By.XPATH, '//div[@class = "Order_Header__BZXOb"]'
    FIRST_NAME = By.XPATH, '//input[@placeholder = "* Имя"]'
    SECOND_NAME = By.XPATH, '//input[@placeholder = "* Фамилия"]'
    ADDRESS = By.XPATH, '//input[@placeholder = "* Адрес: куда привезти заказ"]'
    METRO = By.XPATH, '//input[@placeholder = "* Станция метро"]'
    PHONE = By.XPATH, '//input[@placeholder = "* Телефон: на него позвонит курьер"]'
    RENT_HEADER = By.XPATH, '//div[@class = "Order_Header__BZXOb"]'
    CONFIRM_BUTTON = By.XPATH, '//button[@class = "Button_Button__ra12g Button_Middle__1CSJM"]'
    FINAL_CONFIRM_BUTTON = By.XPATH, '//button[text() = "Да"]'
    METRO_OPTION = By.XPATH, "//li[@data-index='{}']"
    DATE_FIELD = By.XPATH, '//input[@placeholder = "* Когда привезти самокат"]'
    DATE_OPTION = By.XPATH, "//div[contains(@class,'react-datepicker__day--0{}')]"
    RENTAL_PERIOD = By.XPATH, '//div[@class = "Dropdown-placeholder"]'
    DAY_RENTAL = By.XPATH, '//div[text()="четверо суток"]'
    COLOR = By.ID, '{}'
    COMMENT = By.XPATH, '//input[@class = "Input_Input__1iN_Z Input_Responsible__1jDKN"]'
    CANSEL_ORDER = By.XPATH, '//button[@class = "Button_Button__ra12g Button_Middle__1CSJM Button_Inverted__3IF-i"]'
    STATUS_BUTTON = By.XPATH, '//button[text()="Посмотреть статус"]'
    ORDER_SUCCESS = By.XPATH, '//div[@class = "Order_ModalHeader__3FDaJ"]'