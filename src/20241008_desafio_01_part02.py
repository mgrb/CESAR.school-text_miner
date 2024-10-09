"""Web Screping - Desafio 01 - Parte 02.

Wikipedia - Pesquisar sobre o CESAR

Usando o SELENIUN acesse a pagina: https://pt.wikipedia.org/
2. Na bara de busca pesquise pelo termo "cesar" (em minúsculo)
3. Na página que abrir, click no link do CESAR "*Centro de Estudos e Sistemas Avançados do Recife, conhecido como Instituto CESAR*"
4. Com os dados da página colete as informações necessárias para completar corretamente o texto do print (a célula a baixo deve ficar por ultimo no teu notebook).
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Inicializando o driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Acessando a wikipediawik
driver.get("https://pt.wikipedia.org/")
driver.implicitly_wait(10)

# Encontrando a caixa de pesquisa e realizando uma ação
search_box = driver.find_element(by=By.NAME, value="search")
search_box.send_keys("cesar")
especial_search_link = driver.find_element(
    By.CSS_SELECTOR, "a.cdx-menu-item__content.cdx-typeahead-search__search-footer"
)

especial_search_link.click()

# Clicar no link que contenha o title = "Centro de Estudos e Sistemas Avançados do Recife, conhecido como Instituto CESAR"
title_link = "Centro de Estudos e Sistemas Avançados do Recife"
cesar_link = driver.find_element(by=By.XPATH, value=f"//a[@title='{title_link}']")
cesar_link.click()

# print o conteúdo da página
print(driver.page_source)

input("Pressione ENTER para fechar o navegador...")

# Coletando os dados do CESAR a partir da página do wikipedia do driver


# tipo                =
# data_fundacao       =
# fundador_01         =
# fundador_02         =
# fundador_03         =
# local_fundacao      =
# ceo                 =
# coo                 =
# numero_funcionarios =
# graduacao_01        =
# graduacao_02        =
# metrado_01          =
# mestrado_01         =
# doutorado_01        =
# site                =

# print(f"""
#       O CESAR é um {tipo} fundado em {data_fundacao} por {fundador_01}, {fundador_02}, {fundador_03}
#       em {local_fundacao}. Segundo os dados coletados, {ceo} (CEO) e {coo} (COO) são os chefes da organização
#       que tem {numero_funcionarios}. O CESAR possui cursos de {graduacao_01}, {graduacao_02}, {metrado_01},
#       {mestrado_01}, {doutorado_01}. Para mais detalhes dessa instituição incrível, acesse {site}
# """)
