from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from capmonster_python import RecaptchaV2Task
import inquirer
import requests
import pydub
import speech_recognition as sr
import os
from time import sleep
from time import time
import random
import string
import threading
import sys
import datetime

# proxy_server = "http://49fcb87045f3a57acb4b6f0983876ce4caea018d:autoparse=true@proxy.zenrows.com"
# proxy_port = 8001

# options = Options()
# options.add_argument(f'--proxy-server=https://{proxy_server}:{proxy_port}')
# # global headless
# # if headless:
# #     options.add_argument('--headless')
# email = webdriver.Chrome(options=options)
# email.maximize_window()
# email.get("https://rbx115.truehost.cloud:2083/")

# email.find_element(By.CSS_SELECTOR, 'input[name="user"]').send_keys('westsid2')
# sleep(1)

# email.find_element(By.CSS_SELECTOR, 'input[name="pass"]').send_keys('#JbOo2an!3EO37')
# sleep(1)

# email.find_element(By.CSS_SELECTOR, 'button[name="login"]').click()
# sleep(1)

# email.find_element(By.CSS_SELECTOR, 'a[id="item_email_accounts"]').click()
# sleep(1)

# email.find_element(By.CSS_SELECTOR, 'button[id="btnCreateEmailAccount"]').click()
# sleep(1)

# email.find_element(By.CSS_SELECTOR, 'input[id="txtUserName"]').send_keys('thxbromillion')
# sleep(1)

# email.find_element(By.CSS_SELECTOR, 'input[id="txtEmailPassword"]').send_keys('thxbromillion')
# sleep(1)

# email.find_element(By.CSS_SELECTOR, 'button[spinner-id="spinnerCreateEmail"]').click()
# sleep(1)

# sleep(10000)

path_to_mp3 = os.path.normpath(os.path.join(os.getcwd(), f"audio.mp3"))

if os.path.exists(path_to_mp3):
    os.remove(path_to_mp3)
