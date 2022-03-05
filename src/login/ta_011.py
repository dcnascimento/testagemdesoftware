from selenium import webdriver
from selenium.webdriver.common.by import By

session = webdriver.Firefox(executable_path="C:\geckodriver")

session.get("https://kabum.com.br/login")

login = "igorsantossilva@dayrep.com"
pwd = "Q1w@e3r4"

botao_login = session.find_element(By.ID, 'botaoLogin')
input_login = session.find_element(By.ID, 'inputUsuarioLogin')
input_pwd = session.find_element(By.ID, 'inputSenhaLogin')

input_login.send_keys(login)
input_pwd.send_keys(pwd)
botao_login.click()



