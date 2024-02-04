from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pytest


class Test_myEducations():

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/giris")
        self.driver.maximize_window()
        self.successful_login()

    def teardown_method(self):
        self.driver.quit()
     
     #Eğitim paneli kontrol
    def successful_login(self):     
        email_input = WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/main/section/div/div/div/div/form/input[1]")))
        email_input.send_keys("utkutrn@hotmail.com")
        password_input = WebDriverWait(self.driver, 3).until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/main/section/div/div/div/div/form/input[2]")))
        password_input.send_keys("tobeto1234")
        login_button = WebDriverWait(self.driver, 4).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/section/div/div/div[1]/div/form/button")))
        login_button.click()
        searchContent = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/div[2]")))
        assert  "Giriş başarılı" in searchContent.text
    
    def test_education_panel(self):
        #eğitimlerim tab menüsünü bul
        myTrainingbutton = WebDriverWait(self.driver, 4).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='lessons-tab']")))
        # eğitimlerim menüsüne tıkla
        myTrainingbutton.click()
        #Daha fazla göster butonu.
        mytrainingsShowMore = WebDriverWait(self.driver, 4).until(ec.visibility_of_element_located((By.XPATH, "//div[@class='showMoreBtn'][1]")))
        # daha fazla göster butonu gözükecek şekilde sayfayı kaydır
        self.driver.execute_script("arguments[0].scrollIntoView();", mytrainingsShowMore)
        # sayfanın kaymasını bekle
        sleep(1)
        # sayfa kayınca daha fazla göstere tıkla
        mytrainingsShowMore.click()
        # daha fazlasını göstermesini bekle
        sleep(2)
        searchContent = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main")))
        assert  "Eğitimlerim" in searchContent.text
        #Arama çubuğuna aranacak kelimeyi yaz
        search_input_box = WebDriverWait(self.driver, 4).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='search']")))
        search_input_box.send_keys("y")
        sleep(1)
        search_input_box.send_keys("a")
        sleep(1)
        search_input_box.send_keys("z")
        search_input_box.send_keys("ı")
        search_input_box.send_keys("l")
        search_input_box.send_keys("ı")
        search_input_box.send_keys("m")
        #arama sonucunu görmeyi bekle
        sleep(2)
        searchContent = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main")))
        assert  "Yazılım" in searchContent.text
        #sonucu gördükten sonra bir sonraki arama için arama kutusunu temizle
        search_input_box.clear()
        sleep(2)

        #Başarısız arama denemesi
        search_input_box.send_keys("t")
        search_input_box.send_keys("o")
        search_input_box.send_keys("b")
        search_input_box.send_keys("e")
        search_input_box.send_keys("t")
        sleep(1)
        search_input_box.send_keys("o")
        sleep(2)
        #arama sonucunu görmeyi bekle
        sleep(2)
        searchContent = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main")))
        assert  "Size atanan herhangi bir eğitim bulunmamaktadır." in searchContent.text
        
        try:
            # 'hata_mesaji_alani' elementini bulmaya çalış
            
            errormessagearea = self.driver.find_element(By.CLASS_NAME, 'noDataCard')
            print("Hata mesajı alanı var.")
            #assert hata_mesaji_alani.text == "Size atanan herhangi bir eğitim bulunmamaktadır.*"
        except NoSuchElementException:
            print("Hata mesajı alanı yok.")

        #sonucu gördükten sonra bir sonraki arama için arama kutusunu temizle
        search_input_box.clear()
        search_input_box.send_keys(' ')
        search_input_box.send_keys(Keys.BACK_SPACE)
        sleep(3)

        # kurum filtresi alanı
        institution_filter_input = WebDriverWait(self.driver, 4).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='react-select-2-input']")))
        institution_filter_input.send_keys("İstanbul" + Keys.ENTER)
        sleep(2)
        searchContent = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[1]/div/div[2]/div/div[1]")))
        assert  "İstanbul" in searchContent.text
       
        # Aramaya göre seçilen filtreyi kaldırma
        remove_selected_institution_filter = self.driver.find_element(By.XPATH, '//*[contains(@aria-label, "İstanbul")]').click()
        sleep(2)
        # kurum filtresi alanı
        institution_filtering = WebDriverWait(self.driver, 4).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='react-select-2-input']")))
        #Filitreleme Çubuğu başarısız.
        institution_filtering.send_keys("tobeto")
        searchContent = WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.XPATH, "//*[@id='__next']/div/main/div[2]/div[1]/div/div[2]/div")))
        assert  "Seçenek" in searchContent.text
        
        institution_filter_search_menu_area = WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located((By.CLASS_NAME,"select__menu")))
        institution_filter_search_menu_area_content = institution_filter_search_menu_area.text
        if "tobeto" in institution_filter_search_menu_area_content :
            print("Filtrede tobeto ile ilgili sonuç var.")
        else:
            print("Filtrede tobeto ile ilgili sonuç yok.")
            self.driver.execute_script("alert('Sonuç alamadık');")
            sleep(2)
            alert = self.driver.switch_to.alert
            alert.accept()  # Uyarıyı kabul etmek için
        sleep(2)
        # sıralama değiştirme
        filters = self.driver.find_elements(By.CSS_SELECTOR, '.select__control')
        sort_filter = filters[1]
        sort_filter.click()
        sleep(1)
        assert "Yazılım" in self.driver.page_source

        training_sorting_option = self.driver.find_elements(By.CSS_SELECTOR, '.select__menu-list .select__option')
        za_arrangement = training_sorting_option[1]
        za_arrangement.click()
        sleep(3)
        sort_filter.click()
        sleep(1)
        assert "Yazılım" in self.driver.page_source

        education_sorting_options = self.driver.find_elements(By.CSS_SELECTOR, '.select__menu-list .select__option')
        ye_arrangement = education_sorting_options[2]
        ye_arrangement.click()
        sleep(5)
        assert "Yazılım" in self.driver.page_source
 
        #sonuncu eğitim elemanına eriş (asenkron)
        trainings = self.driver.find_elements(By.CSS_SELECTOR, '#all-lessons-tab-pane > div > div')
        last_education = trainings[-1]
        last_education_link = last_education.find_element(By.TAG_NAME, 'a')
        self.driver.execute_script("arguments[0].scrollIntoView();", last_education)
        sleep(1)
        last_education_link.click()
        videoPlayButton = WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located((By.CLASS_NAME, "vjs-big-play-button")))
        videoPlayButton.click()
        assert "Yazılım Kalite ve Test " in self.driver.page_source
       
       # Videonun oynamaya başladığını kontrol et
        def video_started(sd):
            return sd.execute_script("return document.getElementById('my-player_html5_api').currentTime > 0;")

        
        try:
            WebDriverWait(self.driver, 20).until(video_started)
            self.driver.execute_script("alert('Video oynamaya başladı');")
            sleep(2)
            alert = self.driver.switch_to.alert
            alert.accept()  # Uyarıyı kabul etmek için
        except NoSuchElementException:
            self.driver.execute_script("alert('Video oynatılamadı');")
            sleep(2)
            alert = self.driver.switch_to.alert
            alert.accept()  # Uyarıyı kabul etmek için

        # 5 saniye izle
        sleep(5)
        