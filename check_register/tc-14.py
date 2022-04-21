from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://nhanvan.vn/")

driver.find_element(By.XPATH, "//*[@id='header']/div[2]/div/div/div[3]/div/div[3]/a[2]").click()
driver.find_element(By.NAME, "register").click()
driver.find_element(By.NAME,"customer[last_name]").send_keys("Nguyễn")
driver.find_element(By.XPATH, "//*[@id='create_customer']/div[7]/div/input").click()

time.sleep(6)
driver.close()
