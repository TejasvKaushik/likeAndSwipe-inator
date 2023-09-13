import time
import os
import bumble.secrets as secrets
from selenium import webdriver
from selenium.webdriver.common.by import By

class BumbleBot(webdriver.Chrome):
    def __init__(self, driver_path=r"D:\Projects\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(BumbleBot, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(secrets.BASE_URL)

    def dismissCookies(self):
        xButton = self.find_element(By.XPATH, '/html/body/aside/div/button')
        xButton.click()

    def clickSignIn(self):
        signInButton = self.find_element(By.XPATH, '/html/body/div[2]/div/div/main/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/a')

        print("sign in button found")
        signInButton.click()
        print("sign in button clicked")

    def loginWithFB(self):
        main_window = self.current_window_handle

        loginWithFBbutton = self.find_element(By.XPATH, '/html/body/div/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[2]/div')

        print("login with fb button found")
        loginWithFBbutton.click()
        print("login with fb button clicked")

        for handle in self.window_handles:
            if handle != main_window:
                popup = handle
                self.switch_to.window(popup)

        username = self.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
        username.send_keys(secrets.FB_EMAIL)
        print("Username used")

        # time.sleep(2)

        password = self.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
        password.send_keys(secrets.FB_PASSWORD)
        print("Password used")

        loginButton = self.find_element(By.XPATH, '/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
        print("final login button found")
        loginButton.click()
        print("final login button clicked")

        self.switch_to.window(main_window)

    def like(self):
        try:
                                                    # /html/body/div/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[2]/div
                                                    # /html/body/div/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[2]/div/div[1]/span
            # likeButton = self.find_element(By.XPATH, '/html/body/div/div/div[1]/main/div[2]/div/div/span/div[contains[@class, "encounters-user__controls"]]/div/div[2]/div/div[2]/div')
            likeButton = self.find_element(By.XPATH, '/html/body/div/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[2]/div/div[1]/span')
            print("like button found")
            likeButton.click()
            print("like button clicked")

            time.sleep(2)
        except Exception as e:
            print(e)



