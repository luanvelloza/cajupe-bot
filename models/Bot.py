from selenium import webdriver
import time

class Bot():
    def __init__(self):
        self.driver = ''

    def init_driver(self):
        self.driver = webdriver.Chrome()
    
    def open_site(self, alert_text: str = None):
        self.driver.get("https://appcajupe.com/#/login")
        print(alert_text, "") if alert_text else 0
        input("Digite qualquer tecla para continuar (10 segundos): ")
        self.time_sleep_count(10)

    def time_sleep_count(self, t = int):
        for i in range (1, t):
            print(f'{i}')
            time.sleep(1)