from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def linkedin_login(driver, email, password):
    """ Faz login no LinkedIn e retorna o navegador logado. """
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)

    email_input = driver.find_element(By.ID, "username")
    email_input.send_keys(email)

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    time.sleep(3)  # Espera o login ser processado
    return driver
