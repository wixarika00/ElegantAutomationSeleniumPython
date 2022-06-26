from selenium.webdriver.common.by import By
from venvs.browser_automation.ElegantTest.base_element import BaseElement
from venvs.browser_automation.ElegantTest.base_page import BasePage
from locator import Locator


class TrainingGroundPage(BasePage):
    url = 'https://techstepacademy.com/training-ground'

    @property  # treates it as variable
    def button1(self):
        locator = Locator(by=By.ID, value='b1')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )



