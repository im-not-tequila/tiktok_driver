import selenium.webdriver
import undetected_chromedriver as uc

from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.remote.webelement import WebElement

from webdriver_manager.chrome import ChromeDriverManager


class TiktokAuthorization:
    def __init__(self, login: str, password: str, profiles_directory: str):
        self.login = login
        self.password = password
        # self.proxy = proxy
        self.is_hide = False
        self.profiles_directory = profiles_directory
        self.implicitly_wait = 20.0
        self.window_size = (800, 1200)

    def _make_driver(self) -> uc.Chrome:
        # options = {
        #     # 'proxy': self.proxy
        # }
        profile_directory = f'{self.profiles_directory}/{self.login}'

        options = uc.ChromeOptions()
        options.add_argument(f"--user-data-dir={profile_directory}")

        if self.is_hide:
            options.add_argument("--headless")

        driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.implicitly_wait(self.implicitly_wait)
        driver.set_window_size(*self.window_size)

        return driver

    def google_auth(self) -> str:
        _tiktok_link = 'https://www.tiktok.com/'

        driver = self._make_driver()
        driver.get(_tiktok_link)

        sleep(5)

        try:
            login_button = driver.find_element(By.XPATH, "//button[@id='header-login-button']")
            login_button.click()
        except ElementClickInterceptedException:
            pass

        sleep(5)

        auth_type_buttons = driver.find_elements(By.XPATH, "//div[@data-e2e='channel-item']")

        is_clicked = False

        for button in auth_type_buttons:
            if 'Google' in button.text:
                button.click()
                is_clicked = True

                break

        if not is_clicked:
            raise NoSuchElementException

        sleep(5)

        windows = driver.window_handles
        driver.switch_to.window(windows[-1])

        # sleep(3)

        accounts_from_auth = driver.find_elements(By.XPATH, "//li")

        is_clicked = False

        for button in accounts_from_auth:
            if self.login in button.text:
                button.click()
                is_clicked = True

                break

        if not is_clicked:
            raise NoSuchElementException

        sleep(5)

        continue_button = driver.find_elements(By.XPATH, "//button")[-1]
        continue_button.click()

        sleep(30678)

        driver.quit()

        return f'{self.profiles_directory}/{self.login}'

    def email_auth(self):
        _tiktok_link = 'https://www.tiktok.com/'

        driver = self._make_driver()
        driver.get(_tiktok_link)

        sleep(5)

        try:
            login_button = driver.find_element(By.XPATH, "//button[@id='header-login-button']")
            login_button.click()
        except ElementClickInterceptedException:
            pass

        auth_type_buttons = driver.find_elements(By.XPATH, "//div[@data-e2e='channel-item']")

        is_clicked = False

        for button in auth_type_buttons:
            if 'почту' in button.text:
                button.click()
                is_clicked = True

                break

        if not is_clicked:
            raise NoSuchElementException

        sleep(5)

        email_auth_link = driver.find_element(By.XPATH, "//a[@href='/login/phone-or-email/email']")
        email_auth_link.click()

        sleep(5)

        email_input = driver.find_element(By.XPATH, "//input[@name='username']")
        email_input.send_keys(self.login)

        sleep(2)

        password_input = driver.find_element(By.XPATH, "//input[@type='password']")
        password_input.send_keys(self.password)

        password_input.send_keys(Keys.RETURN)


        sleep(400)

    def check_yt_authorization(self) -> bool:
        driver = self._make_driver()

        driver.get("https://www.youtube.com")

        sleep(5)

        try:
            driver.find_element(By.XPATH, '//a[@aria-label="Войти"]')
            return False
        except NoSuchElementException:
            return True

