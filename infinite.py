from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import pydub
import speech_recognition as sr
import os
from time import sleep
from time import time
import random
import string
import subprocess
import zipfile

domain = '@westside.com.ng'

license = "C:\\Users\\Public\\conf"

value = 1

if os.path.isfile(license):
    with open(license, 'r') as file:
        content = file.read()
    value = content.split('\n')[0]
    if value != '0':
        with open(license, 'w') as file:
            file.write(str(int(value) - 1))
else:
    content = "10\n"
    with open(license, 'w') as file:
        file.write(content)

try:
    with open('proxy.txt', 'r') as file:
        proxies = [line.strip() for line in file.readlines()]
except:
    input("Proxy error, add proxy to 'proxy.txt' file, Press Enter button to stop")


class spotify:
    def __init__(self, index):
        self.index = index
        self.proxy_gen()
        self.info_gen()
        self.bot()

    def proxy_gen(self):
        self.proxy = random.choice(proxies)
        proxyinfo = self.proxy.split(':')
        PROXY_HOST = proxyinfo[0]
        PROXY_PORT = proxyinfo[1]
        PROXY_USER = proxyinfo[2]
        PROXY_PASS = proxyinfo[3]
        manifest_json = """
        {
            "version": "1.0.0",
            "manifest_version": 2,
            "name": "Chrome Proxy",
            "permissions": [
                "proxy",
                "tabs",
                "unlimitedStorage",
                "storage",
                "<all_urls>",
                "webRequest",
                "webRequestBlocking"
            ],
            "background": {
                "scripts": ["background.js"]
            },
            "minimum_chrome_version":"22.0.0"
        }
        """

        background_js = """
        var config = {
                mode: "fixed_servers",
                rules: {
                singleProxy: {
                    scheme: "http",
                    host: "%s",
                    port: parseInt(%s)
                },
                bypassList: ["localhost"]
                }
            };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "%s",
                    password: "%s"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
                    callbackFn,
                    {urls: ["<all_urls>"]},
                    ['blocking']
        );
        """ % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)

        pluginfile = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)

    def info_gen(self):
        letters = string.ascii_lowercase + string.ascii_uppercase
        up_letters = string.ascii_uppercase
        num = string.digits

        gender_list = ['gender_option_male', 'gender_option_female',
                       'gender_option_non_binary', 'gender_option_other', 'gender_option_prefer_not_to_say']
        self.email = ''.join(random.choice(letters) for _ in range(
            12)) + ''.join(random.choice(num) for _ in range(6))
        self.pwd = ''.join(random.choice(letters) for _ in range(4)) + ''.join(random.choice(
            up_letters) for _ in range(4)) + ''.join(random.choice(num) for _ in range(4))
        self.username = ''.join(random.choice(letters) for _ in range(
            6)) + '_' + ''.join(random.choice(num) for _ in range(3))
        self.month = random.randint(1, 12)
        self.day = random.randint(1, 30)
        self.year = random.randint(1994, 2006)
        self.gender = gender_list[random.randint(0, 1)]

    def delay(self, driver, waiting_time=5):
        driver.implicitly_wait(waiting_time)

    def bot(self):
        try:
            print(f'''account {self.index}: Start
                
  /$$$$$$                        /$$     /$$  /$$$$$$          
 /$$__  $$                      | $$    |__/ /$$__  $$         
| $$  \__/  /$$$$$$   /$$$$$$  /$$$$$$   /$$| $$  \__//$$   /$$
|  $$$$$$  /$$__  $$ /$$__  $$|_  $$_/  | $$| $$$$   | $$  | $$
 \____  $$| $$  \ $$| $$  \ $$  | $$    | $$| $$_/   | $$  | $$
 /$$  \ $$| $$  | $$| $$  | $$  | $$ /$$| $$| $$     | $$  | $$
|  $$$$$$/| $$$$$$$/|  $$$$$$/  |  $$$$/| $$| $$     |  $$$$$$$
 \______/ | $$____/  \______/    \___/  |__/|__/      \____  $$
          | $$                                        /$$  | $$
          | $$                                       |  $$$$$$/
          |__/                                        \______/ 
                ''')
            options = Options()
            options.add_extension("proxy_auth_plugin.zip")
            driver = webdriver.Chrome(options=options)
            wait = WebDriverWait(driver, 20)
            driver.maximize_window()
            driver.get("http://51.83.2.241:2082/")

            element = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'input[name="user"]')))
            element.send_keys('westsid2')
            sleep(1)

            element = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'input[name="pass"]')))
            element.send_keys('#JbOo2an!3EO37')
            sleep(1)

            element = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button[name="login"]')))
            element.click()
            sleep(1)

            element = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'a[id="item_email_accounts"]')))
            element.click()
            sleep(1)

            element = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button[id="btnCreateEmailAccount"]')))
            element.click()
            print(f'account {self.index}: Create email')
            sleep(1)

            element = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'input[id="txtUserName"]')))
            element.send_keys(self.email)
            print(f'account {self.index}: Input cpanel email -> {self.email}')
            sleep(1)

            element = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'input[id="txtEmailPassword"]')))
            element.send_keys(self.pwd)
            print(f'account {self.index}: Input cpanel pwd -> {self.pwd}')
            sleep(1)

            element = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button[spinner-id="spinnerCreateEmail"]')))
            element.click()
            print(f'account {self.index}: Input submit email')
            sleep(1)

            driver.get("https://www.spotify.com/signup")

            element = wait.until(EC.element_to_be_clickable((By.ID, 'username')))
            element.send_keys(self.email + domain)
            print(f'account {self.index}: Input email -> {self.email}')
            sleep(1)

            try:
                driver.find_element(
                    By.CSS_SELECTOR, 'button[id="onetrust-accept-btn-handler"]').click()
                print(f'account {self.index}: Close modal')
                sleep(1)
            except NoSuchElementException:
                pass

            element = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button[data-testid="submit"]')))
            element.click()
            print(f'account {self.index}: Next')
            sleep(1)

            element = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'input[id="new-password"]')))
            element.send_keys(self.pwd)
            print(f'account {self.index}: Input password -> {self.pwd}')
            sleep(1)

            element = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button[data-testid="submit"]')))
            element.click()
            print(f'account {self.index}: Next')
            sleep(1)

            element = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'input[name="displayName"]')))
            element.send_keys(self.username)
            print(f'account {self.index}: Input username -> {self.username}')
            # sleep(1)

            element = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f'option[value="2"]')))
            element.click()
            # sleep(1)

            element = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'input[id="day"]')))
            element.send_keys(self.month)
            print(f'account {self.index}: Input month -> {self.month}')
            # sleep(1)

            element = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'input[id="year"]')))
            element.send_keys(self.year)
            print(f'account {self.index}: Input year -> {self.year}')
            # sleep(1)

            element = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f'label[for={self.gender}]')))
            element.click()
            print(f'account {self.index}: Input gender')
            # sleep(1)

            element = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button[data-testid="submit"]')))
            element.click()
            print(f'account {self.index}: Next')
            sleep(1)

            element = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'label[for="terms-conditions-checkbox"]')))
            element.click()
            print(f'account {self.index}: Check')
            sleep(1)

            current_url = driver.current_url

            element = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button[data-testid="submit"]')))
            element.click()
            print(f'account {self.index}: Next')

            while driver.current_url == current_url:
                sleep(2)

            sleep(5)

            driver.switch_to.frame(0)
            sleep(1)

            driver.find_element(
                By.CSS_SELECTOR, 'div[class="recaptcha-checkbox-border"]').click()
            print(f'account {self.index}: Checked button')
            sleep(3)

            driver.switch_to.default_content()
            sleep(1)

            status = driver.find_element(
                By.CSS_SELECTOR, 'textarea[id="g-recaptcha-response"]').get_attribute("value")
            if status == "":
                # -------------------------
                print(f'account {self.index}: Unpassed')

                driver.switch_to.frame(2)
                self.delay(driver, 1)

                element = wait.until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[id="recaptcha-audio-button"]')))
                element.click()
                print(f'account {self.index}: Audio button')
                self.delay(driver, 1)

                src = driver.find_element(
                    By.ID, 'audio-source').get_attribute('src')
                name = "audio"
                path_to_mp3 = os.path.normpath(
                    os.path.join(os.getcwd(), f"{name}.mp3"))
                path_to_wav = os.path.normpath(
                    os.path.join(os.getcwd(), f"{name}.wav"))

                with open(path_to_mp3, "wb") as file:
                    response = requests.get(src)
                    self.delay(driver, 1)

                    file.write(response.content)

                sound = pydub.AudioSegment.from_mp3(path_to_mp3)
                sound.export(path_to_wav, format="wav")
                sample_audio = sr.AudioFile(path_to_wav)
                print(f'account {self.index}: Audio downloaded')

                self.delay(driver, 5)
                r = sr.Recognizer()
                with sample_audio as source:
                    audio = r.record(source)
                key = r.recognize_google(audio)
                print(f'account {self.index}: Audio converted')

                element = wait.until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'input[id="audio-response"]')))
                element.send_keys(key)
                print(f'account {self.index}: Answer input ({key})')
                self.delay(driver, 1)

                element = wait.until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[id="recaptcha-verify-button"]')))
                element.click()
                print(f'account {self.index}: Captcha verify')
                self.delay(driver, 5)

                driver.switch_to.default_content()
                sleep(1)

                os.remove(path_to_mp3)
                os.remove(path_to_wav)
                print(f'account {self.index}: Remove audio files')

            # ---------------------------

            element = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button[data-encore-id="buttonPrimary"]')))
            element.click()
            print(f'account {self.index}: Submit')
            sleep(1)

            driver.quit()
            print(f'account {self.index}: Completed')
            file_name = "result.txt"

            data = f'{self.email}{domain}:{self.pwd}'
            if os.path.exists(file_name):
                with open(file_name, 'a') as file:
                    file.write(f"{data}\n")

            else:
                with open(file_name, 'w') as file:
                    file.write(f"{data}\n")

            print(f'account {self.index}: Saved')

            print(f'account {self.index}: Finished')

        except Exception:
            raise Exception('Bot is not running')


def run(index):
    spotify(index)


i = 0

if value != '0':
    while True:
        try:
            start_time = time()
            run(i)
            print(time() - start_time)
            i = i + 1


        except KeyboardInterrupt:
            print("User stopped")
            break

        except Exception:
            pass

else:
    print('You have no license')
    input('please press Enter key to finish')
