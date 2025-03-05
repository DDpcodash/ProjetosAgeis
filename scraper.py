from selenium.webdriver.common.by import By
import time

def buscar_vagas(driver, url_vagas):
    """ Acessa a página de vagas e retorna uma lista de dicionários com os resultados. """
    driver.get(url_vagas)
    time.sleep(5)  # Espera carregar

    vagas = driver.find_elements(By.CLASS_NAME, "job-card-container")
    
    resultados = []
    for vaga in vagas[:10]:  # Pega as 10 primeiras vagas
        titulo = vaga.find_element(By.CLASS_NAME, "job-card-list__title").text
        empresa = vaga.find_element(By.CLASS_NAME, "job-card-container__company-name").text
        localizacao = vaga.find_element(By.CLASS_NAME, "job-card-container__metadata-item").text
        link = vaga.find_element(By.TAG_NAME, "a").get_attribute("href")

        resultados.append({
            "Título": titulo,
            "Empresa": empresa,
            "Localização": localizacao,
            "Link": link
        })

    return resultados
