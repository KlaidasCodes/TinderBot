from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException
import time
import random

# Initializing the drivers and stuff
driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=driver_options)
driver.get(url="https://tinder.com/app/recs")

# Getting onto tinder (logging in through facebook, clicking a bunch of stuff)
time.sleep(1.5)
log_in_button = driver.find_element(By.LINK_TEXT, "Log in")
log_in_button.click()
time.sleep(random.uniform(0.5, 0.9))

fb_log_in_button = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/"
                                                 "div[2]/button/div[2]/div[2]/div/div")
fb_log_in_button.click()
time.sleep(random.uniform(1.5, 3.0))
driver.switch_to.window(driver.window_handles[1])
accept_cookies = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div/div/div[4]/button[2]")
accept_cookies.click()
time.sleep(random.uniform(0.5, 1.2))
fb_email = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[1]/div/input")
fb_email.send_keys("EMAIL")
time.sleep(random.uniform(0.1, 1.0))
fb_pw = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[2]/div/input")
fb_pw.send_keys("PASSWORD", Keys.ENTER)
time.sleep(random.uniform(7.0, 9.0))
driver.switch_to.window(driver.window_handles[0])
allow_location_button = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[1]/div/div/div[3]/button[1]/div[2]/"
                                                      "div[2]")
allow_location_button.click()
not_interested_button = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[1]/div/div/div[3]/button[2]"
                                                      "/div[2]/div[2]")
not_interested_button.click()
tinder_cookies_accept_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button"
                                                             "/div[2]/div[2]")
tinder_cookies_accept_button.click()
time.sleep(random.uniform(6.0, 7.5))
error_exists = True
like_button = None
# Swiping non-stop, overcoming the exception when there's a match
while error_exists:
    try:
        like_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]"
                                                    "/div/div[3]/div/div[4]/button/span/span")
        error_exists = False
    except NoSuchElementException:
        time.sleep(random.uniform(2.0, 3.0))
        print("No such link, waiting some time...")
while True:
    try:
        like_button.click()
        time.sleep(random.uniform(1.0, 3.0))
    except ElementClickInterceptedException:
        dismiss_match = driver.find_element(By.LINK_TEXT, "BACK TO TINDER")
        time.sleep(random.uniform(2.5, 3.5))
