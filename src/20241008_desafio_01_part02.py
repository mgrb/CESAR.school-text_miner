"""Web Screping - Desafio 01 - Parte 02.

Wikipedia - Pesquisar sobre o CESAR

Usando o SELENIUN acesse a pagina: https://pt.wikipedia.org/
2. Na bara de busca pesquise pelo termo "cesar" (em minúsculo)
3. Na página que abrir, click no link do CESAR "*Centro de Estudos e Sistemas Avançados do Recife, conhecido como Instituto CESAR*"
4. Com os dados da página colete as informações necessárias para completar corretamente o texto do print (a célula a baixo deve ficar por ultimo no teu notebook).
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager


def navegate_to_cesar_page(driver: WebDriver):
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


def transform_table_data(data_table: WebElement) -> dict:
    dados = []
    for row in data_table.find_elements(By.TAG_NAME, "tr"):
        colunas = row.find_elements(By.TAG_NAME, "td")
        if colunas:
            dados.append([coluna.text for coluna in colunas])

    # Transformando a lista de listas em um dicionário
    dict_data = {}
    for dado in dados:
        if len(dado) == 2:
            dict_data[dado[0].lower().replace(" ", "_")] = dado[1]
    return dict_data


def extract_data_table(driver: WebDriver) -> dict:
    # Localiza a tabela com dados basicos do CESAR pela classe CSS (utilizando 'CSS_SELECTOR' com todas as classes)
    data_table_basic = driver.find_element(By.CSS_SELECTOR, "table.infobox.infobox_v2")
    dados = transform_table_data(data_table_basic)

    return dados


def extract_fundadores(fundadores_str: str) -> list:
    fundadores = fundadores_str.replace(" e ", ", ")
    return fundadores.split(", ")


# Inicializando o driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

navegate_to_cesar_page(driver)
table = extract_data_table(driver)

# Coletando os dados do CESAR a partir da página do wikipedia do driver

fundadores = extract_fundadores(table.get("fundadores"))
organizacao = table.get("organização").split("\n")

tipo = table.get("tipo")
data_fundacao = table.get("fundação")
fundador_01 = fundadores[0]
fundador_02 = fundadores[1]
fundador_03 = fundadores[2]
local_fundacao = table.get("sede")
ceo = organizacao[0]
coo = organizacao[1]
numero_funcionarios = table.get("empregados")
graduacao_01 = ""
graduacao_02 = ""
metrado_01 = ""
mestrado_01 = ""
doutorado_01 = ""
site = table.get("sítio_oficial")

print(f"""
      O CESAR é um {tipo} fundado em {data_fundacao} por {fundador_01}, {fundador_02}, {fundador_03}
      em {local_fundacao}. Segundo os dados coletados, {ceo} e {coo} são os chefes da organização
      que tem {numero_funcionarios}. O CESAR possui cursos de {graduacao_01}, {graduacao_02}, {metrado_01},
      {mestrado_01}, {doutorado_01}. Para mais detalhes dessa instituição incrível, acesse {site}
""")

input("Pressione ENTER para fechar o navegador...")
