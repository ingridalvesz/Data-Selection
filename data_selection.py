import pandas as pd

emissoes_gases = pd.read_excel('1-SEEG10_GERAL-BR_UF_2022.10.27-FINAL-SITE.xlsx', sheet_name = 'GEE Estados')
emissoes_gases.head()

emissoes_gases.info()

emissoes_gases['Emissão / Remoção / Bunker'].unique()

(emissoes_gases['Emissão / Remoção / Bunker'] == 'Remoção NCI') | (emissoes_gases['Emissão / Remoção / Bunker'] == 'Remoção')

emissoes_gases[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção'])]
# para escrever diversos valores na mesma linha utilizaremos o .isin

emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção']), 1970:2021]

emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção']), 1970:2021]

emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'].isin(['Remoção NCI', 'Remoção']), 1970:2021].max()

emissoes_gases.loc[emissoes_gases['Emissão / Remoção / Bunker'] == 'Bunker', 'Estado'].unique()
# identificado com o .unique que a coluna está vazia (array([nan], dtype=object) nos dados Bunker e Estados.

emissoes_gases = emissoes_gases[emissoes_gases['Emissão / Remoção / Bunker'] == 'Emissão']
emissoes_gases
# aqui está igualando com == para a função ser somente de 'Emissão'

emissoes_gases = emissoes_gases.drop(columns= 'Emissão / Remoção / Bunker')
emissoes_gases
# apagando a coluna com .drop()

emissoes_gases.loc[:, 'Nível 1 - Setor':'Produto'].columns
# localizando as colunas desejadas

colunas_info = list(emissoes_gases.loc[:, 'Nível 1 - Setor':'Produto'].columns)
colunas_info
# salvando em uma list() as colunas desejadas

emissoes_gases.loc[:, 1970:2021].columns

colunans_emissao = list(emissoes_gases.loc[:, 1970:2021].columns)
colunans_emissao

emissoes_gases.melt(id_vars = colunas_info, value_vars = colunans_emissao, var_name = 'Ano', value_name = 'Emissao')

emissoes_por_ano = emissoes_gases.melt(id_vars = colunas_info, value_vars = colunans_emissao, var_name = 'Ano', value_name = 'Emissao')

emissoes_por_ano.groupby('Gás')
#para somar a coluna "Emissão" com base nos tipos de gás da coluna "Gás" usamos o grupby()

emissoes_por_ano.groupby('Gás').groups

emissoes_por_ano.groupby('Gás').get_group('CO2 (t)')

emissoes_por_ano.groupby('Gás').sum(numeric_only = True)
# %%