from selenium import webdriver
from selenium.webdriver.common.by import By

session = webdriver.Firefox(executable_path="C:\geckodriver")

session.get("https://kabum.com.br")
login = session.find_element(By.ID, 'linkLoginHeader')

login.click()