"""
This script demonstrates web automation using Selenium WebDriver with Chrome.
It navigates to Google, searches for "download python", clicks on the first search result,
navigates to the desired download link, and clicks the final download link.

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ServiceChrome
from webdriver_manager.chrome import ChromeDriverManager

class Driver:
    """
    A class to manage the Chrome WebDriver instance using Selenium.

    Methods:
    - chrome(): Initializes and returns a Chrome WebDriver instance.
    """

    def __init__(self) -> None:
        self._service_chrome = None
        self._driver = None

    def chrome(self) -> webdriver:
        """
        Initialize the Chrome WebDriver instance.

        Returns:
        webdriver: Chrome WebDriver instance.
        
        Raises:
        ConnectionError: If unable to start the Chrome browser.
        """
        try:
            self._service_chrome = ServiceChrome(executable_path=ChromeDriverManager().install())
            self._driver = webdriver.Chrome(service=self._service_chrome)
        except Exception as e:
            raise ConnectionError('Failed to initialize browser') from e
        
        return self._driver

# Initialize the Driver
driver_manager = Driver()
driver = driver_manager.chrome()

try:
    # Open Google page
    driver.get("https://www.google.com/")

    # Create WebDriverWait
    wait = WebDriverWait(driver, 10)

    # Wait for search box to be clickable and send search query
    search_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="APjFqb"]')))
    search_box.send_keys("download python")
    search_box.send_keys(Keys.RETURN)

    # Wait for and click the first search result
    first_result = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3')))
    first_result.click()

    # Wait for and click the desired download link on the next page
    download_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/section/div[2]/ol/li[3]/span[1]/a')))
    download_link.click()

    # Wait for and click the final download link
    final_download_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/section/article/table/tbody/tr[4]/td[1]/a')))
    final_download_link.click()

except Exception as e:
    print(f"An error occurred: {e}")
