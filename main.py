from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

upgrades_available = driver.find_elements(By.CSS_SELECTOR, "#store div")
upgrade_ids = [i.get_attribute("id") for i in upgrades_available]

five_sec = time.time() + 5
five_min = time.time() + 5 * 60

while True:
    cookie.click()

    if time.time() > five_sec:
            
        upgrades = driver.find_elements(By.CSS_SELECTOR, "#store b")

        upgrades_cost= []
        for i in upgrades:
            text = i.text
            if text != "":
                cost = int(text.split("-")[1].strip().replace(",", ""))
                upgrades_cost.append(cost)

        money = driver.find_element(By.ID, "money").text
        if "," in money:
            money = money.replace(",", "")
        integ_money = int(money)

        cookie_upgrades = {}
        for i in range(len(upgrades_cost)):
            cookie_upgrades[upgrades_cost[i]] = upgrade_ids[i]

        can_buy = {}
        for money, id in cookie_upgrades.items():
            if integ_money > money:
                can_buy[money] = id

        if len(can_buy) > 0:
            pricey = max(can_buy)
            pricey_id = can_buy[pricey]

            driver.find_element(By.ID, pricey_id).click()

        five_sec = time.time() + 5

    if time.time() > five_min:
        cookie_per_sec = driver.find_element(By.ID, "cps").text
        print(cookie_per_sec)
        break