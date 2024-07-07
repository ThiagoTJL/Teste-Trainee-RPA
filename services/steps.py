from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from database.mongodb import Database		
from datetime import datetime


class DownloadPythonSteps():

	errors_db = Database("erros")

	def __init__(self, driver) -> None:
		self._driver = driver
		self._wait = WebDriverWait(self._driver, 10)


	def open_browser(self, url:str) -> dict:
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


	def search(self, search_arg:str) -> dict:
		"""
		Realiza uma pesquisa no google para o termo desejado.

		Argumentos:
		- search_arg: O termo alvo da pesquisa.
		"""
		try:
			search_box = self._wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="APjFqb"]')))
			search_box.send_keys(search_arg)
			search_box.send_keys(Keys.RETURN)
			return {'error': False, 'msg': 'Pesquisa realizada com sucesso.'}
		except:
			msg = f'Falha ao pesquisar por termo: {search_arg}.'
			self.errors_db.insert({'msg': msg, 'datetime': datetime.now()})
			return {'error': True, 'msg': msg}
