# import pytest
import time

from seleniumwire import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.firefox.options import Options as FirefoxOptions

#Mute the browser
options = FirefoxOptions()
# options.set_preference("media.volume_scale", "0.0")


driver = webdriver.Firefox(options=options)

#Join Blinest
driver.get("https://blinest.com/parties/quiz-general")

driver.title
driver.implicitly_wait(2)

#Join the game
join_btn = driver.find_element(By.CLASS_NAME, "btn")
join_btn.click()
print("[bbb] :  Waiting for game to start")

#Wait for the joining modal to disappear and accept cookies TODO : manage finished games and their modals
bye_modal = WebDriverWait(driver, 45).until(ec.invisibility_of_element_located(driver.find_element(By.ID, "startModal")))
time.sleep(2)
driver.find_element(By.CLASS_NAME, "cookie-consent__agree").click()

print("[bbb] :  Game has started")

count = 1


# Intercept the url of song media file
while(True) :
    print("Fetch : " + str(count))
    req = driver.wait_for_request('https:\/\/cdns-preview',100)
    print(req)
    del driver.requests # must delete all requests otherwise "wait for request" function will return the first request matching in the list forever
    time.sleep(20)
    count += 1
