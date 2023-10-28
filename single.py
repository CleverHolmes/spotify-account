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

threads = []

headless = True

proxy_server = "http://49fcb87045f3a57acb4b6f0983876ce4caea018d:autoparse=true@proxy.zenrows.com"
proxy_port = 8001

domain = '@westside.com.ng'

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
        up_letters = string.ascii_uppercase
        low_num_letters = string.ascii_lowercase + string.digits
        num = string.digits

        gender_list = ['gender_option_male', 'gender_option_female', 'gender_option_non_binary', 'gender_option_other', 'gender_option_prefer_not_to_say']

        self.api = 'efad4a1d9c2b6d35313f22d3d67195b4'
        self.email = ''.join(random.choice(low_letters) for _ in range(8)) + ''.join(random.choice(num) for _ in range(4))
        self.pwd = ''.join(random.choice(low_letters) for _ in range(4)) + ''.join(random.choice(up_letters) for _ in range(4)) + ''.join(random.choice(num) for _ in range(4))
        self.username = ''.join(random.choice(low_letters) for _ in range(6)) + '_' + ''.join(random.choice(num) for _ in range(3))
        self.month = random.randint(1, 12)
        self.day = random.randint(1, 30)
        self.year = random.randint(1994, 2006)
        self.gender = gender_list[random.randint(0, 1)]

    def delay(self, driver, waiting_time=5):
        driver.implicitly_wait(waiting_time)

    def bot(self):
        email.find_element(By.CSS_SELECTOR, 'button[id="btnCreateEmailAccount"]').click()
        print(f'account {self.index}: Create email')
        sleep(1)

        email.find_element(By.CSS_SELECTOR, 'input[id="txtUserName"]').send_keys(self.email)
        print(f'account {self.index}: Input cpanel email -> {self.email}')
        sleep(1)

        email.find_element(By.CSS_SELECTOR, 'input[id="txtEmailPassword"]').send_keys(self.pwd)
        print(f'account {self.index}: Input cpanel pwd -> {self.pwd}')
        sleep(1)

        email.find_element(By.CSS_SELECTOR, 'button[spinner-id="spinnerCreateEmail"]').click()
        print(f'account {self.index}: Input submit email')
        sleep(1)

        options = Options()

        options.add_argument(f'--proxy-server=https://{proxy_server}:{proxy_port}')

        global headless
        if headless:
            options.add_argument('--headless')

        print(f'account {self.index}: Start')

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://www.spotify.com/signup")

        driver.find_element(By.ID, 'username').send_keys(self.email + domain)
        print(f'account {self.index}: Input email -> {self.email}')
        sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'button[data-testid="submit"]').click()
        print(f'account {self.index}: Next')
        sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'input[id="new-password"]').send_keys(self.pwd)
        print(f'account {self.index}: Input password -> {self.pwd}')
        sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'button[data-testid="submit"]').click()
        print(f'account {self.index}: Next')
        sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'input[name="displayName"]').send_keys(self.username)
        print(f'account {self.index}: Input username -> {self.username}')
        # sleep(1)

        driver.find_element(By.CSS_SELECTOR, f'option[value="2"]').click()
        # sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'input[id="day"]').send_keys(self.month)
        print(f'account {self.index}: Input month -> {self.month}')
        # sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'input[id="year"]').send_keys(self.year)
        print(f'account {self.index}: Input year -> {self.year}')
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

        driver.switch_to.frame(0)
        sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'div[class="recaptcha-checkbox-border"]').click()
        print(f'account {self.index}: Checked button')
        sleep(3)
        
        driver.switch_to.default_content()
        sleep(1)

        status = driver.find_element(By.CSS_SELECTOR, 'textarea[id="g-recaptcha-response"]').get_attribute("value")
        if status == "":
        # -------------------------
            print(f'account {self.index}: Unpassed')

            driver.switch_to.frame(2)
            self.delay(driver, 1)
            
            driver.find_element(By.CSS_SELECTOR, 'button[id="recaptcha-audio-button"]').click()
            print(f'account {self.index}: Audio button')
            self.delay(driver, 1)

            src = driver.find_element(By.ID, 'audio-source').get_attribute('src')
            name = "audio"
            path_to_mp3 = os.path.normpath(os.path.join(os.getcwd(), f"{name}.mp3"))
            path_to_wav = os.path.normpath(os.path.join(os.getcwd(), f"{name}.wav"))
            file_name = str(name) + ".mp3"     

            with open(file_name, "wb") as file:         # open in binary mode 
                response = requests.get(src)            # get request 
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

            driver.find_element(By.CSS_SELECTOR, 'input[id="audio-response"]').send_keys(key)
            print(f'account {self.index}: Answer input ({key})')
            self.delay(driver, 1)

            driver.find_element(By.CSS_SELECTOR, 'button[id="recaptcha-verify-button"]').click()
            print(f'account {self.index}: Captcha verify')
            self.delay(driver, 5)

            driver.switch_to.default_content()
            sleep(1)
        # ---------------------------

        driver.find_element(By.CSS_SELECTOR, 'button[data-encore-id="buttonPrimary"]').click()
        print(f'account {self.index}: Submit')
        sleep(5)

        driver.quit()
        print(f'account {self.index}: Finished')

        if os.path.exists(path_to_mp3):
            os.remove(path_to_mp3)
            os.remove(path_to_wav)
        
        file_name = "result.txt"

        data = f'{self.email}{domain}:{self.pwd}'
        if os.path.exists(file_name):
            with open(file_name, 'a') as file:
                file.write(f"{data}\n")

        else:
            with open(file_name, 'w') as file:
                file.write(f"{data}\n")

def inq():
    questions = [
        inquirer.List(
            'menu',
            message="What mode are you running your bot",
            choices=[
                "no-headless: show the current status of creating account",
                "headless: hide the current status of creating account"
                ],
        ),
    ]

    answers = inquirer.prompt(questions)
    selected_option = answers['menu']
    global headless
    if selected_option == "no-headless: show the current status of creating account":
        headless = False
    else:
        headless = True

def run(index):
    account = spotify(index)

inq()

user_input = input("Please enter a value: ")

email_options = Options()
email_options.add_argument(f'--proxy-server=https://{proxy_server}:{proxy_port}')

if headless:
    email_options.add_argument('--headless')
email = webdriver.Chrome(options=email_options)
email.maximize_window()
email.get("https://rbx115.truehost.cloud:2083/")

email.find_element(By.CSS_SELECTOR, 'input[name="user"]').send_keys('westsid2')
sleep(1)

email.find_element(By.CSS_SELECTOR, 'input[name="pass"]').send_keys('#JbOo2an!3EO37')
sleep(1)

email.find_element(By.CSS_SELECTOR, 'button[name="login"]').click()
sleep(1)

email.find_element(By.CSS_SELECTOR, 'a[id="item_email_accounts"]').click()
sleep(1)

for i in range(int(user_input)):
    try:
        run(i)

    except KeyboardInterrupt:
        print("User stopped")
        break

    except Exception as e:
        print(e)
        continue