from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from capmonster_python import RecaptchaV2Task
import inquirer
import os
from time import sleep
from time import time
import random
import string
import threading
import sys

threads = []

headless = True

proxy_server = "http://49fcb87045f3a57acb4b6f0983876ce4caea018d:autoparse=true@proxy.zenrows.com"
proxy_port = 8001

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

        options.add_argument(f'--proxy-server=https://{proxy_server}:{proxy_port}')

        global headless
        if headless:
            options.add_argument('--headless')

        print(f'account {self.index}: Start')

        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://www.spotify.com/signup")

        driver.find_element(By.ID, 'username').send_keys(self.email)
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

        website_url = driver.current_url
        iframe = driver.find_element(By.CSS_SELECTOR, 'div[class="g-recaptcha"]')
        website_key = iframe.get_attribute('data-sitekey')

        capmonster = RecaptchaV2Task(self.api)
        task_id = capmonster.create_task(website_url, website_key, no_cache=True)
        result = capmonster.join_task_result(task_id).get('gRecaptchaResponse')
        print(f'account {self.index}: Received result')
        print(result)
        driver.execute_script(f"document.querySelector('#g-recaptcha-response').value = '{result}';")

        driver.switch_to.frame(0)
        sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'div[class="recaptcha-checkbox-border"]').click()
        sleep(1)

        driver.switch_to.default_content()
        sleep(1)
        
        driver.find_element(By.CSS_SELECTOR, 'button[data-encore-id="buttonPrimary"]').click()
        sleep(5)
        driver.quit()
        print(f'account {self.index}: Finished')
        
        file_name = "result.txt"

        data = f'{self.email}:{self.pwd}'
        if os.path.exists(file_name):
            with open(file_name, 'a') as file:
                file.write(f"{data}\n")

        else:
            with open(file_name, 'w') as file:
                file.write(f"{data}\n")
def custom_excepthook(exctype, value, traceback):
    print(f"Exception of type {exctype} occurred with value {value}")

sys.excepthook = custom_excepthook

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

try:
    for i in range(int(user_input)):
        thread = threading.Thread(target=run,args=(i,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

except:
    print("User stopped")

