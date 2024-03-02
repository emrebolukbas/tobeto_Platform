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

class Test_resetPassword():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    #1) Kullanıcının şifremi unuttum butonuna  tıklayarak  ‘’ Şifremi Unuttum ’’ sayfasında geçerli e-posta ile kullanıcının şifre sıfırlaması test edilecektir.
    def test_valid_reset_password(self):
        forgotPassword = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/label/small/p")))
        forgotPassword.click()
        current_url = self.driver.current_url
        expected_url = "https://tobeto.com/sifremi-unuttum"
        if (current_url and expected_url):
            True
        else:
            False
        resetPasswordInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/input")))
        resetPasswordInput.send_keys("test@tobeto.com")
        sendButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/button")))
        sendButton.click()
        systemMessage = WebDriverWait(self.driver,2).until(ec.presence_of_element_located((By.XPATH,c.SYSTEM_MESSAGE)))

        assert "Şifre sıfırlama linkini e-posta adresinize gönderdik. Lütfen gelen kutunuzu kontrol edin." in systemMessage.text

    #2) Kullanıcının platformda kayıtlı olmayan rastgele bir e-posta ile şifre sıfırlaması test edilecektir.
    def test_withRandomMail_reset_password(self):
        forgotPassword = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/label/small/p")))
        forgotPassword.click()
        current_url = self.driver.current_url
        expected_url = "https://tobeto.com/sifremi-unuttum"
        if (current_url and expected_url):
            True
        else:
            False
        resetPasswordInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/input")))
        resetPasswordInput.send_keys("123fd1s3fsfa@test1323eq.deneme")
        sendButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/button")))
        sendButton.click()
        systemMessage = WebDriverWait(self.driver,2).until(ec.presence_of_element_located((By.XPATH,c.SYSTEM_MESSAGE)))

        assert "Girmiş olduğunuz e-posta adresine ait bir kayıt bulunamadı." in systemMessage.text
        #Gerçekleşen Sonuç: Şifre sıfırlama linkini e-posta adresinize gönderdik. Lütfen gelen kutunuzu kontrol edin. Rastgele mail dışında sadece mail kurallarına yazılan herşey mail olarak algılanmakta ve mail gönderimi gerçekleşmektedir. 
    
    #3) Kullanıcının şifremi unuttum butonuna  tıklayarak  ‘’ https://tobeto.com/sifremi-unuttum’’ sayfasında geçersiz e-posta ile kullanıcının şifre sıfırlaması test edilecektir.
    def test_invalid_reset_password(self):
        forgotPassword = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/label/small/p")))
        forgotPassword.click()
        current_url = self.driver.current_url
        expected_url = "https://tobeto.com/sifremi-unuttum"
        if (current_url and expected_url):
            True
        else:
            False
        resetPasswordInput = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/input")))
        resetPasswordInput.send_keys("test.tobeto.com")
        sendButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div/button")))
        sendButton.click()
        systemMessage = WebDriverWait(self.driver,2).until(ec.presence_of_element_located((By.XPATH,c.SYSTEM_MESSAGE)))

        assert "Girdiğiniz e-posta geçersizdir." in systemMessage.text 


        


                                                                

        



        
        