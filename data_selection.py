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

# %%