# Our Test
from selenium import webdriver
from training_ground_page import TrainingGroundPage

# Test Setup
from venvs.browser_automation.ElegantTest.trial_page import TrialPage

browser = webdriver.Chrome()

# Test
trial_page = TrialPage(driver=browser)
trial_page.go()
trial_page.stone_inpt.input_text("rock")
trial_page.stone_button.click()

#
trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
assert trng_page.button1.text == 'Button1', "Unexpected button1 text"

browser.quit()

