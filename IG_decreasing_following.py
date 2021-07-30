from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
#from webdriver_manager.microsoft import EdgeChromiumDriverManager


CHROME_DRIVER_PATH = "D:\\RITIK BAISLA\\Ritik\\web d\\Development\\chromedriver.exe"
USERNAME ="" #instagram username
PASSWORD = "" #account password


class Ig_dec_Following:

    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)


    def login(self, user, password):
        self.driver.get("https://www.instagram.com/")
        time.sleep(10)
        user_input = self.driver.find_element_by_name("username")
        user_input.send_keys(user)
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys(password)
        time.sleep(3)
        password_input.send_keys(Keys.ENTER)
        time.sleep(15)

    #this takes to users profile
    def profile(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]'
                                          '/div/div[5]/span/img').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div'
                                          '/div[5]/div[2]/div[2]/div[2]/a[1]').click()
        time.sleep(2)

    #this method is to get the number of accounts user follow
    def number_of_following(self):
        count_list = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div'
                                                 '/header/section/ul/li[3]/a/span').text.split(",")
        c =""
        for number in count_list:
            c = f"{c}{number}"
        count = int(c)
        print(count)
        return count

    def dec_following(self, count):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        time.sleep(5)
        self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

        pop_up_window = WebDriverWait(
            self.driver, 2).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='isgrP']")))

        #loads all the accounts in the popup
        for i in range(count):
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                pop_up_window
            )
            time.sleep(1)

        all_buttons = self.driver.find_elements_by_css_selector("li button")

        for button in all_buttons:
            button.click()
            time.sleep(2)
            self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]').click()
            time.sleep(2)

        time.sleep(60)
        self.driver.refresh()



account = Ig_dec_Following()
account.login(USERNAME, PASSWORD)
account.profile()
account.dec_following(int(account.number_of_following()))

