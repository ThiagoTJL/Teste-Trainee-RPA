from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ServiceChrome
from webdriver_manager.chrome import ChromeDriverManager


class ChromeDriver:
	"""
	Classe para gerenciar a instância do Chrome WebDriver usando Selenium.

	Métodos:
	- chrome(): Inicializa e retorna uma instância do Chrome WebDriver.
	"""
	_driver = None

	def __init__(self) -> None:
		"""
		Inicializa a instância do Chrome WebDriver.

		Retorna:
		webdriver: Instância do Chrome WebDriver.
		
		Lança:
		ConnectionError: Se não for possível iniciar o navegador Chrome.
		"""
		try:
			service_chrome = ServiceChrome(executable_path=ChromeDriverManager().install())
			self._driver = webdriver.Chrome(service=service_chrome)
		except Exception as e:
			raise ConnectionError('Falha ao inicializar o navegador') from e


	def get_driver(self) -> webdriver:
		"""
		Obtém o driver instanciado
		"""
		return self._driver
