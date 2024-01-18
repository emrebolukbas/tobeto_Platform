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
        assert  "Giriş başarılı." in systemMessage.text

    #1) Kullanıcının kişisel bilgi kısımlarının sayfa içerisinde görüntülenmesi test edilecektir.
    def test_myProfil_content_control(self):
        myProfil = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.MY_PROFIL_XPATH)))
        myProfil.click()
        sleep(5)
        myProfilContent = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.MY_PROFIL_CONTENT_XPATH)))
        nameSurnameContent = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/div/div[2]/div[1]/div/div[1]/div/div[2]/div[1]/div[2]/span[1]")))
        socialMediaContent = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/div/div[2]/div[1]/div/div[6]/div/div[1]/span")))
        activityMapContent = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/div/div[2]/div[2]/div/div[4]/div/div[1]/span")))
        assert myProfilContent.text == "Profilim"  
        assert nameSurnameContent.text == "Ad Soyad" 
        assert socialMediaContent.text == "Medya Hesaplarım" 
        assert activityMapContent.text == "Aktivite Haritam"

    #2) Kullanıcının profil linkinin kopyalayabilmesi test edilecektir.
    def test_tobeto_profil_link(self):
        myProfil = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,c.MY_PROFIL_XPATH)))
        myProfil.click()
        connectionLink = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='dropdown-basic']")))
        connectionLink.click()
        profilShareContent = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/div/div[1]/div/div/div/div[1]/p")))
        assert profilShareContent.text == "Profilimi paylaş"
        sleep(5)
        copyLink = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/div/div[1]/div/div/div/div[2]/div/i")))
        copyLink.click()
        systemMessage = WebDriverWait(self.driver,2).until(ec.presence_of_element_located((By.XPATH,"//*[@id='__next']/div/div[2]/div/div[2]")))
        assert  "Url kopyalandı." in systemMessage.text
    
    #3) Kullanıcının Değerlendirmeler sayfasındaki başarı modeli testi içerisindeki başla butonunun işlevselliği test edilecektir.
    def test_assessments_success_model_test(self):
        assessments = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/ul/li[3]/a")))
        assessments.click()
        assessmentsContent = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/ul/li[3]/a")))
        assert assessmentsContent.text == "Değerlendirmeler"
        startButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section[2]/div/div/div[1]/div/a")))
        startButton.click()
        assesmentsStartButtonContent = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div/div[3]/a")))
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        sleep(1)
        assert  "Değerlendirmeye Başla" in assesmentsStartButtonContent.text

    #4) Kullanıcının Değerlendirmeler sayfasındaki yazılımda başarı testindeki başla butonunun işlevselliği test edilecektir.
    def test_software_success_test(self):
        assessments = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/ul/li[3]/a")))
        assessments.click()
        softwareSuccessTest = WebDriverWait(self.driver,2).until(ec.visibility_of_all_elements_located((By.CLASS_NAME,"dashboard-card-slim")))
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        assert len(softwareSuccessTest) == 5
        startButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section[2]/div/div/div[4]/div/div[1]/button")))
        startButton.click()
        sleep(1)
        testContent = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div/div/div[1]/span")))
        assert  "Front End" in testContent.text
        