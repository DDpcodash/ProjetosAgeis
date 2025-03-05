from selenium import webdriver
from login import linkedin_login
from scraper import buscar_vagas

# Credenciais do LinkedIn
EMAIL = "seu_email_aqui"
PASSWORD = "sua_senha_aqui"
URL_VAGAS = "https://www.linkedin.com/jobs/search/?keywords=Desenvolvedor%20Python"

# Configuração do Selenium
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  
driver = webdriver.Chrome(options=options)

try:
    # Fazer login
    driver = linkedin_login(driver, EMAIL, PASSWORD)

    # Buscar vagas
    vagas = buscar_vagas(driver, URL_VAGAS)

    # Exibir resultados
    for vaga in vagas:
        print(vaga)

finally:
    driver.quit()  # Fecha o navegador ao terminar
