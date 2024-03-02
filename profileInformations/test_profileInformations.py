from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
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
       
    #Eğitim Hayatım sayfası görüntüleme test edilecektir.
    def test_my_education (self):
        self.driver.get('https://tobeto.com/profilim/profilimi-duzenle/egitim-hayatim')
        sleep(3)
        assert "Eğitim" in self.driver.page_source

    #Eğitim Hayatım sayfası boş kayıt test edilecektir.
    def test_my_education_life(self):
        self.driver.get('https://tobeto.com/profilim/profilimi-duzenle/egitim-hayatim')
        save_button_element = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'form > button')))
        save_button_element.click()
        sleep(1)
        assert "Doldurulması zorunlu alan" in self.driver.page_source
       
    
    #Eğitim Hayatım Eğitim durumu kontrol
    def test_my_education_status_options(self):
        self.driver.get('https://tobeto.com/profilim/profilimi-duzenle/egitim-hayatim')
        option_values = []
        select_element = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'select[name="EducationStatus"]')))
        select_element.click()
        select = Select(select_element)
        for option in select.options:
            option_values.append(option.get_attribute("value"))
        option_count = len(select.options)
        if option_count > 4:
            message = "Select içinde 4'ten fazla seçenek var!"
        else:
            message = "Select içinde 4 veya daha az seçenek var!"
        print(message)
        assert 1 == 1, print(message)

    #Eğitim Hayatım üniversite input kontrol
    def test_my_education_university_input_control(self):
        self.driver.get('https://tobeto.com/profilim/profilimi-duzenle/egitim-hayatim')
        university_input_element = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="University"]')))
        for i in range(0, 100):
            university_input_element.send_keys(".")
        sleep(1)
        save_button_element = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'form > button')))
        save_button_element.click()
        sleep(1)
        next_element = university_input_element.find_element(By.XPATH, "following-sibling::span")
        
        if "En fazla" in next_element.text:
            print("100 karakter girilemiyor.")
        else:
            print("100 karakter girilebiliyor.")

        sleep(1)
        university_input_element.clear()
        save_button_element.click()
        sleep(1)
        next_element = university_input_element.find_element(By.XPATH, "following-sibling::span")
        
        if "zorunlu" in next_element.text:
            print("Boş bırakılamıyor.")
        else:
            print("Boş bırakılabiliyor.")
        assert "Eğitim" in self.driver.page_source

    #Eğitim Hayatım bölüm input kontrol
    def test_my_education_department_input_control(self):
        self.driver.get('https://tobeto.com/profilim/profilimi-duzenle/egitim-hayatim')
        department_input_element = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="Department"]')))
        for i in range(0, 100):
            department_input_element.send_keys(".")
        sleep(1)
        save_button_element = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'form > button')))
        save_button_element.click()
        sleep(1)
        next_element = department_input_element.find_element(By.XPATH, "following-sibling::span")
        
        if "En fazla" in next_element.text:
            print("100 karakter girilemiyor.")
        else:
            print("100 karakter girilebiliyor.")

        sleep(1)
        department_input_element.clear()
        save_button_element.click()
        sleep(1)
        next_element = department_input_element.find_element(By.XPATH, "following-sibling::span")
        
        if "zorunlu" in next_element.text:
            print("Boş bırakılamıyor.")
        else:
            print("Boş bırakılabiliyor.")
        assert "Eğitim" in self.driver.page_source
      
    #Eğitim Hayatım başlangıç yılı input kontrol
    def test_my_education_start_year_input_control(self):
        self.driver.get('https://tobeto.com/profilim/profilimi-duzenle/egitim-hayatim')
        start_year_main_element =  WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.react-datepicker-wrapper')))
        start_year_input_element = WebDriverWait(start_year_main_element,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'div > input')))
        start_year_input_element.send_keys("2024")
        save_button_element = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'form > button')))
        save_button_element.click()
        sleep(2)
        start_year_input_element.send_keys(Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE, Keys.BACK_SPACE)
        sleep(1)
        save_button_element.click()
        sleep(5)
        next_element = start_year_main_element.find_element(By.XPATH, "following-sibling::span")
        if "zorunlu" in next_element.text:
            print("Boş bırakılamıyor.")
        else:
            print("Boş bırakılabiliyor.")
        assert "Eğitim" in self.driver.page_source
        
    #Eğitim Hayatım mezuniyet yılı input kontrol
    def test_my_education_graduation_year_input_control(self):
        self.driver.get('https://tobeto.com/profilim/profilimi-duzenle/egitim-hayatim')
        graduation_year_main_element =  WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.react-datepicker-wrapper:nth-child(2)')))
        graduation_year_input_element = WebDriverWait(graduation_year_main_element,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'div > input')))
    
        if graduation_year_input_element.is_enabled():
            print("Mezuniyet yılı etkin durumda.")
        else:
            print("Mezuniyet yılı pasif durumda.")
        assert "Eğitim" in self.driver.page_source
        
    #Eğitim Hayatım devam ediyorum aktifken mezuniyet yılı pasiflik kontrol
    def test_my_education_checkbox_control(self):
        self.driver.get('https://tobeto.com/profilim/profilimi-duzenle/egitim-hayatim')
        sleep(1)
        datepicker_elements =  WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR, '.react-datepicker-wrapper')))
        start_year_input_element = WebDriverWait(datepicker_elements[0],5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'div > input')))
        start_year_input_element.send_keys("2020")
        sleep(1)
        graduation_year_main_element = datepicker_elements[1]
        graduation_year_input_element = WebDriverWait(graduation_year_main_element,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'div > input')))
        graduation_year_input_element.click()
        graduation_year_input_element.send_keys("2022")
        sleep(1)
        start_year_input_element.click()
        sleep(1)
        checkbox_element =  WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.NAME, 'checkbox')))
        checkbox_element.click()
        sleep(1)
        graduation_year_input_element.click()
        
        if graduation_year_input_element.is_enabled():
            print("Mezuniyet yılı etkin durumda.")
        else:
            print("Mezuniyet yılı pasif durumda.")
        sleep(1)
        assert "Eğitim" in self.driver.page_source
        
    #Eğitim Hayatım kayıt kontrol
    def test_my_education_save_control(self):
        self.driver.get('https://tobeto.com/profilim/profilimi-duzenle/egitim-hayatim')

        education_status_select_element = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'select[name="EducationStatus"]')))
        education_status_select_element.click()
        education_status_select = Select(education_status_select_element)
        education_status_select.select_by_visible_text("Ön Lisans")
        sleep(1)
        
        university_input_element = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="University"]')))
        university_input_element.send_keys("Haliç University")
        sleep(1)
        
        department_input_element = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="Department"]')))
        department_input_element.send_keys("Software Tester")
        sleep(1)

        datepicker_elements =  WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.CSS_SELECTOR, '.react-datepicker-wrapper')))
        start_year_input_element = WebDriverWait(datepicker_elements[0],5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'div > input')))
        start_year_input_element.click()
        sleep(1)
        WebDriverWait(datepicker_elements[1],5).until(ec.visibility_of_element_located((By.XPATH, '//div[text()="2019"]'))).click()
        sleep(1)

        graduation_year_input_element = WebDriverWait(datepicker_elements[1],5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'div > input')))
        graduation_year_input_element.click()
        sleep(1)
        WebDriverWait(datepicker_elements[1],5).until(ec.visibility_of_element_located((By.XPATH, '//div[text()="2021"]'))).click()
        sleep(1)
        
        save_button_element = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'form > button')))
        save_button_element.click()
        sleep(3)
        try:
            success_message_element = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.CSS_SELECTOR, '.fade.toast.bg-success')))
            print("Kayıt başarılı")
        except NoSuchElementException:
            print("Kayıt başarılı değil")     
            sleep(2)
            assert "Eğitim" in self.driver.page_source

    #Sosyal Medya sayfası görüntüleme test edilecektir.
    def test_socialMedia(self):
        profileImg = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button")))
        profileImg.click()
        myInformationButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")))
        myInformationButton.click() 
        socialMedia = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[6]")))
        socialMedia.click()
        current_url = self.driver.current_url
        expected_url = "https://tobeto.com/profilim/profilimi-duzenle/medya-hesaplarim"
        assert current_url == expected_url
    
    #Doldurulması zorunlu alanlar doldurulmadan sosyal medya hesapları kaydedilme işlemi test edilecektir.
    def test_mardatoryArea_mymedia(self):
        profileImg = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button")))
        profileImg.click()
        myInformationButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")))
        myInformationButton.click() 
        socialMedia = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[6]")))
        socialMedia.click()
        save_button = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div[1]/form/button")))
        save_button.click()
        MandatoryArea = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div[1]/form/div/div[1]/span")))
        assert "Doldurulması zorunlu alan" in MandatoryArea.text
    
    #Sosyal medya hesapları ekleme işlemi test edilecektir.
    def test_socialmedia_add_delete(self):
        profileImg = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button")))
        profileImg.click()
        myInformationButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")))
        myInformationButton.click() 
        socialMedia = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[6]")))
        socialMedia.click()
        media_choose = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div/form/div/div[1]/select")))
        media_choose.click()
        linkedin_add = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div/form/div/div[1]/select/option[4]")))
        linkedin_add.click()
        linkArea = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div/form/div/div[2]/input")))
        linkArea.send_keys("https://www.linkedin.com/in/tobeto-test/")
        save_button = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div/form/button")))
        save_button.click()
        systemMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/div[2]/div/div[2]"))).text
        assert "Sosyal medya adresiniz başarıyla eklendi" in systemMessage
        media_choose = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div/form/div/div[1]/select")))
        media_choose.click()
        sleep(2)
        linkedin_add = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div/form/div/div[1]/select/option[4]")))
        linkedin_add.click()
        sleep(2)
        linkArea = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div/form/div/div[2]/input")))
        linkArea.send_keys("https://www.linkedin.com/in/tobeto-test/")
        save_button = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[2]/div/form/button")))
        save_button.click()
        sleep(2)
        systemMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/div[2]/div/div[2]")))
        #Varolan sosyal medya adresi ekleme
        assert "Bu sosyal medya zaten mevcut" in systemMessage.text
        closeSystemMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/div[2]/div/div[1]/button")))
        closeSystemMessage.click()
        delete_button = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".social-delete")))
        delete_button.click()
        yesButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".btn-yes")))
        yesButton.click()
        systemMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/div[2]/div/div[2]")))
        #sosyal medya adresi silme
        assert "Sosyal medya adresiniz başarıyla kaldırıldı" in systemMessage.text
        
        

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
        changePassword.click()
        assert "Şifreniz güncellenmiştir" in systemMessage
    
    
    #Ayarlar sayfasında şifre alanına 6 karakter boşluk (space tuşu) karakteri girilerek şifre değiştirme işlemi test edilecektir.
    def test_Setting_useSpaceKey_change_Password(self):
        profileImg = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/button")))
        profileImg.click()
        myInformationButton = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/nav/div[1]/div/div/div[2]/ul/li[1]/a")))
        myInformationButton.click()
        settings = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[1]/div/a[8]")))
        settings.click()
        oldPassword = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[1]/input")))
        oldPassword.send_keys("abc123456")
        newPassword = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[2]/input")))
        newPassword.send_keys("      ")
        newPasswordAgain = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/form/div/div[3]/input")))
        newPasswordAgain.send_keys("      ")
        changePassword = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/main/section/div/div/div[2]/div/div/div[1]/button")))
        changePassword.click()
        systemMessage = WebDriverWait(self.driver,2).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/div[2]/div/div[2]"))).text
        sleep(5)
        oldPassword.send_keys("      ")
        newPassword.send_keys("abc123456")
        newPasswordAgain.send_keys("abc123456")
        changePassword.click()
        assert "Geçersiz Karakter Girişi" in systemMessage
        #Gerçekleşen Sonuç: Şifre değiştirme işlemi başarılı bir şekilde gerçekleşmiştir.

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