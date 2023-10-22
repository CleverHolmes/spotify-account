from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import requests
import json
import os
import datetime
from time import sleep
from time import time
import json
import asyncio
import random
import string
import pyaudio
import wave
import numpy as np
# import speech_recognition as sr

from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.requests import RecaptchaV2ProxylessRequest

client_options = ClientOptions(api_key='efad4a1d9c2b6d35313f22d3d67195b4')
cap_monster_client = CapMonsterClient(options=client_options)

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
OUTPUT_FILENAME = "output_audio.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=False,
                frames_per_buffer=CHUNK)

frames = []

class Captcha:
    def __init__(self, key, site_key, web_link):
        self.key = key
        self.web_link = web_link
        self.site_key = site_key

    def Get_id_fun(self):
        params = {
            "key": self.key,
            "method": "funcaptcha",
            "publickey": self.site_key,
            "surl": "https://client-api.arkoselabs.com",
            "pageurl": self.web_link,
            "json": 1
        }
        response = requests.get('http://2captcha.com/in.php',params=params).json()
        if response['status'] == 1 and 'request' in response: return response['request']

    def Get_id_re(self):
        params = {
            "key": self.key,
            "method": "userrecaptcha",
            "googlekey": self.site_key,
            "pageurl": self.web_link,
            "json": 1
        }
        response = requests.get('http://2captcha.com/in.php', params=params).json()
        if response['status'] == 1 and 'request' in response: return response['request']

    def Get_id(self, google):
        if google == True: id = self.Get_id_re()
        else: id = self.Get_id_fun()
        return id


    def Get_token(self, google=True, timing=60):
        try:
            id = self.Get_id(google)
            if not id: return
            start = time()
            while (time() - start) < timing:
                params = {
                    "key": self.key,
                    "action": "get",
                    "id": id,
                    "json": 1
                }
                response = requests.get('http://2captcha.com/res.php', params=params).json()
                if response['status'] != 1:
                    sleep(10)
                    if 'request' in response and response['request'] == 'ERROR_CAPTCHA_UNSOLVABLE': break
                    continue
                if 'request' in response: return response['request']
        except:
            pass

class spotify:
    def __init__(self):
        self.info_gen()
        self.bot()

    def email_gen(self):
        pass

    def info_gen(self):
        letters_num = string.ascii_letters + string.digits
        low_letters = string.ascii_lowercase
        low_num_letters = string.ascii_lowercase + string.digits
        num = string.digits

        gender_list = ['gender_option_male', 'gender_option_female', 'gender_option_non_binary', 'gender_option_other', 'gender_option_prefer_not_to_say']

        self.api = 'efad4a1d9c2b6d35313f22d3d67195b4'
        self.email = ''.join(random.choice(low_letters) for _ in range(8)) + ''.join(random.choice(num) for _ in range(4)) + '@gmail.com'
        self.pwd = ''.join(random.choice(letters_num) for _ in range(8))
        self.username = ''.join(random.choice(low_letters) for _ in range(6)) + '_' + ''.join(random.choice(num) for _ in range(3))
        self.month = random.randint(1, 12)
        self.day = random.randint(1, 30)
        self.year = random.randint(1994, 2006)
        self.gender = gender_list[random.randint(0, 1)]

    def bot(self):
        async def solve_captcha():
            return await cap_monster_client.solve_captcha(recaptcha2request)

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.spotify.com/signup")

        driver.find_element(By.ID, 'username').send_keys(self.email)
        sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'button[data-testid="submit"]').click()
        sleep(1)

        if driver.current_url == 'https://www.spotify.com/us/signup':
            print('repeat')

        driver.find_element(By.CSS_SELECTOR, 'input[id="new-password"]').send_keys(self.pwd)
        sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'button[data-testid="submit"]').click()
        sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'input[name="displayName"]').send_keys(self.username)
        # sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'option[value="2"]').click()
        # sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'input[id="day"]').send_keys(self.month)
        # sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'input[id="year"]').send_keys(self.year)
        # sleep(1)

        driver.find_element(By.CSS_SELECTOR, f'label[for={self.gender}]').click()
        # sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'button[data-testid="submit"]').click()
        sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'button[data-testid="submit"]').click()
        while driver.current_url == 'https://www.spotify.com/us/signup#step=3':
            sleep(2)
        sleep(5)
        # https://www.spotify.com/us/signup

# delay
        website_url = driver.current_url
        iframe = driver.find_element(By.CSS_SELECTOR, 'div[class="g-recaptcha"]')
        website_key = iframe.get_attribute('data-sitekey')

        recaptcha2request = RecaptchaV2ProxylessRequest(websiteUrl=website_url,
                                                        websiteKey=website_key)

        responses = asyncio.run(solve_captcha())
        answer = responses['gRecaptchaResponse']
        print(answer)

        print('here')
        # driver.find_element(By.CSS_SELECTOR, 'textarea[id="g-recaptcha-response"]').send_keys(answer)
# ------------------------------
        driver.switch_to.frame(0)
        sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'div[class="recaptcha-checkbox-border"]').click()
        sleep(1)
        
        # driver.execute_script(f"document.querySelector('#g-recaptcha-response').innerHTML = '{answer}';")
        # sleep(10000)

        driver.switch_to.default_content()
        sleep(1)
        
        driver.switch_to.frame(2)
        sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'button[id="recaptcha-audio-button"]').click()
        sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'button[aria-labelledby="audio-instructions rc-response-label"]').click()
        sleep(1)

        # driver.find_element(By.CSS_SELECTOR, 'button[aria-labelledby="audio-instructions rc-response-label"]').click()
        # --------------------------
        # recognizer = sr.Recognizer()

        # with sr.Microphone() as source:
        #     print("Please start speaking...")
        #     recognizer.adjust_for_ambient_noise(source)
        #     audio = recognizer.listen(source)

        # try:
        #     recognized_text = recognizer.recognize_google(audio)
        #     print(f"Recognized text: {recognized_text}")
        # except sr.UnknownValueError:
        #     print("Speech Recognition could not understand audio.")
        # except sr.RequestError as e:
        #     print(f"Could not request results from Google Speech Recognition service; {e}")
# -----------------------------
        # url = driver.current_url
        # iframe = driver.find_element(By.CSS_SELECTOR, 'div[class="g-recaptcha"]')
        # website_key = iframe.get_attribute('data-sitekey')
        # captcha = Captcha(self.api, website_key, url)
        # key = captcha.Get_token(False, 2000)
        # if not isinstance(key, str): return
        # driver.execute_script('''var anyCaptchaToken = arguments[0];
        # var enc = document.getElementById('enforcementFrame');
        # var encWin = enc.contentWindow || enc;
        # var encDoc = enc.contentDocument || encWin.document;
        # let script = encDoc.createElement('SCRIPT');
        # script.append('function AnyCaptchaSubmit(token) { parent.postMessage(JSON.stringify({ eventId: "challenge-complete", payload: { sessionToken: token } }), "*") }');
        # encDoc.documentElement.appendChild(script);
        # encWin.AnyCaptchaSubmit(anyCaptchaToken);''', key)
        # WebDriverWait(driver, 30).until(EC.url_changes(url))


        
        
        
        
        
        # sleep(1000)
        # captcha = driver.find_element(By.CSS_SELECTOR, 'div[class="recaptcha-checkbox-borderAnimation"]')
        # sleep(1)

        # ActionChains(driver).click(captcha).perform()
        # sleep(1)

        # driver.switch_to.default_content()
        # sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'button[data-encore-id="buttonPrimary"]').click()
        sleep(5)
        driver.quit()

account = spotify()

    