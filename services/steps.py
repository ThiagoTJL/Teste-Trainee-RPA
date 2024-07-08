from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from database.mongodb import Database
from datetime import datetime
import os
import time


class DownloadPythonSteps():

    errors_db = Database("erros")

    def __init__(self, driver) -> None:
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)
        self.download_dir = os.path.join(os.path.dirname(__file__), 'downloads')

    def open_browser(self, url: str) -> dict:
        """
        Abre a URL solicitada.

        Argumentos:
        - url: A URL desejada para abrir no navegador.
        """
        try:
            self._driver.get(url)
            return {'error': False, 'msg': 'Navegador aberto com sucesso.'}
        except:
            msg = 'Falha ao abrir o navegador.'
            self.errors_db.insert({'msg': msg, 'datetime': datetime.now()})
            return {'error': True, 'msg': msg}

    def search(self, search_arg: str) -> dict:
        """
        Realiza uma pesquisa no google para o termo desejado.

        Argumentos:
        - search_arg: O termo alvo da pesquisa.
        """
        try:
            search_box = self._wait.until(EC.element_to_be_clickable((By.ID, 'APjFqb')))
            search_box.send_keys(search_arg)
            search_box.send_keys(Keys.RETURN)
            return {'error': False, 'msg': 'Pesquisa realizada com sucesso.'}
        except:
            msg = f'Falha ao pesquisar por termo: {search_arg}.'
            self.errors_db.insert({'msg': msg, 'datetime': datetime.now()})
            return {'error': True, 'msg': msg}

    def click_first_result(self) -> dict:
        try:
            first_result = self._wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3')))
            first_result.click()
            return {'error': False, 'msg': 'Primeiro resultado clicado com sucesso.'}
        except:
            msg = 'Falha ao clicar no primeiro resultado da pesquisa.'
            self.errors_db.insert({'msg': msg, 'datetime': datetime.now()})
            return {'error': True, 'msg': msg}

    def click_download_link(self) -> dict:
        try:
            download_link = self._wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/section/div[2]/ol/li[3]/span[1]/a')))
            download_link.click()
            return {'error': False, 'msg': 'Link de download clicado com sucesso.'}
        except:
            msg = 'Falha ao clicar no link de download.'
            self.errors_db.insert({'msg': msg, 'datetime': datetime.now()})
            return {'error': True, 'msg': msg}

    def click_final_download_link(self) -> dict:
        try:
            final_download_link = self._wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/section/article/table/tbody/tr[4]/td[1]/a')))
            final_download_link.click()
            return {'error': False, 'msg': 'Link final de download clicado com sucesso.'}
        except:
            msg = 'Falha ao clicar no link final de download.'
            self.errors_db.insert({'msg': msg, 'datetime': datetime.now()})
            return {'error': True, 'msg': msg}

    def wait_for_download(self) -> dict:
        """
        Espera até que o download seja concluído.
        """
        try:
            download_wait_time = 0
            while not any([file.endswith(".crdownload") for file in os.listdir(self.download_dir)]):
                time.sleep(1)
                download_wait_time += 1
                if download_wait_time > 300:  # 5 minutos de espera
                    msg = 'Tempo limite para download excedido.'
                    self.errors_db.insert({'msg': msg, 'datetime': datetime.now()})
                    return {'error': True, 'msg': msg}

            # Espera o arquivo .crdownload sumir (indicando fim do download)
            while any([file.endswith(".crdownload") for file in os.listdir(self.download_dir)]):
                time.sleep(1)

            return {'error': False, 'msg': 'Download concluído com sucesso.'}
        except Exception as e:
            msg = f'Erro ao esperar o download ser concluído: {str(e)}'
            self.errors_db.insert({'msg': msg, 'datetime': datetime.now()})
            return {'error': True, 'msg': msg}
