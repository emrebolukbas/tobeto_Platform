from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from constants import globalConstants as c

class Test_contact_form_Testing():

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/giris")
        self.driver.maximize_window()
        self.successful_login()
    
    def teardown_method(self):
        self.driver.quit()

    def successful_login(self):     
        email_input = WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/main/section/div/div/div/div/form/input[1]")))
        email_input.send_keys("johiked454@telvetto.com")
        password_input = WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/main/section/div/div/div/div/form/input[2]")))
        password_input.send_keys("basariligiris")
        login_button = WebDriverWait(self.driver, 4).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button")))
        login_button.click()
        signUpText = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/div[2]/div/div[2]"))).text
        assert ("Giriş başarılı") in signUpText 
        
        #Bize Ulaşın butonu 
    def test_contact_form(self):
        contact_button = WebDriverWait(self.driver, 4).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/section/div/div/div[2]/ul/li/a")))
        self.driver.execute_script("window.scrollBy(0, 500);")
        sleep(3)
        # Butona tıkla
        contact_button.click()
        sleep(1)
       # Adınız alanını bul ve doldur
        name_surname_field = WebDriverWait(self.driver, 4).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[3]/section/div[3]/div/div[2]/div/form/input[1]")))
        name_surname_field.send_keys('Johi Ked')
       # E-mail alanını bul ve doldur
        email_field = WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[3]/section/div[3]/div/div[2]/div/form/input[2]")))
        email_field.send_keys("johiked454@telvetto.com")
       # Mesajınız alanını bul ve doldur
        message_field = WebDriverWait(self.driver, 4).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[3]/section/div[3]/div/div[2]/div/form/textarea")))
        message_field.send_keys('Merhaba Tobeto')
        self.driver.execute_script("window.scrollBy(0, 200);")
        iframe = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_IFRAME_XPATH)))
        self.driver.switch_to.frame(iframe)
        captcha = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CAPTCHA)))
        captcha.click()
        sleep(60)
        self.driver.switch_to.default_content()
       # Gönder butonunu bul ve tıkla
        send_button = WebDriverWait(self.driver, 4).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[3]/section/div[3]/div/div[2]/div/form/button")))
        send_button.click()
          #Gönderildi uyarı mesajı 
         # Uyarı mesajının metnini al
        signUpText = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div"))).text
        assert ("İletişim formu başarıyla gönderilmiştir.") in signUpText 
        sleep(1)

    # İsim Soy isim alanına sayısal değer girilerek formun gönderilmesi test edilecektir.
    def test_send_with_intChar_form(self):
        contact_button = WebDriverWait(self.driver, 4).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/section/div/div/div[2]/ul/li/a")))
        self.driver.execute_script("window.scrollBy(0, 500);")
        sleep(3)
        # Butona tıkla
        contact_button.click()
        sleep(1)
       # Adınız alanını bul ve doldur
        name_surname_field = WebDriverWait(self.driver, 4).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[3]/section/div[3]/div/div[2]/div/form/input[1]")))
        name_surname_field.send_keys('1')
       # E-mail alanını bul ve doldur
        email_field = WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[3]/section/div[3]/div/div[2]/div/form/input[2]")))
        email_field.send_keys("johiked454@telvetto.com")
       # Mesajınız alanını bul ve doldur
        message_field = WebDriverWait(self.driver, 4).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[3]/section/div[3]/div/div[2]/div/form/textarea")))
        message_field.send_keys('Merhaba Tobeto')
        self.driver.execute_script("window.scrollBy(0, 200);")
        iframe = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_IFRAME_XPATH)))
        self.driver.switch_to.frame(iframe)
        captcha = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CAPTCHA)))
        captcha.click()
        sleep(60)
        self.driver.switch_to.default_content()
       # Gönder butonunu bul ve tıkla
        send_button = WebDriverWait(self.driver, 4).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[3]/section/div[3]/div/div[2]/div/form/button")))
        send_button.click()
          #Gönderildi uyarı mesajı 
         # Uyarı mesajının metnini al
        signUpText = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div"))).text
        assert ("Geçersiz Karakter Girişi.") in signUpText
        #Gerçekleşen Sonuç: İsim Soy isim alanına sayısal değer girildiğinde formun gönderilmesi başarılı bir şekilde gerçekleşmiştir. 
        sleep(1)


