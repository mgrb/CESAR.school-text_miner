from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.cesar.org.br")
html = driver.page_source
print(html)
