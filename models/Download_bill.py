from models.Bot import Bot
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import pyautogui
import pandas as pd
import requests
import os

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

class Download_bill_v2():
    """Downloads customer bills using the link provided in the bill-addresses.xlsx"""

    def _ask_folder_path(self) -> str:
        """
            Prompts the user for the destination folder path of downloaded files and validates the address.

            Output:
                - A string containing the variable's address if the path is valid.
                - An empty string if the user chooses to exit the system.
        """

        while True:
            url = input("Informe o endereço da pasta de destino dos downloads (Sem Aspas): ")

            if url == "2":
                print("Voltando ao menu de seleção.")
                return ""
            
            if os.path.exists(url):
                return url
            
            print("Endereço de pasta inválido! Por favor, tente novamente ou digite dois para voltar ao menu de seleção.")


    def run_download(self) -> None:
        """Script designed to automate the bill download process"""

        #Stores the data extracted from the spreadsheet
        url_excel_file = f'{os.getcwd()}/excel_tables/table-with-the-bill-addresses/bill-addresses.xlsx'
        df = pd.read_excel(url_excel_file)

        name_document_column = "Numero_Documento"
        links_bill_column = "Boleto"

        #Prompts the user to specify the destination folder the downloaded bills
        save_folder_path_url = self._ask_folder_path()
        if not save_folder_path_url:
            return

        #Iterates through the list and download bills one by one
        for index, row in df.iterrows():

            #Check if the column containing the document name and the invoice link is present in the spreadsheet.
            try:
                document_name = row[name_document_column]
                link_bill = row[links_bill_column]

            except Exception as e:
                print(f" Coluna {e} não encontrada! Por favor, tente novamente.")
                return    

            #Check if the link exists.
            if not link_bill:
                print(f"{document_name}: não possui link de downlod do boleto.")
                continue

            #Download the bill and save them in the selected folder. 
            try:
                request = requests.get(link_bill)
                request.raise_for_status()

                new_file_name = f"{save_folder_path_url}\\{document_name}.pdf"
                with open(new_file_name, "wb") as f:
                    f.write(request.content)
                
            except Exception as e:
                print(f"Erro ao baixar o link {link_bill}: {e}")
        
        print("Download dos Boletos Finalizados!")