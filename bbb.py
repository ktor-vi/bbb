# import pytest
import time

from seleniumwire import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.firefox.options import Options as FirefoxOptions

import urllib.request
import asyncio
from shazamio import Shazam, Serialize

#Mute the browser
options = FirefoxOptions()
# options.set_preference("media.volume_scale", "0.0")


driver = webdriver.Firefox(options=options)

#Join Blinest
driver.get("https://blinest.com/rooms/quiz-general")

driver.title
driver.implicitly_wait(2)

#Fill in email + password

email = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
password = driver.find_element(By.CSS_SELECTOR, "input[type='password']")

email.send_keys("voitokas.sakotiov@gmail.com")
password.send_keys("JEANMIDU13")

connect_btn = driver.find_element(By.CLASS_NAME, "btn-primary")
connect_btn.click()

#Join the game

print("[bbb] :  Waiting for game to start")

#Wait for the joining modal to disappear and accept cookies TODO : manage finished games and their modals
#bye_modal = WebDriverWait(driver, 45).until(ec.invisibility_of_element_located(driver.find_element(By.ID, "startModal")))
#time.sleep(2)
#driver.find_element(By.CLASS_NAME, "cookie-consent__agree").click()

print("[bbb] :  Game has started")

count = 1

# Intercept the url of song media file
while(True) :
    print("Fetch : " + str(count))
    req = driver.wait_for_request('https:\/\/cdns-preview',100)
    print(req)
    urllib.request.urlretrieve(req.url, "file.mp3") # type: ignore
    
    async def main():
        shazam = Shazam()
        song = await shazam.recognize_song('file.mp3')
        #serialized = Serialize.track(song)
        #title = song.get("title")
        #artist = song.get("subtitle")
        title = song['track']['title']
        artist = song['track']['subtitle']

        answer = title + ' ' + artist
        print(answer)

        answer_field = driver.find_element(By.CLASS_NAME, "text-2xl")
        answer_field.send_keys(answer)

        send_button = answer_field = driver.find_element(By.CLASS_NAME, "btn-send")
        send_button.click()
        
        #print(song)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    del driver.requests # must delete all requests otherwise "wait for request" function will return the first request matching in the list forever
    time.sleep(20)
    count += 1
