from models.Bot import Bot
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import pyautogui

class Download_bill(Bot):
    
    def _click_print_bank_slip_btn(self) -> None:
        time.sleep(0.5)
        if self._check_Element("//button[@id='print']", 5):
            time.sleep(0.5)
            self.driver.find_element(By.XPATH, "//button[@id='print']").click()

    def _print_bank_slip(self, nf_number) -> None:
        #Use the shortcut key to print.
        time.sleep(3.5) #Wait for the website to load.
        pyautogui.keyDown("ctrl")
        pyautogui.press("p")
        pyautogui.keyUp("ctrl")

        #Press "Enter" to confirm the print.
        time.sleep(0.5)
        pyautogui.press("enter")

        #Enter the invoice number as the file name.
        time.sleep(2)
        pyautogui.write(nf_number, interval=0.2)

        #Press "Enter" to save the file.
        time.sleep(2)
        pyautogui.press("enter")

        #Close the browser window.
        time.sleep(2)
        pyautogui.keyDown("ctrl")
        pyautogui.press("w")
        pyautogui.keyUp("ctrl")
    
    def _exit_card(self) -> None:
        time.sleep(1.5)
        pyautogui.press("esc")

    def _exit_error_card(self) -> None:
        time.sleep(1)
        btn = self.driver.find_element(By.XPATH,"//div[@class='swal2-actions']//button[@class='swal2-confirm swal2-styled']")
        btn.click()

    def _check_Element(self, xpath: str, time: int) -> bool:
        """
            Check if the element exist and load. If don't load, returns False
        
            Input:
                - xpath - str - (element's xpath)
                - time - int - (How mach time need to load)

            Output:
                - True
                - False
        """
        
        try:
            wait = WebDriverWait(self.driver, timeout=time)
            return wait.until(lambda d: self.driver.find_element(By.XPATH, xpath).is_displayed())
        except:
            return False
        
    def run_bot(self) -> None:
        self.init_driver()
        self.open_site("Troque a configuração do navegado para \"Perguntar onde salvar cada arquivo\"")

        tbody = self.driver.find_element(By.TAG_NAME, "tbody")
        tr_list = tbody.find_elements(By.XPATH, "//tr[@class='AUTORIZADO']")
        tr_list.extend(tbody.find_elements(By.XPATH, "//tr[@class='RECIBO']"))

        for tr in tr_list:
            td_list = tr.find_elements(By.TAG_NAME, "td")
            nf_number = td_list[8].text
            
            btn_list = tr.find_element(By.XPATH, ".//button[@title='Títulos']")
            btn_list.click()
                            
            #Click the print button inside the release card.
            self._click_print_bank_slip_btn()
            
            #Check if there is a bank slip available for printing.
            if self._check_Element("//h2[@id='swal2-title']", 5):
                self._exit_error_card()
            else:
                self._print_bank_slip(nf_number)

            #Close the pop-up window.
            self._exit_card()
            time.sleep(2)

        input("Digite qualquer tecla para finalizar: ")
        self.driver.quit()

