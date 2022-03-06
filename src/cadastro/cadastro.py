#Testes de Geisana Fonseca Rodrigues

#from lib2to3.pgen2 import driver
from selenium import webdriver
import time



navegador = webdriver.Chrome()
navegador.get("https://www.kabum.com.br/login")

#Logar com email invalido e retornar mensagem de erro
def CT_001():
    #email
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[1]/div/div/input')
    campo.send_keys('numero7')

    #senha 
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[2]/div/div/input')
    campo.send_keys('numero7')

    #confirmação de senha 
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[3]/div/div/input')
    campo.send_keys('numero7')

    #cpf
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[5]/div/div/input')
    campo.send_keys('60889838330')

    #cep
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[6]/div/div/input')
    campo.send_keys('65110000')

    #cadastro
    campo = navegador.find_element_by_id("botaoPreCadastro")
    campo.click()

    assert 'Insira um e-mail válido.' in navegador.page_source

    time.sleep(3)
    return None 

#Logar com cpf invalido e retornar mensagem de erro
def CT_002():
    
    #email
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[1]/div/div/input')
    campo.send_keys('frgeisana@gmail.com')

    #senha 
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[2]/div/div/input')
    campo.send_keys('numero7')

    #confirmação de senha 
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[3]/div/div/input')
    campo.send_keys('numero7')

    #cpf
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[5]/div/div/input')
    campo.send_keys('608abc12347')

    #cep
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[6]/div/div/input')
    campo.send_keys('65110000')

    #cadastro
    campo = navegador.find_element_by_id("botaoPreCadastro")
    campo.click()

    assert 'Insira um documento válido.' in navegador.page_source

    time.sleep(3)
    return None 

#Logar com CNPJ invalido e retornar mensagem de erro
def CT_003():
    #email
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[1]/div/div/input')
    campo.send_keys('frgeisana@gmail.com')

    #senha 
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[2]/div/div/input')
    campo.send_keys('numero7')

    #confirmação de senha 
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[3]/div/div/input')
    campo.send_keys('numero7')

    #cpf
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[5]/div/div/input')
    campo.send_keys('00000000000000')

    #cep
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[6]/div/div/input')
    campo.send_keys('65110000')

    #cadastro
    campo = navegador.find_element_by_id("botaoPreCadastro")
    campo.click()

    assert 'Insira um documento válido.' in navegador.page_source

    time.sleep(3)
    return None 

#Logar com senha com caractere invalido e retornar mensagem de erro
def CT_004():

    
    #email
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[1]/div/div/input')
    campo.send_keys('frgeisana@gmail.com')

    #senha 
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[2]/div/div/input')
    campo.send_keys('geïsana1')

    #confirmação de senha 
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[3]/div/div/input')
    campo.send_keys('geïsana1')

    #cpf
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[5]/div/div/input')
    campo.send_keys('60889838330')

    #cep
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[6]/div/div/input')
    campo.send_keys('65110000')

    #cadastro
    campo = navegador.find_element_by_id("botaoPreCadastro")
    campo.click()

    assert 'Senha deve conter apenas caracteres válidos.' in navegador.page_source

    time.sleep(3)
    return None 

#Logar com o campo de senha sem preenchimento e  retornar mensagem de erro
def CT_005():
    #email
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[1]/div/div/input')
    campo.send_keys('frgeisana@gmail.com')

    #senha 
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[2]/div/div/input')
    campo.send_keys('')

    #confirmação de senha 
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[3]/div/div/input')
    campo.send_keys('')

    #cpf
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[5]/div/div/input')
    campo.send_keys('60889838330')

    #cep
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[6]/div/div/input')
    campo.send_keys('65110000')

    #cadastro
    campo = navegador.find_element_by_id("botaoPreCadastro")
    campo.click()

    assert 'Este campo é obrigatório' in navegador.page_source

    time.sleep(3)
    return None 


