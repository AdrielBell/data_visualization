import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lê os dados do arquivo CSV
df = pd.read_csv('imigrantes_canada.csv')

# Define 'País' como índice
df.set_index('País', inplace=True)

# Seleciona os anos desejados
anos = list(map(str, range(1980, 2014)))

# Seleciona os dados para o Brasil
brasil = df.loc['Brasil', anos]

# Seleciona os dados para a Argentina
argentina = df.loc['Argentina', anos]

# Cria DataFrames para os dados do Brasil e Argentina
dados_brasil = pd.DataFrame({'ano': brasil.index, 'imigrantes_Brasil': brasil.values})
dados_argentina = pd.DataFrame({'ano': argentina.index, 'imigrantes_Argentina': argentina.values})

# Converte os anos para inteiros
dados_brasil['ano'] = dados_brasil['ano'].astype(int)
dados_argentina['ano'] = dados_argentina['ano'].astype(int)

# Mudar o estilo do gráfico
sns.set(style="darkgrid")

# Cria o gráfico
plt.figure(figsize=(8,4))
plt.plot(dados_brasil['ano'], dados_brasil['imigrantes_Brasil'], label='Brasil', marker='o')
plt.plot(dados_argentina['ano'], dados_argentina['imigrantes_Argentina'], label='Argentina', marker='o')

# Adiciona título e rótulos aos eixos
plt.title('Imigrantes do Brasil e Argentina para o Canadá (1980-2013)')
plt.xlabel('Ano')
plt.ylabel('Número de Imigrantes')
plt.legend()

# Exibe o gráfico
plt.show()
