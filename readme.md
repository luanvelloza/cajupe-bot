# **🄲🄰🄹🅄🄿🄴 🄱🄾🅃**

## **Índice**

1. [Introdução](#1-introdução)
2. [Instalação](#2-instalação)
   - 2.1 [Pré-requisitos](#21-pré-requisitos)
   - 2.2 [Passo 1: Clonar o repositório](#22-passo-1-clonar-o-repositório)
   - 2.3 [Passo 2: Criar um ambiente virtual (venv)](#23-passo-2-criar-um-ambiente-virtual-venv)
   - 2.4 [Passo 3: Ativar o ambiente virtual](#24-passo-3-ativar-o-ambiente-virtual)
   - 2.5 [Passo 4: Instalar as dependências](#25-passo-4-instalar-as-dependências)
   - 2.6 [Executar o programa](#26-executar-o-programa)
   - 2.7 [Passo 6: Desativar o ambiente virtual (opcional)](#27-passo-6-desativar-o-ambiente-virtual-opcional)
3. [Funcionalidades](#3-funcionalidades)
   - 3.1 [Inserir valores do rateio em Títulos a Pagar (Apportion_accounts_payable)](#31-inserir-valores-do-rateio-em-títulos-a-pagar-apportion_accounts_payable)
     - 3.1.1 [Contexto e solução do Problema](#311-contexto-e-solução-do-problema)
     - 3.1.2 [Como usar](#312-como-usar)
       - 3.1.2.1 [Preparando a planilha de referência](#3121-preparando-a-planilha-de-referência)
       - 3.1.2.2 [Execução do programa](#3122-execução-do-programa)
   - 3.2 [Baixar boletos (Download_bills)](#32-baixar-boletos-download_bills)
     - 3.2.1 [Contexto e solução do Problema](#321-contexto-e-solução-do-problema)
     - 3.2.2 [Como usar](#322-como-usar)
       - 3.2.2.1 [Preparando a planilha de referência](#3221-preparando-a-planilha-de-referência)
       - 3.2.2.2 [Execução do programa](#3222-execução-do-programa)
   - 3.3 [Baixar folhas de ponto (Download_timesheets)](#33-baixar-folhas-de-ponto-download_timesheets)
     - 3.3.1 [Contexto e Solução do Problema](#331-contexto-e-solução-do-problema)
     - 3.3.2 [Como usar](#332-como-usar)
       - 3.3.2.1 [Preparando a planilha de referência](#3321-preparando-a-planilha-de-referência)
       - 3.3.2.2 [Execução do programa](#3322-execução-do-programa)
   - 3.4 [Inserir Taxas dos Serviços (Update_billing_tax_info)](#34-inserir-taxas-dos-serviços-update_billing_tax_info)
     - 3.4.1 [Contexto e Solução do Problema](#341-contexto-e-solução-do-problema)
     - 3.4.2 [Como usar](#342-como-usar)
       - 3.4.2.1 [Preparando a planilha de referência](#3421-preparando-a-planilha-de-referência)
       - 3.4.2.2 [Execução do programa](#3422-execução-do-programa)
   - 3.5 [Inserir Valores dos Serviços (Update_service_values_on_billing_page)](#35-inserir-valores-dos-serviços-update_service_values_on_billing_page)
     - 3.5.1 [Contexto e Solução do Problema](#351-contexto-e-solução-do-problema)
     - 3.5.2 [Como usar](#352-como-usar)
       - 3.5.2.1 [Preparando a planilha de referência](#3521-preparando-a-planilha-de-referência)
       - 3.5.2.2 [Execução do programa](#3522-execução-do-programa)
4. [Tecnologias](#4-tecnologias)

## **1. Introdução**

O Cajupe Bot foi desenvolvido para otimizar e simplificar processos no ambiente de trabalho, automatizando tarefas manuais e repetitivas que surgem ao integrar a cultura organizacional e as demandas do escritório com o aplicativo [Cajupe](https://objetivar.com.br/) (um sistema de gestão empresarial). Com ele, se ganha eficiência e reduz erros operacionais.

## **2. Instalação**

Siga os passos abaixo para configurar e executar o projeto em sua máquina.

### **2.1. Pré-requisitos**

Antes de começar, verifique se você tem o Python (3.12) e o pip instalados em sua máquina. Além disso, é essencial que o Chromedriver esteja instalado e configurado corretamente.

Se precisar de ajuda para instalar o Chromedriver, consulte este guia detalhado: [Como instalar o Chromedriver no Windows 10](https://pt.linkedin.com/pulse/como-instalar-o-chromedriver-windows-10-jo%C3%A3o-gross).

### **2.2. Passo 1: Clonar o repositório**

Primeiro, clone o repositório do projeto para o seu ambiente local:

```bash
git clone https://github.com/luanvelloza/cajupe-bot.git
cd cajupe-bot
```

### **2.3. Passo 2: Criar um ambiente virtual (venv)**

Primeiro, clone o repositório do projeto para o seu ambiente local:

```bash
python -m venv venv
```

### **2.4. Passo 3: Ativar o ambiente virtual**

Ative o ambiente virtual que você acabou de criar:

#### **No Linux ou macOS:**
```bash
source venv/bin/activate
```

#### **No Windows:**
```bash
venv\Scripts\activate
```
### **2.5. Passo 4: Instalar as dependências**

Com o ambiente virtual ativado, instale as bibliotecas necessárias listadas no arquivo ```requirements.txt```:

```bash
pip install -r requirements.txt`
```

### **2.6. Executar o programa**

Após a instalação das dependências, você pode executar o programa com o seguinte comando: 

```bash
python app.py
```

### **2.7. Passo 6: Desativar o ambiente virtual (opcional)**

Quando terminar de usar o programa, você pode desativar o ambiente virtual com o comando:
```bash
deactivate
```

## **3. Funcionalidades**

### **3.1. Inserir valores do rateio em Títulos a Pagar (Apportion_accounts_payable)**

#### **3.1.1. Contexto e solução do Problema:**

**Contexto**

A empresa realiza compras em grande volume, que são posteriormente distribuídas entre diferentes tomadores (centros de custo). No sistema, é necessário inserir o valor total da compra (conforme especificado na Nota Fiscal) e realizar o rateio desses valores entre os tomadores. Esse controle era feito manualmente por meio de uma planilha do Excel, o que demandava tempo e estava sujeito a erros.

**Solução**

O Cajupe Bot utiliza uma planilha do Excel contendo duas colunas principais: "Nome do Centro de Custo" e "Valor".

Com base nesses dados, o script automatiza a inserção dos valores rateados no sistema, diretamente no título de pagamento correspondente. Isso elimina a necessidade de inserção manual, agiliza o processo e reduz a probabilidade de inconsistências."

#### **3.1.2. Como usar:**
##### **3.1.2.1. Preparando a planilha de referência**

Acesse o caminho ```./excel_tables/tables-with-the-apportionment-values``` e abra o arquivo ```apportionment-values.xlsx```.

Preencha a planilha com as seguintes informações:

Na coluna **"Centro de Custo"**, insira os nomes dos tomadores (centros de custo).

Na coluna **"Valor"**, insira os valores correspondentes a cada tomador.

Salve a planilha, mantendo-a na mesma pasta (```./excel_tables/tables-with-the-apportionment-values```).

Verifique se não há formatos inconsistentes ou células vazias na planilha, pois isso pode causar erros durante a execução do program

#### **3.1.2.2. Execução do programa**

1. **Ative o ambiente virtual**:
   - No **Linux/macOS**, use:
     ```bash
     source venv/bin/activate
     ```
   - No **Windows**, use:
     ```bash
     venv\Scripts\activate
     ```

2. **Execute o script principal**:
   No terminal, digite o seguinte comando para iniciar o Cajupe Bot:
   ```bash
   python app.py
   ```
3. **Selecione a funcionalidade:**
- Após a execução, o programa exibirá uma lista de funcionalidades disponíveis.

- Digite o número correspondente à funcionalidade desejada (Inserir Rateio (Títulos a Pagar)).

4. **Faça login no sistema:**
- Um navegador será aberto automaticamente.

- Insira suas credenciais de login no sistema Cajupe.

5. **Acesse o módulo "Títulos a Pagar":**
- Após o login, navegue até o módulo "Títulos a Pagar" no sistema Cajupe.

6. **Adicione um novo título:**
- Crie um novo título de pagamento no sistema.

7. **Inicie a automação**
- No console do terminal, pressione qualquer tecla para iniciar o processo de automação.

8. **Conclusão:**

- O Cajupe Bot executará automaticamente a inserção dos valores rateados com base na planilha de referência.
- Aguarde até que o processo seja concluído e verifique os resultados no sistema.
- Após a conferência, digite 1 para repetir o processo (atualizando a planilha com as novas informações) ou qualquer outra tecla para encerrar.


### **3.2. Baixar boletos (Download_bills)**

#### **3.2.1. Contexto e solução do Problema:**

**Contexto**

Mensalmente enviamos os boletos dos clientes por e-mail. O Cajupe já possui uma funcionalidade de envio automático de e-mail. Porém, devido às particularidades da empresa, precisamos baixar os boletos individuais e enviar junto com outras documentações. O sistema do Cajupe só nos permite baixar os boletos individualmente.

**Solução:**

O Cajupe Bot baixa os boletos de forma individual sem precisar de intervenção humana. 

#### **3.2.2. Como usar:**

##### **3.2.2.1. Preparando a planilha de referência**

1. **Faça login no sistema do Cajupe:**
- Abra o sistema do cajupe e insira suas credenciais de login no sistema Cajupe.

2. **Acesse o módulo "Documento faturamento":**
- Após o login, navegue até o módulo **"Documento faturamento"** no sistema Cajupe.

3. **Filtre por data:**
- No sistema, insira o período de emissão dos boletos que deseja baixar.

4. **Exportar e Renomear**
- Clique no botão Exportar para iniciar o processo de download.

- Após a conclusão do download, abra o arquivo e salve-o no formato `.xlsx`, renomeando-o como `bill-addresses.xlsx.`

- Salve o arquivo na pasta especificada: `./excel_tables/table-with-the-bill-addresses.`

##### **3.2.2.2. Execução do programa**

1. **Ative o ambiente virtual**:
   - No **Linux/macOS**, use:
     ```bash
     source venv/bin/activate
     ```
   - No **Windows**, use:
     ```bash
     venv\Scripts\activate
     ```

2. **Execute o script principal**:
   No terminal, digite o seguinte comando para iniciar o Cajupe Bot:
   ```bash
   python app.py
   ```
3. **Selecione a funcionalidade:**
- Após a execução, o programa exibirá uma lista de funcionalidades disponíveis.

- Digite o número correspondente à funcionalidade desejada (Baixar Boletos (Faturamento)).

4. **Escreva o link da pasta de destino:**
- Digite o caminho completo da pasta de destino sem utilizar aspas. Exemplo: `C:\User\Área de Trabalho\Boletos.`

- Se desejar sair, basta digitar `2`.

5. **Conclusão:**
- O Cajupe Bot iniciará o download dos boletos, utilizando como referência a planilha previamente preparada.

- Aguarde até que o processo seja finalizado e, em seguida, verifique os boletos na pasta de download selecionada.

### **3.3. Baixar folhas de ponto (Download_timesheets)**

#### 3.3.1 Contexto e Solução do Problema:

**Contexto:**

Mensalmente precisamos enviar as folhas de ponto para os clientes dos colaboradores alocados. O Cajupe nos permite baixar as folhas de ponto por cliente, porém não nos permite baixar todos de uma vez em uma pasta compactada dividida por cliente.

**Solução:**

O Cajupe Bot baixa as folhas de ponto por cliente de forma individual.

#### **3.3.2 Como usar:**
##### **3.3.2.1. Preparando a planilha de referência**

Acesse o caminho ```./excel_tables/table-with-the-timesheets-values``` e abra o arquivo ```timesheets-values.xlsx```.

Preencha a planilha com as seguintes informações:

Na coluna **"Centro de Custo"**, insira os nomes dos tomadores (centros de custo).

Na coluna **"ID. Centro de Custo"**, insira os números de identificação correspondentes a cada tomador.

Salve a planilha, mantendo-a na mesma pasta (```./excel_tables/table-with-the-timesheets-values```).

Verifique se não há formatos inconsistentes, pois isso pode causar erros durante a execução do programa

#### **3.1.2.2. Execução do programa**

1. **Ative o ambiente virtual**:
   - No **Linux/macOS**, use:
     ```bash
     source venv/bin/activate
     ```
   - No **Windows**, use:
     ```bash
     venv\Scripts\activate
     ```

2. **Execute o script principal**:
   No terminal, digite o seguinte comando para iniciar o Cajupe Bot:
   ```bash
   python app.py
   ```
3. **Selecione a funcionalidade:**
- Após a execução, o programa exibirá uma lista de funcionalidades disponíveis.

- Digite o número correspondente à funcionalidade desejada (Baixar Folhas de Ponto (Cálculo de Ponto)).

4. **Faça login no sistema:**
- Um navegador será aberto automaticamente.

- Insira suas credenciais de login no sistema Cajupe.

5. **Acesse o módulo "Cálculo de Ponto":**
- Após o login, navegue até o módulo "Cálculo de Ponto" no sistema Cajupe.

6. **Insira o período desejado:**
- No sistema, selecione o período correspondente às folhas de ponto que deseja baixar.

7. **Configure a pasta de download:**
- Acesse as configurações do navegador e ajuste para que ele **pergunte o local de destino** ao baixar arquivos.

- Certifique-se de selecionar uma pasta de fácil acesso para armazenar as folhas de ponto.

8. **Inicie a automação**
- No console do terminal, pressione **qualquer tecla** para iniciar o processo de automação.

8. **Conclusão:**

- O Cajupe Bot executará automaticamente o download das folhas de ponto por cliente.

- Aguarde até que o processo seja concluído e verifique as folhas de ponto na pasta de download selecionada.

### **3.4. Inserir Taxas dos Serviços (Update_billing_tax_info)**

#### **3.4.1 Contexto e Solução do Problema:**

**Contexto**

A empresa usa uma planilha Excel para controlar os valores pagos aos clientes, bem como as estimativas de impostos. Com isso, mensalmente, antes do faturamento, precisamos repassar as porcentagens dos serviços prestados aos clientes para o sistema do Cajupe, o que demanda tempo e esforço.

**Solução**:

O Cajupe Bot, a partir da tabela Excel, insere as porcentagens dos serviços prestados aos clientes no sistema.

#### **3.4.2 Como usar:**
##### **3.4.2.1. Preparando a planilha de referência**

Acesse o caminho ```./excel_tables/tables-with-the-billing-values``` e abra o arquivo ```billing-values.xlsx```.

Preencha a planilha com as seguintes informações:
  - **CNPJ:** Insira o CNPJ do cliente.
  - **CLIENTE:** Insira o nome do cliente.
  - **Nome serviço (descrição):** Descreva o serviço prestado.
  - **Parametrização fiscal:** Informe o regime fiscal aplicável (ex: Simples Nacional, Lucro Presumido, Lucro Real).
  - **VLR ANO 2024:** Insira o valor total do serviço para o ano de 2024.
  - **%pessoas (vt):** Informe a porcentagem do valor referente a custos com pessoal.
  - **%material (va):** Informe a porcentagem do valor referente a custos com materiais.
  - **PERCENTUAL:** Insira o percentual referente à base de cálculo do INSS.
  - **BOLETO:** Insira o número do boleto associado ao serviço.
 
Salve a planilha, mantendo-a na mesma pasta (```./excel_tables/tables-with-the-billing-values```).

Verifique se não há formatos inconsistentes, pois isso pode causar erros durante a execução do programa

#### **3.1.2.2. Execução do programa**

1. **Ative o ambiente virtual**:
   - No **Linux/macOS**, use:
     ```bash
     source venv/bin/activate
     ```
   - No **Windows**, use:
     ```bash
     venv\Scripts\activate
     ```
2. **Execute o script principal**:
   No terminal, digite o seguinte comando para iniciar o Cajupe Bot:
   ```bash
   python app.py
   ```
3. **Selecione a funcionalidade:**
- Após a execução, o programa exibirá uma lista de funcionalidades disponíveis.

- Digite o número correspondente à funcionalidade desejada (Inserir Taxas dos Serviços (Parametrização Fiscal)).

4. **Faça login no sistema:**
- Um navegador será aberto automaticamente.

- Insira suas credenciais de login no sistema Cajupe.

5. **Acesse o módulo "Parametrização Serviços":**
- Após o login, navegue até o módulo "Parametrização Fiscal" no sistema Cajupe.

6. **Inicie a automação**
- No console do terminal, pressione **qualquer tecla** para iniciar o processo de automação.

7. **Conclusão:**

- O Cajupe Bot parametrizará o sistema cliente por cliente, inserindo automaticamente as novas taxas.

- Aguarde até que o processo seja concluído e verifique as atualizações no sistema

### **3.5. Inserir Valores dos Serviços (Update_service_values_on_billing_page)**

#### **3.5.1. Contexto e Solução do Problema:**

**Problema**

A empresa usa uma planilha Excel para controlar os valores pagos aos clientes, bem como as estimativas de impostos. Com isso, mensalmente, antes do faturamento, precisamos repassar os novos valores para o Cajupe, o que demanda tempo e esforço.

**Solução**

O Cajupe Bot, a partir da tabela Excel da empresa, insere os valores dos serviços prestados aos clientes.

#### **3.5.2. Como usar:**
##### **3.5.2.1. Preparando a planilha de referência**

Acesse o caminho ```./excel_tables/tables-with-the-billing-values``` e abra o arquivo ```billing-values.xlsx```.

Preencha a planilha com as seguintes informações:
  - **CNPJ:** Insira o CNPJ do cliente.
  - **CLIENTE:** Insira o nome do cliente.
  - **Nome serviço (descrição):** Descreva o serviço prestado.
  - **Parametrização fiscal:** Informe o regime fiscal aplicável (ex: Simples Nacional, Lucro Presumido, Lucro Real).
  - **VLR ANO 2024:** Insira o valor total do serviço para o ano de 2024.
  - **%pessoas (vt):** Informe a porcentagem do valor referente a custos com pessoal.
  - **%material (va):** Informe a porcentagem do valor referente a custos com materiais.
  - **PERCENTUAL:** Insira o percentual referente à base de cálculo do INSS.
  - **BOLETO:** Insira o número do boleto associado ao serviço.
 
Salve a planilha, mantendo-a na mesma pasta (```./excel_tables/tables-with-the-billing-values```).

Verifique se não há formatos inconsistentes, pois isso pode causar erros durante a execução do programa

#### **3.1.2.2. Execução do programa**

1. **Ative o ambiente virtual**:
   - No **Linux/macOS**, use:
     ```bash
     source venv/bin/activate
     ```
   - No **Windows**, use:
     ```bash
     venv\Scripts\activate
     ```

2. **Execute o script principal**:
   No terminal, digite o seguinte comando para iniciar o Cajupe Bot:
   ```bash
   python app.py
   ```
3. **Selecione a funcionalidade:**
- Após a execução, o programa exibirá uma lista de funcionalidades disponíveis.

- Digite o número correspondente à funcionalidade desejada (Inserir Valores dos Serviços (Parametrização de Serviços)).

4. **Faça login no sistema:**
- Um navegador será aberto automaticamente.

- Insira suas credenciais de login no sistema Cajupe.

5. **Acesse o módulo "Parametrização Serviços":**
- Após o login, navegue até o módulo "Parametrização Serviços" no sistema Cajupe.

6. **Inicie a automação**
- No console do terminal, pressione **qualquer tecla** para iniciar o processo de automação.

7. **Conclusão:**

- O Cajupe Bot parametrizará o sistema cliente por cliente, inserindo automaticamente os novos valores dos serviços.

- Aguarde até que o processo seja concluído e verifique as atualizações no sistema.

## **4. Tecnologias**

- **Python:** Linguagem de programação principal.
- **Selenium:** Automação de navegador.
- **PyAutoGUI:** Automação de interface gráfica.
- **Pandas:** Extração de dados.
