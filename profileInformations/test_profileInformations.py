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
from selenium.webdriver.support.ui import Select

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

    #Deneyimlerim sayfasında başarılı şekilde deneyim eklenmesi test edilecektir.
        
    def test_myExperiences_Add(self):
        profileImg = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button")))
        profileImg.click()
        myInformationButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")))
        myInformationButton.click()
        myExperiences = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[2]")))
        myExperiences.click()
        company = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input")))
        company.send_keys("Tobeto")
        position = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input")))
        position.send_keys("Yazılım Test")
        sector = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input")))
        sector.send_keys("Yazılım")
        city = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/select")))
        select_city = Select(city)
        select_city.select_by_visible_text("İstanbul")
        startDate = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div/div/input")))
        startDate.send_keys("01.01.2021")
        startDate.send_keys(Keys.ENTER)
        endDate = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/div/div/input")))
        endDate.send_keys("01.01.2022")
        endDate.send_keys(Keys.ENTER)
        description = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[7]/textarea")))
        description.send_keys("Test senaryosu oluşturmak")
        saveButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/button")))
        saveButton.click()
        systemMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/div[2]/div/div[2]"))).text
        sleep(2)
        assert "Deneyim eklendi." in systemMessage
    #Deneyim ekleme sayfasında devam etmekte olduğunu deneyimi eklemensi test edilecektir.
    def test_myExperiences_to_Work_Contd(self):
        profileImg = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button")))
        profileImg.click()
        myInformationButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")))
        myInformationButton.click()
        myExperiences = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[2]")))
        myExperiences.click()
        company = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input")))
        company.send_keys("Enocta")
        position = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input")))
        position.send_keys("Yazılım Test")
        sector = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input")))
        sector.send_keys("Yazılım")
        city = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/select")))
        select_city = Select(city)
        select_city.select_by_visible_text("İstanbul")
        startDate = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div/div/input")))
        startDate.send_keys("01.01.2021")
        startDate.send_keys(Keys.ENTER)
        toWorkContd = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/label[2]/input")))
        toWorkContd.click()
        description = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[7]/textarea")))
        description.send_keys("Test senaryosu oluşturmak")
        saveButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/button")))
        saveButton.click()
        experience = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]")))
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        assert "Devam Ediyor" in experience.text

    #Deneyimlerim sayfasında şirket adı alanına en az 5 karakter girilmeden deneyim eklenme işlemi test edilecektir.
    def test_myExperiences_companyName_missing_char(self):
        profileImg = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button")))
        profileImg.click()
        myInformationButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")))
        myInformationButton.click()
        myExperiences = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[2]")))
        myExperiences.click()
        company = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input")))
        company.send_keys("Tob")
        position = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input")))
        position.send_keys("Yazılım Test")
        sector = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input")))
        sector.send_keys("Yazılım")
        city = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[4]/select")))
        select_city = Select(city)
        select_city.select_by_visible_text("İstanbul")
        startDate = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[5]/div/div/input")))
        startDate.send_keys("01.01.2021")
        startDate.send_keys(Keys.ENTER)
        endDate = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[6]/div/div/input")))
        endDate.send_keys("01.01.2022")
        endDate.send_keys(Keys.ENTER)
        description = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[7]/textarea")))
        description.send_keys("Test senaryosu oluşturmak")
        saveButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/button")))
        saveButton.click()
        mardatoryField = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.CLASS_NAME,"text-danger")))
        sleep(2)
        assert "En az 5 karakter girmelisiniz" in mardatoryField.text

    #Deneyimlerim sayfasında varolan deneyimi silme işlemi test edilecektir.
    def test_myExperiences_Delete(self):
        profileImg = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button")))
        profileImg.click()
        myInformationButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")))
        myInformationButton.click()
        myExperiences = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[2]")))
        myExperiences.click()
        deleteExperience = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[2]/div[5]/span[1]")))
        deleteExperience.click()
        iframe = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "iframe[@title='archetype']")))
        self.driver.switch_to.frame(iframe)
        yesButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div/div/div/div[2]/button[2]")))
        yesButton.click()
        self.driver.switch_to.default_content()
        systemMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/div[2]/div/div[2]"))).text
        sleep(2)
        assert "Deneyim kaldırıldı." in systemMessage

    #Deneyimler sayfasında boş alanları doldurmadan deneyim eklenme işlemi test edilecektir.
    def test_myExperiences_Add_Empty(self):
        profileImg = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button")))
        profileImg.click()
        myInformationButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")))
        myInformationButton.click()
        myExperiences = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[2]")))
        myExperiences.click()
        saveButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/button")))
        saveButton.click()
        mardatoryFields = WebDriverWait(self.driver,2).until(ec.visibility_of_all_elements_located((By.CLASS_NAME,"text-danger")))
        
        for mardatoryField in mardatoryFields:
            assert "Doldurulması zorunlu alan" in mardatoryField.text

    #Ayarlar sayfasında eski şifre farklı girilerek şifre değiştirme işlemi test edilecektir.
    def test_Setting_with_Diff_Password_Try(self):
        profileImg = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button")))
        profileImg.click()
        myInformationButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")))
        myInformationButton.click()
        settings = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[8]")))
        settings.click()
        oldPassword = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input")))
        oldPassword.send_keys("abc1")
        newPassword = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input")))
        newPassword.send_keys("abc123")
        newPasswordAgain = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input")))
        newPasswordAgain.send_keys("abc123")
        changePassword = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[1]/button")))
        changePassword.click()
        systemMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/div[2]/div/div[2]"))).text
        assert "Mevcut şifre geçersizdir." in systemMessage
    
    #Ayarlar sayfasında yeni şifre alanı boş bırakılarak şifre değiştirme işlemi test edilecektir.
    def test_Setting_least_new_Password(self):
        profileImg = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button")))
        profileImg.click()
        myInformationButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")))
        myInformationButton.click()
        settings = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[8]")))
        settings.click()
        oldPassword = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input")))
        oldPassword.send_keys("abc123456")
        newPassword = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input")))
        newPassword.send_keys("a")
        newPasswordAgain = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input")))
        newPasswordAgain.send_keys("a")
        changePassword = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[1]/button")))
        changePassword.click()
        systemMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/div[2]/div/div[2]"))).text
        assert "Şifreniz en az 6 karakterden oluşmalıdır." in systemMessage
    
    #Ayarlar sayfasında birbirinde farklı yeni şifre girilerek şifre değiştirme işlemi test edilecektir.
    def test_Setting_with_Diff_newPassword(self):
        profileImg = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button")))
        profileImg.click()
        myInformationButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")))
        myInformationButton.click()
        settings = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[8]")))
        settings.click()
        oldPassword = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input")))
        oldPassword.send_keys("abc123456")
        newPassword = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input")))
        newPassword.send_keys("abc123")
        newPasswordAgain = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input")))
        newPasswordAgain.send_keys("abc1234")
        changePassword = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[1]/button")))
        changePassword.click()
        systemMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/div[2]/div/div[2]"))).text
        assert "Girilen şifreler eşleşmiyor kontrol ediniz" in systemMessage

    #Ayarlar sayfasında tüm şifreler aynı girilerek şifre değiştirme işlemi test edilecektir.
    def test_Setting_with_all_samePassword(self):
        profileImg = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button")))
        profileImg.click()
        myInformationButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")))
        myInformationButton.click()
        settings = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[8]")))
        settings.click()
        oldPassword = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input")))
        oldPassword.send_keys("abc123456")
        newPassword = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input")))
        newPassword.send_keys("abc123456")
        newPasswordAgain = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input")))
        newPasswordAgain.send_keys("abc123456")
        changePassword = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[1]/button")))
        changePassword.click()
        systemMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/div[2]/div/div[2]"))).text
        assert "Yeni şifreniz mevcut şifrenizden farklı olmalıdır" in systemMessage

    #Ayarlar sayfasında başarılı şekilde şifre değiştirme işlemi test edilecektir.
    def test_Setting_successfull_change_Password(self):
        profileImg = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button")))
        profileImg.click()
        myInformationButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")))
        myInformationButton.click()
        settings = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[8]")))
        settings.click()
        oldPassword = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input")))
        oldPassword.send_keys("abc123456")
        newPassword = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input")))
        newPassword.send_keys("abc1234")
        newPasswordAgain = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input")))
        newPasswordAgain.send_keys("abc1234")
        changePassword = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[1]/button")))
        changePassword.click()
        systemMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/div[2]/div/div[2]"))).text
        sleep(5)
        oldPassword.send_keys("abc1234")
        newPassword.send_keys("abc123456")
        newPasswordAgain.send_keys("abc123456")
        assert "Şifreniz güncellenmiştir" in systemMessage

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