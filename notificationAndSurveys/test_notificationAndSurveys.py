from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.keys import Keys
import pytest

class Test_Notification:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/giris")
        self.driver.maximize_window()
        self.successful_login()
        
    def teardown_method(self): 
        self.driver.quit()

    def successful_login(self):
        emailInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[1]")))
        emailInput.send_keys("haceryalcnn@gmail.com")
        passwordInput = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/input[2]")))
        passwordInput.send_keys("Hy123456")
        loginButton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH,  "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button")))
        loginButton.click()
        systemMessage = WebDriverWait(self.driver,5).until(ec.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/div[2]/div/div[2]")))
        assert systemMessage.text == "• Giriş başarılı."
    
    def test_notification(self):
        self.driver.execute_script("window.scrollBy(0, 500);") 
        sleep(1)
        # Duyuru ve Haber Kontrolü
        notification_button = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "notification-tab")))
        notification_button.click()
        sleep(1)
        # Daha fazla göster 
        showmorebutton = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='notification-tab-pane']/div/div[4]")))
        showmorebutton.click()
        notifications = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[1]/div")))
        assert notifications.text == "Duyurularım"
        sleep(1)
        # arama butonu 
        search_btn = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "search")))
        search_btn.send_keys("Ocak")
        sleep(1)
        filtre_btn = notifications = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div")))
        filtre_btn.click()
        assert 'Ocak' in filtre_btn.text      
        sleep(1)
        # arama butonu temizleme
        search_btn = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "search")))
        search_btn.clear()
        sleep(1)
        # Duyuru bulunmamaktadır
        search_btn = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "search")))
        search_btn.send_keys("s")
        search_btn.send_keys("ın")
        search_btn.send_keys("av")
        sleep(1)
        search_not_btn = WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[2]/div/p")))
        search_btn.click()
        assert search_not_btn.text == 'Bir duyuru bulunmamaktadır.'
        sleep(1)
        # sayfa yenile
        self.driver.get("https://tobeto.com/duyurular")
        self.driver.refresh()
        sleep(1)

        # tür seçme

        type_button = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[1]/div/div[2]/button")))
        type_button.click()
        sleep(1)
        type_button = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[1]/div/div[2]/ul/li[2]/div")))
        type_button.click()
        
        sleep(1)
        self.driver.get("https://tobeto.com/duyurular")
        self.driver.refresh()
        sleep(1)
       # organizasyon seçme 
        organization_button = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[1]/div/div[3]/div[1]/div[1]/div[2]")))
        organization_button.click()
        sleep(1)
        self.driver.get("https://tobeto.com/duyurular")
        self.driver.refresh()
        sleep(1)
       # sıralama butonu
        line_up = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[1]/div/div[4]/div[1]/button")))
        line_up.click()
        sleep(1)
        line_up= WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[1]/div/div[4]/div[1]/ul/li[2]/a")))
        line_up.click()
        sleep(1)
        line_filtre = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[2]/div[1]/div/div[2]/span[1]")))
        assert line_filtre.text == '27.09.2023'
    
    def test_surveys(self):
        self.driver.execute_script("window.scrollBy(0, 500);") 
        sleep(2)
        #anketlerim Kontrolü
        survey_button = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "mySurvey-tab")))
        self.driver.execute_script("window.scrollBy(0, 100);")   
        survey_button.click()
        sleep(3)
        survey_not_btn = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID, "mySurvey-tab-pane")))
        assert survey_not_btn.text == 'Atanmış herhangi bir anketiniz bulunmamaktadır'


     
        
      


    
