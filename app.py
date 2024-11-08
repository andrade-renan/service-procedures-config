import pandas as pd
import json

# Criar uma base de dados com os procedimentos e seus valores, e uma estrutura que relaciona serviços e procedimentos
with open('data\procedures.json', 'r', encoding='utf-8') as file:
    procedures = json.load(file)

# Serviços e os procedimentos que os compõem
with open('data\services.json', 'r', encoding='utf-8') as file:
    services = json.load(file)


# Calculando o total e comisão para cada serviço
results = {}
for service, steps in services.items():
    total_cost = sum([procedures[step]['Valor'] for step in steps])
    total_commission = sum([procedures[step]['Repasse'] for step in steps])
    total_time = sum([procedures[step]['Tempo'] for step in steps])
    results[service] = {"Valor Total": total_cost, "Comissão": total_commission, "Porcentagem de Comissão": total_commission/total_cost, "Tempo": total_time}


# Criar uma planilha usando pandas
df_services = pd.DataFrame.from_dict(results, orient='index')

# Salvar em um arquivo Excel para fácil edição
file_path = 'data\Servicos_Etapas.xlsx'
with pd.ExcelWriter(file_path) as writer:
    df_services.to_excel(writer, sheet_name='Valores_Serviços')

df_services, file_path