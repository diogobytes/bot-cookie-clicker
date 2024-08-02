from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Navigate to Wikipedia homepage
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Wait until the overlay (e.g., #darken) is not visible
time.sleep(10)


cookie = driver.find_element(By.ID, "bigCookie")


products = [
    driver.find_element(By.ID, "product0"),
    driver.find_element(By.ID, "product1"),
    driver.find_element(By.ID, "product2"),
    driver.find_element(By.ID, "product3"),
    driver.find_element(By.ID, "product4"),
]
timeout = time.time() + 5
while True:
    cookie_budget = int(
        driver.find_element(By.ID, "cookies").text.split(" ")[0].replace(",", "")
    )
    product_prices = []
    for i in range(5):
        price_text = driver.find_element(By.ID, f"productPrice{i}").text.replace(
            ",", ""
        )
        if price_text:
            product_prices.append(int(price_text))
        else:
            product_prices.append(float("inf"))

    cookie.click()

    if time.time() >= timeout:

        for i in reversed(range(5)):
            if cookie_budget > product_prices[i]:
                products[i].click()
                break

        timeout = time.time() + 5
