from selenium import webdriver
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/training-ground")

sel = browser.find_element_by_id('sel1')
my_select = Select(sel)
my_select.options
print([elem.text for elem in my_select.options])
my_select.select_by_index(0)
my_select.select_by_value('second')
print(my_select.first_selected_option.text)

