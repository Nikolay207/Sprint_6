from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_BUTTON = By.XPATH, '//div/button[@class = "Button_Button__ra12g"]'
    QUESTION = By.ID, 'accordion__heading-{}'
    ANSWER = By.ID, 'accordion__panel-{}'
    LOCATOR_TO_SCROLL = By.ID, 'accordion__heading-7'
    COOKIE_BANNER_BUTTON = By.ID, "rcc-confirm-button"
    BOTTOM_ORDER_CREATE = By.XPATH, '//div/button[@class = "Button_Button__ra12g Button_Middle__1CSJM"]'
