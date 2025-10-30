from models.Bot import Bot
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from openpyxl import load_workbook
import time
import os

class Update_billing_tax_info(Bot):
    """Update the percentages in the Fiscal Parameterization module."""

    def _take_excel_file(self, url: str) -> dict:
        """
            Take a excel file and return a list of yours elements

            input:
                - file excel' URL

            output:
                - dict with: name, fiscalName, total, vt, va, inssBase, netValue. 
        """

        pw = load_workbook(url)
        pw_ac = pw.active

        list_temp = []

        for item in pw_ac['C'][1:]:
            name = item.value
            line = item.row
            fiscal_name = pw_ac[f'D{line}'].value
            total_value = pw_ac[f'E{line}'].value
            vt = pw_ac[f'F{line}'].value
            va = pw_ac[f'G{line}'].value
            inss_base = pw_ac[f'H{line}'].value
            net_value = pw_ac[f'I{line}'].value

            if not name is None:
                total_value = f'{total_value:.2f}0'
                vt = f'{(vt*100):.4f}'
                va = f'{(va*100):.4f}'
                inss_base = f'{(inss_base*100):.5f}'
                net_value = f'{net_value:.2f}'

                list_temp.append({
                    "name": str(name),
                    "fiscalName": str(fiscal_name),
                    "total": str(total_value),
                    "vt": str(vt),
                    "va": str(va),
                    "inssBase": str(inss_base),
                    "netValue": str(net_value)
                })
        
        return list_temp
    
    def _write_value_in_an_element(self, xpath: str, value: str) -> None:
        #Enter the value inside the specified element.
        input = self.driver.find_element(By.XPATH, xpath)
        input.click()
        time.sleep(0.2)
        input.send_keys(Keys.CONTROL, "a")
        time.sleep(0.3)
        input.send_keys(value)

    def _check_elements_and_click_edit_btn(self, value: str) -> None:
        #Check if the element exists and click on "Edit."
        tr_list = self.driver.find_elements(By.XPATH, "//tr[@class='ATIVO']")
        for tr in tr_list:
            td_list = tr.find_elements(By.XPATH, ".//td")
            if td_list[0].text == value:
                btn_element = tr.find_element(By.XPATH, ".//button[@title='Editar']")
                btn_element.click()
                break
    
    def _check_fiscal_elements_and_click_edit_btn(self) -> None:
        #Review the tax list and select INSS for value editing.
        tr_list = self.driver.find_elements(By.XPATH, "//tr[@class='ATIVO']")
        for tr in tr_list:
            td_list = tr.find_elements(By.XPATH, ".//td")
            if "inss" in td_list[0].text.lower():
                btn_element = tr.find_element(By.XPATH, ".//button")
                btn_element.click()
                break

    def _click_btn(self, xpath: str) -> None:
        #Click on the specified button.
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()

    def _check_Element(self, xpath: str, time: int) -> bool:
        '''
            Check if the element exist and load. If don't load, returns False
        
            Input:
                - xpath - str - (element's xpath)
                - time - int - (How mach time need to load)

            Output:
                - True
                - False
        '''
        
        try:
            wait = WebDriverWait(self.driver, timeout=time)
            return wait.until(lambda d: self.driver.find_element(By.XPATH, xpath).is_displayed())
        except:
            return False  

    def run_bot(self) -> None:
        self.init_driver()
        list_temp = self._take_excel_file(f'{os.getcwd()}/excel_tables/tables-with-the-billing-values/billing-values.xlsx')
        self.open_site()
        list_length = len(list_temp)
        i = 1

        for item in list_temp:

            print(f'{i}/{list_length} | Nome do Cliente: {item['name']} | BASE: {item['inssBase']} | VT: {item['vt']} | VA {item['va']} ')
            i += 1

            #Search for the element in the filter.
            self._write_value_in_an_element("//div[@class='col-md-5 col-12']//input", item['name'])
            time.sleep(2)
            
            #Check the list and select the element with the same name.
            if self._check_Element("//tr[@class='ATIVO']", 300):
                self._check_elements_and_click_edit_btn(item['fiscalName'])
                time.sleep(1)
            
            #Locate the INSS field and click on "Edit."
            self._check_fiscal_elements_and_click_edit_btn()
            time.sleep(0.5)
            
            #Enter the INSS Base Value
            self._write_value_in_an_element("//div[@class='v-card__text']//div[@class='v-text-field__slot']//label[text()='Base Tributação']/following-sibling::input[1]", item['inssBase'])
            time.sleep(0.5)

            #Enter the VT (Vale Transporte) variable value.
            self._write_value_in_an_element("//div[@class='v-card__text']//div[@class='v-text-field__slot']//label[text()='Base % VT']/following-sibling::input[1]", item['vt'])
            time.sleep(0.5)

            #Enter the VA (Vale Alimentação) variable value.
            self._write_value_in_an_element("//div[@class='v-card__text']//div[@class='v-text-field__slot']//label[text()='Base % VA']/following-sibling::input[1]", item['va'])
            time.sleep(0.5)

            #Click the "Save" button on the card with the values.
            self._click_btn("//div[@class='v-card v-sheet theme--light']//button[2]")
            time.sleep(1)

            #Click the "Save" button to save the data.
            self._click_btn("//button[@type='submit']")
            time.sleep(0.5)
            
            #Click the confirmation button on the save confirmation card.
            if self._check_Element("//button[@id='btn-modal-sucesso-nao']", 300):
                self._click_btn("//button[@id='btn-modal-sucesso-nao']")
            else:
                break
            time.sleep(3)

        input("Digite qualquer tecla para finalizar: ")
        self.driver.quit()
