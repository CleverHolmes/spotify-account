from selenium import webdriver
from selenium_recaptcha_solver import RecaptchaSolver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
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
# import speech_recognition as sr
from capmonster_python import RecaptchaV2Task
import threading

from capmonstercloudclient import CapMonsterClient, ClientOptions
from capmonstercloudclient.requests import RecaptchaV2ProxylessRequest

client_options = ClientOptions(api_key='efad4a1d9c2b6d35313f22d3d67195b4')
cap_monster_client = CapMonsterClient(options=client_options)

num_thread = 2

threads = []

proxy_server = "4g.hydraproxy.com"
proxy_port = 3121

class spotify:
    def __init__(self, index):
        self.index = index
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
        options = Options()

        # test_ua = 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'
        # options.add_argument("--headless")  # Remove this if you want to see the browser (Headless makes the chromedriver not have a GUI)
        # options.add_argument(f'--user-agent={test_ua}')
        # options.add_argument('--no-sandbox')
        # options.add_argument("--disable-extensions")
        # options.add_argument(f'--proxy-server=http://{proxy_server}:{proxy_port}')

        print('start')
        driver = webdriver.Chrome()
        driver.maximize_window()
        # solver = RecaptchaSolver(driver=driver)
        driver.get("https://www.spotify.com/signup")

        driver.find_element(By.ID, 'username').send_keys(self.email)
        print(f'account {self.index}: Input email')
        sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'button[data-testid="submit"]').click()
        print(f'account {self.index}: Next')
        sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'input[id="new-password"]').send_keys(self.pwd)
        print(f'account {self.index}: Input password')
        sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'button[data-testid="submit"]').click()
        print(f'account {self.index}: Next')
        sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'input[name="displayName"]').send_keys(self.username)
        print(f'account {self.index}: Input username')
        # sleep(1)

        driver.find_element(By.CSS_SELECTOR, f'option[value="2"]').click()
        # sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'input[id="day"]').send_keys(self.month)
        print(f'account {self.index}: Input month')
        # sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'input[id="year"]').send_keys(self.year)
        print(f'account {self.index}: Input year')
        # sleep(1)

        driver.find_element(By.CSS_SELECTOR, f'label[for={self.gender}]').click()
        print(f'account {self.index}: Input gender')
        # sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'button[data-testid="submit"]').click()
        print(f'account {self.index}: Next')
        sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'button[data-testid="submit"]').click()
        print(f'account {self.index}: Next')
        while driver.current_url == 'https://www.spotify.com/us/signup#step=3':
            sleep(2)
        sleep(5)

# delay
        website_url = driver.current_url
        iframe = driver.find_element(By.CSS_SELECTOR, 'div[class="g-recaptcha"]')
        website_key = iframe.get_attribute('data-sitekey')

        # solver.click_recaptcha_v2(iframe=iframe)
# -------------------
        # capmonster = RecaptchaV2Task(self.api)
        # task_id = capmonster.create_task(website_url, website_key, no_cache=True)
        # result = capmonster.join_task_result(task_id).get('gRecaptchaResponse')
        # print(result)
        # driver.execute_script(f"document.querySelector('#g-recaptcha-response').value = '{result}';")
        # ---------------------------
        # recaptcha2request = RecaptchaV2ProxylessRequest(websiteUrl=website_url,
        #                                                 websiteKey=website_key)

        # responses = asyncio.run(solve_captcha())
        # answer = responses['gRecaptchaResponse']
        # print(answer)

        # print('here')
        # driver.find_element(By.CSS_SELECTOR, 'textarea[id="g-recaptcha-response"]').send_keys(answer)
# ------------------------------
        sleep(1000)
        driver.switch_to.frame(0)
        sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'div[class="recaptcha-checkbox-border"]').click()
        sleep(1)
        
        # driver.execute_script(f"document.querySelector('#g-recaptcha-response').value = '{answer}';")
        # sleep(10000)

        driver.switch_to.default_content()
        sleep(1)
        
        # driver.switch_to.frame(2)
        # sleep(1)

        # driver.find_element(By.CSS_SELECTOR, 'button[id="recaptcha-audio-button"]').click()
        # sleep(1)

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

def run(index):
    account = spotify(index)

for i in range(1):
    thread = threading.Thread(target=run,args=(i,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()


    