from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Safari()
driver.get("http://orteil.dashnet.org/experiments/cookie/")

purchase_times = {"buyCursor": 0, "buyGrandma": 0, "buyTime machine": 0, "buyPortal": 0,
                  "buyAlchemy lab": 0, "buyShipment": 0, "buyMine": 0, "buyFactory": 0}

while True:
    # Keep clicking cookies
    cookie = driver.find_element(By.ID, "cookie")
    cookie.click()

    # Check for upgrades every 5 seconds
    current_time = time.time()

    for upgrade in purchase_times:
        if current_time - purchase_times[upgrade] >= 5:
            try:
                driver.find_element(By.ID, upgrade).click()
                purchase_times[upgrade] = current_time
            except Exception as e:
                print(f"The {e} occurred")
                pass
