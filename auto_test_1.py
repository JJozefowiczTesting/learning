from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Testfile\chromedriver.exe")
driver.get("https://demobank.jaktestowac.pl/logowanie_etap_1.html")
title = driver.title
print(title)
assert title == "Demobank - Bankowość Internetowa - Logowanie"
driver.close()