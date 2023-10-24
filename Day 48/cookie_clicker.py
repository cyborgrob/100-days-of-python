from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create Chrome webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.XPATH, value='//*[@id="cookie"]')

run = True
# How long you want the program to run
timeout = time.time() + 60


def check_for_upgrades():
    # Gets values of upgrades (replaces commas when converting str to int
    money = int(driver.find_element(By.ID, value='money').text.replace(',', ''))
    cursor = driver.find_element(By.CSS_SELECTOR, value='#buyCursor b')
    grandma = driver.find_element(By.CSS_SELECTOR, value='#buyGrandma b')
    factory = driver.find_element(By.CSS_SELECTOR, value='#buyFactory b')
    mine = driver.find_element(By.CSS_SELECTOR, value='#buyMine b')
    shipment = driver.find_element(By.CSS_SELECTOR, value='#buyShipment b')
    alchemy_lab = driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]')
    portal = driver.find_element(By.CSS_SELECTOR, value='#buyPortal b')
    time_machine = driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]')

    # Two separate lists because the two-word upgrades have different index for cost after splitting into list
    list_of_upgrades_1w = [cursor, grandma, factory, mine, shipment, portal]
    list_of_upgrades_2w = [alchemy_lab, time_machine]

    # Creates new lists of just the integer value costs of upgrades for both one-word and two-word upgrades
    cost_of_upgrades_1w = [int(upgrade.text.split()[2].replace(',', '')) for upgrade in list_of_upgrades_1w]
    cost_of_upgrades_2w = [int(upgrade.text.split()[3].replace(',', '')) for upgrade in list_of_upgrades_2w]
    # Creates a combined list and sorts it
    combined_cost_of_upgrades = cost_of_upgrades_1w + cost_of_upgrades_2w
    combined_cost_of_upgrades.sort()
    combined_cost_of_upgrades.reverse()

    # Iterate through list and if money > upgrade, buy the upgrade.
    counter = 0
    for cost in combined_cost_of_upgrades:
        if money > cost:
            if counter == 0:
                driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]').click()
                break
            elif counter == 1:
                driver.find_element(By.XPATH, value='//*[@id="buyPortal"]').click()
                break
            elif counter == 2:
                driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]').click()
                break
            elif counter == 3:
                driver.find_element(By.XPATH, value='//*[@id="buyShipment"]').click()
                break
            elif counter == 4:
                driver.find_element(By.XPATH, value='//*[@id="buyMine"]').click()
                break
            elif counter == 5:
                driver.find_element(By.XPATH, value='//*[@id="buyFactory"]').click()
                break
            elif counter == 6:
                driver.find_element(By.XPATH, value='//*[@id="buyGrandma"]').click()
                break
            elif counter == 7:
                driver.find_element(By.XPATH, value='//*[@id="buyCursor"]').click()
                break
        counter += 1


while run:
    # Click X number of times
    for x in range(300):
        cookie.click()
    # Check for upgrades
    check_for_upgrades()
    if time.time() > timeout:
        run = False

driver.quit()
