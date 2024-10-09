from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Inicializando o driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Acessando o Google
driver.get("https://www.google.com")
driver.implicitly_wait(10)

# Encontrando a caixa de pesquisa e realizando uma ação
search_box = driver.find_element(by=By.NAME, value="q")
search_box.send_keys("CESAR School")
search_box.submit()

# clicando no primeiro resultado
first_result = driver.find_element(by=By.CSS_SELECTOR, value="h3")
first_result.click()

# buscar e clicar no botão com id "onetrust-reject-all-handler"
reject_button = driver.find_element(by=By.ID, value="onetrust-reject-all-handler")
reject_button.click()

input()

# Fechando o navegador
driver.quit()
