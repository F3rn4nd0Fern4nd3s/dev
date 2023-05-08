import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

#Espera aparecer o elemento que tem id de "side"
while True:
    time.sleep(5)
    break