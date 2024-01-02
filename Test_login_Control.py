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

class Test_tobetoPlatformLogin():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()

    def teardown_metahod(self):
        self.driver.quit()
    
    def getData():
        excel = openpyxl.load_workbook("data/invlalidLogin.xlsx")
        sheet = excel["Sheet1"]
        rows = sheet.max_row
        data = []
        for i in range(2,rows+1):
            username = sheet.cell(i,1).value
            password = sheet.cell(i,2).value
            data.append((username,password))

        return data
     

    def test_email_password_passing_empty(self):
        eMail = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.E_MAIL_XPATH)))
        eMail.send_keys("")
        password = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.PASSWORD_XPATH)))
        password.send_keys("")    
        loginButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.LOGIN_BUTTON_XPATH)))
        loginButton.click()
        errorMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.MANDATORY_FIELD_XPATH)))
        assert errorMessage.text == "Doldurulması zorunlu alan*"
    
    