import os
from models.Apportion_accounts_payable import Apportion_accounts_payable
from models.Download_timesheets import Download_timesheets
from models.Download_bill import Download_bill_v2
from models.Update_service_values_on_billing_page import Update_service_values_on_billing_page
from models.Update_billing_tax_info import Update_billing_tax_info

def logo():
    print("Bem vindo! Ao: 🄲🄰🄹🅄🄿🄴 🄱🄾🅃")
    print("")

def selection_menu():
    print("""
    Selecione um numero:
    
    Documentos do Faturamento:
        1. Baixar Boletos (Faturamento);
        2. Baixar Folhas de Ponto (Cálculo de Ponto);
        3. Inserir Valores dos Serviços (Parametrização de Serviços);
        4. Inserir Taxas dos Serviços (Parametrização Fiscal).
    
    Títulos a Pagar
        5. Inserir Rateio (Títulos a Pagar).
    
    Outros:
        6. Sair do Sistema.
      
    """)
    main_menu()

def main_menu():
    number = int(input("Selecione um numero: "))
    match number:
        case 1:
            bot = Download_bill_v2()
            bot.run_download()
        case 2:
            bot = Download_timesheets()
            bot.run_bot()
        case 3:
            bot = Update_service_values_on_billing_page()
            bot.run_bot()
        case 4:
            bot = Update_billing_tax_info()
            bot.run_bot()
        case 5:
            bot = Apportion_accounts_payable()
            bot.run_bot()
        case 6:
            os.system("cls")
            print ("Saíndo do sistema...")     
        case _:
            print ("Selecione um numero de um a 4")


def main():
    logo()
    selection_menu()

if __name__ == '__main__':
    main()









