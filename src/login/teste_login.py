from selenium import webdriver
from selenium.webdriver.common.by import By

class Teste_Login:
    session = webdriver.Firefox(executable_path="C:\geckodriver.exe")
    session.get("https://kabum.com.br/login")

    botao_login = session.find_element(By.ID, 'botaoLogin')
    input_login = session.find_element(By.ID, 'inputUsuarioLogin')
    input_pwd = session.find_element(By.ID, 'inputSenhaLogin')
    botao_facebook = session.find_element(By.ID, 'botaoLoginFacebook')
    botao_google = session.find_element(By.ID, 'botaoLoginGoogle')

    def __init__(self) -> None:
        pass

    def efetuar_login(self, login, pwd):
        self.input_login.send_keys(login)
        self.input_pwd.send_keys(pwd)
        self.botao_login.click()

    def login_facebook(self):
        self.botao_facebook.click()

    def login_google(self):
        self.botao_google.click()

    def esqueceu_senha(self):
        input_email = session.find_element(By.ID, )




