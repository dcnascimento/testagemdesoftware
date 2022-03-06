from selenium import webdriver
from selenium.webdriver.common.by import By 

session = webdriver.Firefox(executable_path="C:\geckodriver.exe")

session.get("https://kabum.com.br/")