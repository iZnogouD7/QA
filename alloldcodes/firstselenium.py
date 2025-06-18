from selenium import webdriver
from selenium.common import NoSuchDriverException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
import time

driver = webdriver.ChromiumEdge()
driver.maximize_window()
driver.get("https://www.demoblaze.com")
try:
    nav_login=driver.find_element(By.ID,"login2")
    nav_login.click()
    uname = driver.find_element(By.ID,"loginusername")
    uname.send_keys("testmorning")

    pwd=driver.find_element(By.ID,"loginpassword")
    pwd.send_keys("test123")
    login_button=driver.find_element(By.XPATH,'//*[@id="logInModal"]/div/div/div[3]/button[2]')
    login_button.click()
except NoSuchElementException as x:
    print("No such Driver Element FOUND: ", x)
except ElementNotInteractableException as e:
    print("Element not interactable", e)


finally:
    driver.quit()