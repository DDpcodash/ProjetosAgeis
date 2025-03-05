from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def linkedin_login(email, password):
    """ Faz login no LinkedIn e retorna o navegador logado. """
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Abre o navegador maximizado
    driver = webdriver.Chrome(options=options)

    try:
        # Acessa a página de login
        driver.get("https://www.linkedin.com/login")
        time.sleep(2)

        # Insere email
        email_input = driver.find_element(By.ID, "username")
        email_input.send_keys(email)

        # Insere senha
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)

        time.sleep(3)  # Aguarda o login ser processado

        # Verifica se o login foi bem-sucedido acessando a home do LinkedIn
        if "feed" in driver.current_url:
            print("✅ Login bem-sucedido!")
        else:
            print("❌ Falha no login. Verifique suas credenciais.")

    except Exception as e:
        print(f"Erro durante o login: {e}")

    finally:
        time.sleep(5)  # Tempo para visualizar o resultado antes de fechar
        # driver.quit()

# Teste direto
EMAIL = @#$email
PASSWORD = @#$senha

linkedin_login(EMAIL, PASSWORD)
