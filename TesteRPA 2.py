from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ServiceChrome
from webdriver_manager.chrome import ChromeDriverManager

class Driver:
    def __init__(self) -> None:
        self._service_chrome = None
        self._driver = None

    def chrome(self) -> webdriver:
        try:
            self._service_chrome = ServiceChrome(executable_path=ChromeDriverManager().install())
            self._driver = webdriver.Chrome(service=self._service_chrome)
        except Exception as e:
            raise ConnectionError('Erro ao iniciar navegador') from e
        
        return self._driver

# Inicializa o Driver
driver_manager = Driver()
driver = driver_manager.chrome()

try:
    # Abre a página do Google
    driver.get("https://www.google.com/")

    # Cria um WebDriverWait
    wait = WebDriverWait(driver, 10)

    # Espera o campo de busca ser clicável e envia a busca
    search_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="APjFqb"]')))
    search_box.send_keys("baixar python")
    search_box.send_keys(Keys.RETURN)

    # Espera e clica no primeiro resultado da busca
    first_result = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3')))
    first_result.click()

    # Espera e clica no link desejado na página seguinte
    download_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/section/div[2]/ol/li[3]/span[1]/a')))
    download_link.click()

    # Espera e clica no link final de download
    final_download_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/section/article/table/tbody/tr[4]/td[1]/a')))
    final_download_link.click()

except Exception as e:
    print(f"Ocorreu um erro: {e}")