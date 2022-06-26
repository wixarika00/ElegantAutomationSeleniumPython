from selenium.webdriver.common.by import By

from venvs.browser_automation.ElegantTest.base_element import BaseElement
from venvs.browser_automation.ElegantTest.base_page import BasePage
from locator import Locator


class TrialPage(BasePage):
    url = 'https://techstepacademy.com/trial-of-the-stones'

    @property
    def stone_inpt(self):
        locator = Locator(By.CSS_SELECTOR, 'input#r1Input')
        return BaseElement(self.driver, locator=locator)

    @property
    def stone_button(self):
        locator = Locator(By.CSS_SELECTOR, 'button#r1Btn')
        return BaseElement(self.driver, locator=locator)

    @property
    def secrets_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input#r2Input')
        return BaseElement(self.driver, locator=locator)

    @property
    def secrets_button(self):
        locator = Locator(By.CSS_SELECTOR, 'input#r2Butn')
        return BaseElement(self.driver, locator=locator)

