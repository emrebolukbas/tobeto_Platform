from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
import openpyxl
from constants import globalConstants as c

class Test_tobetoWelcomePanel():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()
        self.signup_button_check()

    def teardown_method(self):
        self.driver.quit()

    #1) Kullanıcı "Henüz üye değil misin? Kayıt ol" kısmına tıkladığında ‘’https://tobeto.com/kayit-ol’’ sayfasına gidilebilmesi test edilecektir.
    def signup_button_check(self):
        signUpButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_BUTTON)))
        signUpButton.click()
        sleep(1)
        signUpText = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/div/form/h3"))).text
        assert "Hemen Kayıt Ol" in signUpText 

    #2) Kullanıcının istenilen bilgiler doğrultusunda (Ad,Soyad,E-posta,Şifre,Şifre Tekrar) alanları doldurulup sisteme başarılı şekilde kayıt olma işlemi test edilecektir.
    def test_signup_successful(self):
        nameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_NAME)))
        nameInput.send_keys("1")
        surNameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_SURNAME)))
        surNameInput.send_keys("2")
        emailInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_EMAIL)))
        emailInput.send_keys("34@gc.com")
        passwordInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_PASSWORD)))
        passwordInput.send_keys("123456")
        passwordAgainInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_PASSWORD_AGAIN)))
        passwordAgainInput.send_keys("123456")
        signUpButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CONTINUE)))
        signUpButton.click()
        signUpContract = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CONTRACT))).text
        sleep (1)
        assert "Kayıt oluşturmak için gerekli sözleşmeler" in signUpContract

        checkbox1 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CHECKBOX_1)))
        checkbox1.click()
        checkbox2 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CHECKBOX_2)))
        checkbox2.click()
        checkbox3 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CHECKBOX_3)))
        checkbox3.click()
        checkbox4 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CHECKBOX_4)))
        checkbox4.click()
        phoneNumberInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_PHONE)))
        phoneNumberInput.send_keys("5553332211")
        captcha = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CAPTCHA)))
        captcha.click()
        sleep(10)
        finishButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_FINISH)))
        finishButton.click()
        signUpCheck = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div/div/span"))).text
        sleep(1) 
        assert "Tobeto Platform'a kaydınız başarıyla gerçekleşti." in signUpCheck

    #3) Kullanıcının istenilen bilgiler doğrultusunda şifre alanına 6 karakterden az doldurup sisteme kayıt olma işlemi test edilecektir.
    def test_signup_unsuccessful_missing_password(self):
        nameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_NAME)))
        nameInput.send_keys("1")
        surNameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_SURNAME)))
        surNameInput.send_keys("2")
        emailInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_EMAIL)))
        emailInput.send_keys("34@gc.com")
        passwordInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_PASSWORD)))
        passwordInput.send_keys("1234")
        passwordAgainInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_PASSWORD_AGAIN)))
        passwordAgainInput.send_keys("1234")
        signUpButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CONTINUE)))
        signUpButton.click()
        signUpContract = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CONTRACT))).text
        sleep (1)
        assert "Kayıt oluşturmak için gerekli sözleşmeler" in signUpContract

        checkbox1 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CHECKBOX_1)))
        checkbox1.click()
        checkbox2 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CHECKBOX_2)))
        checkbox2.click()
        checkbox3 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CHECKBOX_3)))
        checkbox3.click()
        checkbox4 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CHECKBOX_4)))
        checkbox4.click()
        phoneNumberInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_PHONE)))
        phoneNumberInput.send_keys("5553332211")
        captcha = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CAPTCHA)))
        captcha.click()
        sleep(10)
        finishButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_FINISH)))
        finishButton.click()
        systemMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SYSTEM_MESSAGE))).text
        sleep(1) 
        assert "Şifreniz en az 6 karakterden oluşmalıdır." in systemMessage
        
        #4) Kullanıcının istenilen bilgiler doğrultusunda (Ad,Soyad,E-posta,Şifre,Şifre Tekrar) alanları hatalı doldurulup sisteme kayıt olma işlemi test edilecektir.

    #4) Kullanıcının istenilen bilgiler doğrultusunda alanları hatalı doldurulup sisteme kayıt olma işlemi test edilecektir.
    def test_signup_unsuccessful_double_error(self):
        nameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_NAME)))
        nameInput.send_keys("1")
        surNameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_SURNAME)))
        surNameInput.send_keys("2")
        emailInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_EMAIL)))
        emailInput.send_keys("34@gc.com")
        passwordInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_PASSWORD)))
        passwordInput.send_keys("123456")
        passwordAgainInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_PASSWORD_AGAIN)))
        passwordAgainInput.send_keys("123456")
        signUpButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CONTINUE)))
        signUpButton.click()
        signUpContract = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CONTRACT))).text
        sleep (1)
        assert "Kayıt oluşturmak için gerekli sözleşmeler" in signUpContract

        checkbox1 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CHECKBOX_1)))
        checkbox1.click()
        checkbox2 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CHECKBOX_2)))
        checkbox2.click()
        checkbox3 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CHECKBOX_3)))
        checkbox3.click()
        checkbox4 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CHECKBOX_4)))
        checkbox4.click()
        phoneNumberInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_PHONE)))
        phoneNumberInput.send_keys("5553332211")
        captcha = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CAPTCHA)))
        captcha.click()
        sleep(10)
        finishButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_FINISH)))
        finishButton.click()
        systemMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SYSTEM_MESSAGE))).text
        sleep(1) 
        assert "Girdiğiniz e-posta adresi ile kayıtlı üyelik bulunmaktadır." in systemMessage

    #5) Kullanıcının istenilen bilgiler doğrultusunda şifreleri farklı doldurulup sisteme kayıt olma işlemi test edilecektir.
    def test_signup_unsuccessful_diffrent_password(self):
        nameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_NAME)))
        nameInput.send_keys("1")
        surNameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_SURNAME)))
        surNameInput.send_keys("2")
        emailInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_EMAIL)))
        emailInput.send_keys("34@gc.com")
        passwordInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_PASSWORD)))
        passwordInput.send_keys("1234")
        passwordAgainInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_PASSWORD_AGAIN)))
        passwordAgainInput.send_keys("12345")
        signUpButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CONTINUE)))
        signUpButton.click()
        signUpContract = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CONTRACT))).text
        sleep (1)
        assert "Kayıt oluşturmak için gerekli sözleşmeler" in signUpContract

        checkbox1 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CHECKBOX_1)))
        checkbox1.click()
        checkbox2 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CHECKBOX_2)))
        checkbox2.click()
        checkbox3 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CHECKBOX_3)))
        checkbox3.click()
        checkbox4 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CHECKBOX_4)))
        checkbox4.click()
        phoneNumberInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_PHONE)))
        phoneNumberInput.send_keys("5553332211")
        captcha = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CAPTCHA)))
        captcha.click()
        sleep(10)
        finishButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_FINISH)))
        finishButton.click()
        systemMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SYSTEM_MESSAGE))).text
        sleep(1) 
        assert "Şifreler eşleşmedi." in systemMessage
    

    #6) Kullanıcının eksik telefon numarası girerek sisteme kayıt olma işlemi test edilecektir.
    def test_signup_missing_phoneNumber(self):
        nameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_NAME)))
        nameInput.send_keys("1")
        surNameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_SURNAME)))
        surNameInput.send_keys("2")
        emailInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_EMAIL)))
        emailInput.send_keys("34@gc.com")
        passwordInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_PASSWORD)))
        passwordInput.send_keys("1234")
        passwordAgainInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_PASSWORD_AGAIN)))
        passwordAgainInput.send_keys("12345")
        signUpButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CONTINUE)))
        signUpButton.click()
        signUpContract = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CONTRACT))).text
        sleep (1)
        assert "Kayıt oluşturmak için gerekli sözleşmeler" in signUpContract

        checkbox1 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CHECKBOX_1)))
        checkbox1.click()
        checkbox2 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CHECKBOX_2)))
        checkbox2.click()
        checkbox3 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CHECKBOX_3)))
        checkbox3.click()
        checkbox4 = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_CHECKBOX_4)))
        checkbox4.click()
        phoneNumberInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_PHONE)))
        phoneNumberInput.send_keys("55533")
        mandatoryAreaText = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div/div/div/label[4]/small/p"))).text
        sleep(1) 
        assert "En az 10 karakter girmelisiniz." in mandatoryAreaText

    #7) Kullanıcının kayıt ol formuna geçersiz eposta girme işlemi test edilecektir.
    def test_signup_invalid_mail(self):
        emailInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_EMAIL)))
        emailInput.send_keys("test")
        mandatoryAreaText = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/div/form/p"))).text
        sleep(1) 
        assert "Geçersiz e-posta adresi" in mandatoryAreaText

    #8) Kullanıcının istenilen bilgiler doğrultusunda (Ad,Soyad,Şifre,Şifre Tekrar) alanları boş bırakılıp uyarı alma işlemi test edilecektir.
    def test_signup_passing_empty(self):
        nameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_NAME)))
        nameInput.send_keys("1")
        nameInput.clear()
        nameMardatory = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/div/form/p[1]")))
        surNameInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_SURNAME)))
        surNameInput.send_keys("2")
        surNameInput.clear()
        surNameMardatory = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/div/form/p[2]")))
        sleep(1)
        assert "Doldurulması zorunlu alan" in nameMardatory and surNameMardatory

    #9) Kullanıcının istenilen bilgiler doğrultusunda (E-posta) alanı girilip silinmesi test edilecektir.
    def test_signup_passing_empty_mail(self):
        emailInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.SIGN_UP_EMAIL)))
        emailInput.send_keys("test")
        emailInput.clear()
        mailMardatory = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/div/form/p[3]")))
        sleep(1)
        assert "Doldurulması zorunlu alan" in mailMardatory