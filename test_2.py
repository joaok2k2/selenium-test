from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://joaok2k2.github.io/netpunk/")

series = browser.find_elements_by_class_name("item")

for nomes in series:
    boxfilmes = nomes.find_element_by_class_name("box-filme")
    nomes_s = boxfilmes.get_attribute("alt")
    print(f"Nomes dos filmes/series: {nomes_s}")

browser.quit()