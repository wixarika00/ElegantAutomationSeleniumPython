from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://techstepacademy.com/iframe-training")

iframe = browser.find_element_by_css_selector("iframe")
browser.switch_to.frame(iframe)
welcome_text = browser.find_element_by_css_selector("div#block-ec928cee802cf918d26c div p")
print(welcome_text.text)
browser.switch_to.default_content()  # takes back out from frame
title_text = browser.find_element_by_css_selector("div#block-5d3de848045889000188d389 div p")
print(title_text.text)





