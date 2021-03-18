from selenium import webdriver
from time import sleep

def baixarPlanilha():
    navegador = webdriver.Chrome()
    navegador.get("https://ri.magazineluiza.com.br/")
    navegador.find_element_by_xpath('//*[@id="banner"]/a[1]/img').click()
    navegador.find_element_by_xpath('//*[@id="owl-destaques"]/div[1]/div/div[4]/div/a').click()
    navegador.find_element_by_xpath('//*[@id="N6rVFAHaJxLwG6CqK8aeTQ=="]').click()
    sleep(15)
    navegador.quit()


baixarPlanilha()