#Logar com o cep invalido e  retornar mensagem de erro
def CT_006():
    #email
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[1]/div/div/input')
    campo.send_keys('frgeisana@gmail.com')

    #senha 
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[2]/div/div/input')
    campo.send_keys('123Geisana')

    #confirmação de senha 
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[3]/div/div/input')
    campo.send_keys('123Geisana')

    #cpf
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[5]/div/div/input')
    campo.send_keys('60889838330')

    #cep
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[6]/div/div/input')
    campo.send_keys('00000000')

    #cadastro
    campo = navegador.find_element_by_id("botaoPreCadastro")
    campo.click()

    assert 'Algo deu errado ao tentar buscar seu CEP, tente novamente mais tarde!' in navegador.page_source

    time.sleep(3)
    return None 

#Logar com o senha sem numeros e  retornar mensagem de erro
def CT_007():
    #email
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[1]/div/div/input')
    campo.send_keys('frgeisana@gmail.com')

    #senha 
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[2]/div/div/input')
    campo.send_keys('Geisana')

    #confirmação de senha 
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[3]/div/div/input')
    campo.send_keys('Geisana')

    #cpf
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[5]/div/div/input')
    campo.send_keys('60889838330')

    #cep
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[6]/div/div/input')
    campo.send_keys('65110000')

    #cadastro
    campo = navegador.find_element_by_id("botaoPreCadastro")
    campo.click()

    assert 'Senha deve conter números.' in navegador.page_source

    time.sleep(3)
    return None 

#Criar senha com mais de 32 dígitos e não possibilitar o cadastro.
def CT_008():
    #email
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[1]/div/div/input')
    campo.send_keys('frgeisana@gmail.com')

    #senha 
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[2]/div/div/input')
    campo.send_keys('geisana123456789101112131415161718191')

    #confirmação de senha 
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[3]/div/div/input')
    campo.send_keys('geisana123456789101112131415161718191')

    #cpf
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[5]/div/div/input')
    campo.send_keys('60889838330')

    #cep
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[6]/div/div/input')
    campo.send_keys('65110000')

    #cadastro
    campo = navegador.find_element_by_id("botaoPreCadastro")
    campo.click()

    assert 'Senha deve ter no máximo 32 caracteres.' in navegador.page_source

    time.sleep(3)
    return None 

#CCriar senha com menos de 6 dígitos e não possibilitar o cadastro
def CT_009():
    #email
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[1]/div/div/input')
    campo.send_keys('frgeisana@gmail.com')

    #senha 
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[2]/div/div/input')
    campo.send_keys('a1452')

    #confirmação de senha 
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[3]/div/div/input')
    campo.send_keys('a1452')

    #cpf
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[5]/div/div/input')
    campo.send_keys('60889838330')

    #cep
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[6]/div/div/input')
    campo.send_keys('65110000')

    #cadastro
    campo = navegador.find_element_by_id("botaoPreCadastro")
    campo.click()

    assert 'Senha deve ter no mínimo 6 caracteres.' in navegador.page_source

    time.sleep(3)
    return None 


#Cadastrar todos os dados corretamente e realizar o procedimento com sucesso.
def CT_010():
    #email
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[1]/div/div/input')
    campo.send_keys('frgeisana@gmail.com')

    #senha 
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[2]/div/div/input')
    campo.send_keys('Geisana12')

    #confirmação de senha 
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[3]/div/div/input')
    campo.send_keys('Geisana12')

    #cpf
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[5]/div/div/input')
    campo.send_keys('60889838330')

    #cep
    campo = navegador.find_element_by_xpath('//*[@id="formPreCadastro"]/div[1]/div[6]/div/div/input')
    campo.send_keys('65110000')

    #cadastro
    campo = navegador.find_element_by_id("botaoPreCadastro")
    campo.click()

    time.sleep(5)
    return None 


if __name__ == '__main__':
    #CT_001 ()
    #CT_002 ()
    #CT_003 ()
    #CT_004 ()
    #CT_005 ()
    #CT_006 ()
    #CT_007 ()
    #CT_008()
    #CT_009 ()
    CT_010 ()
    navegador.close()

