from models.Bot import Bot
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from openpyxl import load_workbook
import pyautogui
import os
import time

class Download_timesheets(Bot):
    '''Class responsible for download the timesheets.'''

    def _click_to_write(self) -> None:
        """Click the filter button."""
        time.sleep(1)
        element = self.driver.find_element(By.XPATH, "//div[@class='col-md-7 col-12']//div[@class='v-select__selections']")
        element.click()
        
    def _write_name(self, name: str) -> None:
        """Write the customer's name in the filter."""
        time.sleep(1)
        element = self.driver.find_element(By.XPATH, "//div[@class='col-md-7 col-12']//div[@class='v-select__selections']//input")
        element.send_keys(Keys.BACKSPACE)

        time.sleep(1)
        element.send_keys(name)

    def _first_element_click(self) -> None:
        """Click on the first item."""
        time.sleep(1)
        element = self.driver.find_element(By.XPATH, "//div[@class='v-menu__content theme--light menuable__content__active v-autocomplete__content']//div[@class='v-list-item__content']")
        element.click()

    def _download_timesheet(self) -> None:
        """Click the button to download the timesheet."""
        time.sleep(1)
        element = self.driver.find_element(By.XPATH, "//button[@id='btn-exportar-payroll']")
        element.click()

    def _wait_element_load(self) -> None:
        """Wait for the element to load."""
        try:
            wait = WebDriverWait(self.driver, timeout=300)
            wait.until(lambda d:(self.driver.find_element(By.XPATH, "//div[@class='swal2-success-ring']")).is_displayed)
            time.sleep(2)
        except:
            input("Erro! O elemento não carregou!")
        
    def _write_name_file_and_save(self, name: str) -> None:
        """Write the new file name and click Enter to save."""
        time.sleep(1)
        pyautogui.write(name, interval=0.2)
        time.sleep(0.5)
        pyautogui.press("enter")
        time.sleep(0.5)

    def _continue_btn(self) -> None:
        """Click the button to close the alert and continue."""
        element = self.driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']") 
        element.click()

    def _take_excel_file(self, url) -> dict:
        """
            Take a excel file and return a list of yours elements

            input:
                - file excel' URL

            output:
                - dict with id and value.
        """

        pw = load_workbook(url)
        pw_ac = pw.active

        list_temp = []

        for item in pw_ac['A'][1:]:
            id = str(item.value)
            line = item.row
            value = pw_ac[f'B{line}'].value

            if not value is None:
                value = f'{value:04d}'

                list_temp.append({
                    'id': id,
                    'value': str(value)
                })
        
        return list_temp

    def run_bot(self) -> None:
        self.init_driver()
        self.open_site('Troque a configuração do navegado para "Perguntar onde salvar cada arquivo"')

        list_temp = self._take_excel_file(f'{os.getcwd()}/excel_tables/table-with-the-timesheets-values/timesheets-values.xlsx')
        time.sleep(2)
        list_length = len(list_temp)
        i = 1

        for item in list_temp:
            print(f'{i}/{list_length} - Nome do Cliente: {item['id']}; Novo nome: {item['value']}')
            i += 1

            self._click_to_write()
            self._write_name(item['id'])
            self._first_element_click()
            self._download_timesheet()
            self._wait_element_load()
            self._write_name_file_and_save(item["value"])
            self._continue_btn()


        input("Digite qualquer tecla para finalizar: ")