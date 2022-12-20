from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")
driver.maximize_window()  #ekranı tam boyutuna getirir
sleep(3)

input = driver.find_element(By.NAME,"username")   #inputu bul
input.send_keys("hilal.krl")
input = driver.find_element(By.NAME,"password")
input.send_keys("123456789")
sleep(3)

loginBtn = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]")
loginBtn.click()
sleep(3)

loginBtnText = loginBtn.text

if loginBtnText == "Log in":
    print("Test başarılı 😎")
else:
    print("Test Başarısız ❌")

loginBtn.click()
sleep(3)


