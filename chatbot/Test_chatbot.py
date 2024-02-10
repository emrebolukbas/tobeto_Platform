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


class Test_tobetoPlatformLogin():

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://tobeto.com/giris")
        self.driver.maximize_window()
        self.test_login_page
      
    def teardown_method(self):
        self.driver.quit()

    # 1) Giriş yap alanı görüntülenebilir ve işlevselliği test edilecektir.
    def test_login_page(self):
        chatbot_symbol_frame = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, "exw-launcher-frame")))
        self.driver.switch_to.frame(chatbot_symbol_frame)

        chatbot_icon = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, "launcher")))
        chatbot_icon_hover = ActionChains(self.driver)
        chatbot_icon_hover.move_to_element(chatbot_icon).perform()
        chatbot_icon.click()

        self.driver.switch_to.default_content()
        chatbot_chat_framework = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, "exw-conversation-frame")))
        self.driver.switch_to.frame(chatbot_chat_framework)
        
       
        chatbot_namesurname_input = WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div.exw-inline-response-input-container input")))
        chatbot_namesurname_input.send_keys("Tobeto Öğrencisi")

        chatbot_namesurname_input_text = chatbot_namesurname_input.get_attribute("value")
        if "Öğrenci" in chatbot_namesurname_input_text:
            self.driver.execute_script("alert('Metin girişi başarılı');")
        else:
            self.driver.execute_script("alert('Metin girişi başarısız');")
        assert "Öğrenci" in chatbot_namesurname_input_text, "Metin girişi başarısız."

        sleep(1)
        alert = self.driver.switch_to.alert
        alert.accept()  # Uyarıyı kabul etmek için
        sleep(1)

        chatbot_namesurname_input.send_keys(Keys.ENTER)

        sleep(2)


        # Kategori başlıklarını içeren <ul> elementini bulma
        chatbot_reply_options_framework = WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located((By.CLASS_NAME, "exw-replies")))
       
        sleep(1)
        chatbot_ready_response_options = chatbot_reply_options_framework.find_elements(By.CLASS_NAME, "exw-reply")


        # Başlıkları ekrana yazdırma
        for Options in chatbot_ready_response_options:
            if "Tobeto" in Options.text:
                tobeto_hk_option = Options
            else:
                continue
       
        assert tobeto_hk_option is not None, "Tobeto seçeneği bulunamadı."
        tobeto_hk_option.click()
                
        chat_bot_file_attachment_button= WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located((By.CLASS_NAME, "exw-add-file")))
        chat_bot_file_attachment_button.click()

              
        chatbot_file_drag_and_drop_area = WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".exw-drag-drop-container")))
        chatbot_file_drag_and_drop_area_class_list =chatbot_file_drag_and_drop_area.get_attribute('class')

        if "hidden" in chatbot_file_drag_and_drop_area_class_list:
            self.driver.execute_script("alert('sürükle bırak alanı kapalı');")
        else:
            self.driver.execute_script("alert('sürükle bırak alanı açık');")
        
        sleep(1)
        alert = self.driver.switch_to.alert
        alert.accept()  # Uyarıyı kabul etmek için
        sleep(1)
        assert "Dosya " in self.driver.page_source
        
        self.driver.get("https://tobeto.com")

        chatbot_chat_framework = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, "exw-conversation-frame")))
        self.driver.switch_to.frame(chatbot_chat_framework)

        chatbot_closing_button = WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#exw-conversation-frame-body > div > div > div > div.exw-header-and-loading > div > div.exw-header-buttons > svg.exw-end-session-button.header-button")))
        chatbot_closing_button.click()


        chatbot_closing_framework = WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".exw-finishSessionCheck > .finishSessionCheckButtons")))
       
        sleep(1)
        chatbot_closing_options = chatbot_closing_framework.find_elements(By.TAG_NAME, "button")


        # Başlıkları ekrana yazdırma
        for Options in chatbot_closing_options:
            if "Evet" in Options.text:
                shutdown_yes_option = Options
            else:
                continue
        assert shutdown_yes_option is not None, "'Evet' seçeneği bulunamadı."
        shutdown_yes_option.click()
        

        chatbot_survey_frame = WebDriverWait(self.driver, 15).until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".exw-rateEmojis")))
        chatbot_survey_options = chatbot_survey_frame.find_elements(By.CSS_SELECTOR, "svg.rateEmoji")

        chatbot_survey_options[3].click()
        
        sleep(1)
        assert len(chatbot_survey_options) >= 4, "Anket seçenekleri yetersiz."
        
        chatbot_send_survey_button = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((By.ID, "surveyBtn")))
        chatbot_send_survey_button.click()

        sleep(5)

        self.driver.quit()


