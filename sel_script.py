from selenium import webdriver

driver = webdriver.Chrome()

try: 
    driver.get("https://google.com")

    print(driver.title)
finally:
    driver.quit()