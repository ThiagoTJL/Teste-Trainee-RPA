from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.google.com/")
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="APjFqb"]'))).send_keys("baixar python")
driver.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys(Keys.RETURN)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3'))).click()

wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/section/div[2]/ol/li[3]/span[1]/a'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/section/article/table/tbody/tr[4]/td[1]/a'))).click()





