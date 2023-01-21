from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

import user
import password

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get('https://www.amazon.com.br/')
navegador.find_element('xpath', '//*[@id="nav-signin-tooltip"]/a/span').click()

sleep(3)

#Login
navegador.find_element('xpath', '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]').send_keys(user.email)
sleep(2)
navegador.find_element('xpath', '//*[@id="continue"]').click()
sleep(2)
navegador.find_element('xpath', '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[1]/input').send_keys(password.password)
sleep(2)
navegador.find_element('xpath', '//*[@id="signInSubmit"]').click()
sleep(2)


def product_search(name):
    navegador.find_element('xpath', '//*[@id="twotabsearchtextbox"]').send_keys(name)
    sleep(2)
    navegador.find_element('xpath', '//*[@id="nav-search-submit-button"]').click()
    sleep(2)

def select_and_add(main):
    # Seleção do Produto
    navegador.find_element('xpath', main).click()
    sleep(3)

    #Add no carrinho
    navegador.find_element('xpath', '//*[@id="add-to-cart-button"]').click()
    sleep(3)

product_search('Construindo uma Carreira em Software: um Guia Completo')

select_and_add('//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[2]')

# Limpar a Barra de Pesquisa
navegador.find_element('xpath', '//*[@id="twotabsearchtextbox"]').clear()
sleep(3)

product_search('Python')

select_and_add('//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[4]')

# Finalizar a compra
navegador.find_element('xpath', '//*[@id="sc-buy-box-ptc-button"]/span/input').click()
sleep(3)
