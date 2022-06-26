from selenium import webdriver
from selenium.webdriver.support.select import Select

browser1 = webdriver.Chrome()
browser2 = webdriver.Chrome()

browser1.get("https://techstepacademy.com/training-ground")

browser1.execute_script('window.open("https://techstepacademy.com/training-ground","_blank")')
browser1.execute_script('window.open("https://techstepacademy.com/training-ground","_blank")')
browser1.execute_script('window.open("https://techstepacademy.com/training-ground","_blank")')
browser1.execute_script('window.open("https://techstepacademy.com/training-ground","_blank")')
# browser1.execute_script('window.open("https://google.com","_blank")')
# browser1.execute_script('window.open("https://yahoo.com","_blank")')
# browser1.execute_script('window.open("https://google.com","_blank")')