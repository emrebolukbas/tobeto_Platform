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


class Test_calendar_Testing():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get(c.BASE_URL)
        self.driver.maximize_window()

    def teardown_metahod(self):
        self.driver.quit()
        
    def test_calendar_visibility_of_login_page(self):
        calendar = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='__next']/div/section[1]/div[2]/div")))
        calendar.click()
        calendar_page_title = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[1]/span")))
        assert calendar_page_title.text == "Eğitim ve Etkinlik Takvimi", "Başlık 'Eğitim ve Etkinlik Takvimi' olarak bekleniyor."
        assert calendar.is_displayed(), "Takvim simgesi görüntülenmiyor."
        #aramacubuğu kontrolü
        search_bar=WebDriverWait(self.driver,10).until(ec.visibility_of_element_located((By.XPATH,"//*[@id='search-event']")))
        search_bar.click()
        search_bar.send_keys("yazılım kalite")
        #eğitmenaramayapılacak     
        #eğitim durumu
        # Listbox'a tıklama
        listbox_element = self.driver.find_element(By.XPATH, "//div[2]/div[2]/div/div/div[2]")
        actions = ActionChains(self.driver)
        actions.move_to_element(listbox_element).click_and_hold().perform()
         # Listbox'tan bir öğe seçme
        listbox_option = self.driver.find_element(By.XPATH, "//div[@id='react-select-2-option-0']")
        actions = ActionChains(self.driver)
        actions.move_to_element(listbox_option).release().perform()
        assert listbox_element.is_displayed(), "Listbox görüntülenmiyor."
        assert listbox_option.is_displayed(), "Listbox öğe seçimi başarısız."

        # Seçilen öğeyi tıklama
        checkbox_xpaths = ["//div[2]/div/div/div/div/div[2]/div[2]","//input[@name='eventEnded']","//input[@name='eventContinue']","//input[@name='eventBuyed']","//input[@name='eventNotStarted']"]
        checkbox_elements = [self.driver.find_element(By.XPATH, xpath) for xpath in checkbox_xpaths]
        for checkbox in checkbox_elements:
         checkbox.click()

        # Eğitim durumu kontrolü
        for checkbox in checkbox_elements[1:]:
         assert checkbox.is_selected(), f"{checkbox.get_attribute('name')} seçimi bekleniyor."

        # Geri Button öğesini bulma
        back_button = self.driver.find_element(By.XPATH, "//button[@title='geri']")
        # Geri Button öğesine tıklama
        back_button.click()
        # Bugün Button öğesini bulma
        today_button = self.driver.find_element(By.XPATH, "//button[@title='Bugün']")

       # Bugün Button öğesine tıklama
        today_button.click()
       # ileri Button öğesini bulma
        next_button = self.driver.find_element(By.XPATH, "//button[@title='ileri']")

        #ileri  Button öğesine tıklama
        next_button.click()
        # hafta Button öğesini bulma
        week_button = self.driver.find_element(By.XPATH, "//button[@title='Hafta']")

        # hafta Button öğesine tıklama
        week_button.click()
        # ay Button öğesini bulma
        day_button = self.driver.find_element(By.XPATH, "//button[@title='Gün']")

        #ay Button öğesine tıklama
        day_button.click()

