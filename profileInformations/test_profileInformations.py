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

class Test_profileInformations():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()
        self.valid_login()

    def teardown_method(self):
        self.driver.quit()
    
    def valid_login(self):
        eMail = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.E_MAIL_XPATH)))
        eMail.send_keys("fogacap180@ubinert.com")
        Password = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.PASSWORD_XPATH)))
        Password.send_keys("abc123456")
        loginButton = self.driver.find_element(By.XPATH,c.LOGIN_BUTTON_XPATH)
        loginButton.click()
        systemMessage = WebDriverWait(self.driver,2).until(ec.presence_of_element_located((By.XPATH,"//*[@id='__next']/div/div[2]/div/div[2]")))
        current_url = self.driver.current_url
        expected_url = "https://tobeto.com/platform"
        assert  "Giriş başarılı." in systemMessage.text and current_url == expected_url
        closeSystemMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/div[2]/div/div[1]/button")))
        closeSystemMessage.click()
    
    #Kişisel Bilgilerim sayfasının görüntülenmesi test edilecektir.
    def test_myPersonel_Information_Check(self):
        profileImg = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button")))
        profileImg.click()
        myInformationButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")))
        myInformationButton.click()
        current_url = self.driver.current_url
        expected_url = "https://tobeto.com/profilim/profilimi-duzenle/kisisel-bilgilerim"
        assert current_url == expected_url

    #Sertifikalarım sayfasının görüntülenmesi test edilecektir.
    def test_myCertificates_Check(self):
        profileImg = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button")))
        profileImg.click()
        myInformationButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")))
        myInformationButton.click()
        myCertificates = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[5]")))
        myCertificates.click()
        current_url = self.driver.current_url
        expected_url = "https://tobeto.com/profilim/profilimi-duzenle/sertifikalarim"
        assert current_url == expected_url        