import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import presence_of_element_located, visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.ChromiumEdge()
wait=WebDriverWait(driver,10)
driver.maximize_window()
driver.get("https://www.demoblaze.com")

try:

    nav_login=driver.find_element(By.ID,"login2")
    #nav_login=wait.until(presence_of_element_located((By.ID,"login2")))
    #nav_login=wait.until(visibility_of_element_located(By.ID,"login2"))
    nav_login.click()
    wait.until(EC.element_to_be_clickable(By.ID,"login2"))


    uname = driver.find_element(By.ID,"loginusername")
    uname.send_keys("testmorning")
    pwd=driver.find_element(By.ID,"loginpassword")
    pwd.send_keys("test123")


    login_button=driver.find_element(By.XPATH,'//*[@id="logInModal"]/div/div/div[3]/button[2]')
    login_button.click()
except NoSuchElementException as e:
    print("No such Element FOUND: ", e)

finally:
    driver.quit()



