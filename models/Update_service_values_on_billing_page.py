from models.Bot import Bot
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from openpyxl import load_workbook
import time
import os

class Update_service_values_on_billing_page(Bot):
    """Update the service value in the Service Parameterization module."""

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

            if name is not None:
                total_value = f'{total_value:.2f}0'
                vt = f'{(vt*100):.4f}'
                va = f'{(va*100):.4f}'
                inss_base = f'{(inss_base*100):.4f}'
                net_value = f'{net_value:.2f}'

                list_temp.append({
                    'name': str(name),
                    'fiscalName': str(fiscal_name),
                    'total': str(total_value),
                    'vt': str(vt),
                    'va': str(va),
                    'inssBase': str(inss_base),
                    'netValue': str(net_value)
                })
        
        return list_temp
    
    def _write_value_in_an_element(self, xpath: str, value: str) -> None:
        #Enter the value inside the specified element.
        input = self.driver.find_element(By.XPATH, xpath)
        input.click()
        time.sleep(0.2)
        input.send_keys(Keys.CONTROL, 'a')
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
    
    def _check_services_and_click_edit_btn(self) -> None:
        #Review the services list and select "CONTRATO" for value edit.
        input = self.driver.find_element(By.XPATH, "//div[@class='listagem-finais']//div[@class='v-text-field__slot']//input")
        input.click()
        time.sleep(0.2)
        input.send_keys(Keys.CONTROL, 'a')
        time.sleep(0.3)
        input.send_keys('CONTRATO')

        tr_list = self.driver.find_elements(By.XPATH, "//tr[@class='ATIVO']")
        for tr in tr_list:
            td_list = tr.find_elements(By.XPATH, ".//td")
            if 'contrato' in td_list[0].text.lower():
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

    def run_bot(self):
        self.init_driver()
        list_temp = self._take_excel_file(f'{os.getcwd()}/excel_tables/tables-with-the-billing-values/billing-values.xlsx')
        self.open_site()
        list_length = len(list_temp)
        i = 1

        for item in list_temp:

            print(f'{i}/{list_length} | Nome do Cliente: {item['name']} | Valor: {item['total']}')
            i += 1

            #Search for the client in the filter.
            self._write_value_in_an_element("//div[@class='col-md-5 col-12']//input", item['name'])
            time.sleep(2)
            
            #Check if the element was found and click the "Edit" button.
            if self._check_Element("//tr[@class='ATIVO']", 300):
                self._check_elements_and_click_edit_btn(item['name'])
            time.sleep(1)
            
            #Filter by the name "Contract" and click the "Edit" button.
            self._check_services_and_click_edit_btn()
            time.sleep(0.5)
            
            #Enter the new contract value in the specified element.
            self._write_value_in_an_element("//div[@class='v-card v-sheet theme--light']//div[@class='v-text-field__prefix']/following-sibling::input[1]", item['total'])
            time.sleep(0.5)

            #Click the "Save" button inside the contract element.
            self._click_btn("//div[@class='v-card v-sheet theme--light']//button[2]")
            time.sleep(1)

            #Click the "Save" button on the value confirmation card.
            if self._check_Element("//div[@class='swal2-actions']", 300):
                self._click_btn("//div[@class='swal2-actions']//button[@class='swal2-confirm swal2-styled']")
            else:
                break

            #Click the "Save" button to save the service changes.
            self._click_btn("//button[@type='submit']")
            time.sleep(0.5)
            
            #Click the confirmation button to save the service changes.
            if self._check_Element("//button[@id='btn-modal-sucesso-nao']", 300):
                self._click_btn("//button[@id='btn-modal-sucesso-nao']")
            else:
                break
            time.sleep(3)

        input("Digite qualquer tecla para finalizar: ")
        self.driver.quit()