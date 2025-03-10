import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Pegando credenciais do sistema
EMAIL = os.environ.get("LINKEDIN_EMAIL")
PASSWORD = os.environ.get("LINKEDIN_PASSWORD")

def linkedin_login(email, password):
    """ Faz login no LinkedIn e mantém a página aberta no Safari. """
    
    if not email or not password:
        print("❌ ERRO: Credenciais não encontradas! Defina as variáveis de ambiente.")
        return None

    driver = webdriver.Safari()

    try:
        driver.get("https://www.linkedin.com/login")
        time.sleep(2)

        # Insere email
        email_input = driver.find_element(By.ID, "username")
        email_input.send_keys(email)

        # Insere senha
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys(password)
        password_input.submit()

        time.sleep(3)

        # Verifica se o login foi bem-sucedido
        if "feed" in driver.current_url:
            print("✅ Login bem-sucedido! Navegador permanecerá aberto.")
        else:
            print("❌ Falha no login. Verifique suas credenciais.")
            return None

    except Exception as e:
        print(f"Erro durante o login: {e}")
        return None

    return driver

def acessar_pagina_empregos(driver):
    """ Após login, acessa a página de empregos do LinkedIn. """
    try:
        driver.get("https://www.linkedin.com/jobs/")
        time.sleep(3)  # Espera carregar
        print("✅ Página de empregos acessada com sucesso!")
    except Exception as e:
        print(f"Erro ao acessar página de empregos: {e}")

# Executa o login
driver = linkedin_login(EMAIL, PASSWORD)

if driver:
    acessar_pagina_empregos(driver)
