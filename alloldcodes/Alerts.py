from ftplib import all_errors

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.ChromiumEdge()
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Alerts.html")
alert_with_ok_button = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a')
alert_with_ok_button.click()
time.sleep(2)
middle_button = driver.find_element(By.XPATH,'//*[@id="OKTab"]/button')
middle_button.click()
time.sleep(2)
alert = driver.switch_to.alert
alert.accept()
time.sleep(3)

alert_with_okandcancle_button=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a')
alert_with_okandcancle_button.click()
middle_button2 = driver.find_element(By.XPATH,'//*[@id="CancelTab"]/button')
middle_button2.click()
time.sleep(2)
alert.dismiss()
time.sleep(2)

alert_with_text_button=driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a')
alert_with_text_button.click()
middle_button_text=driver.find_element(By.XPATH,'/*[@id="Textbox"]/button')
middle_button_text.click()
alert.click()
alert.send_keys("Roshan")
time.sleep(2)
alert.accept()
time.sleep(2)
driver.quit()