import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
print("Baixando o banco de dados......")
df=pd.read_csv("https://raw.githubusercontent.com/seade-R/dados-covid-sp/master/data/dados_covid_sp.csv", sep=";", encoding="utf-8")
cidade = str(input("Informe o nome da cidade: "))
filt1=(df['nome_munic'] == cidade)
x=(df[filt1]['datahora']).tolist()
y=(df[filt1]['casos']).tolist()
z=(df[filt1]['casos_novos']).tolist()
tot=len(z)-1
ini=0
while ini <= tot:
	print(x[ini].ljust(10, ' '), end="")
	print(str(z[ini]).rjust(5, ' '), end="")
	print(str(y[ini]).rjust(5, ' '))
	ini += 1

fig, ax = plt.subplots()
ax.plot(x, y, label='casos')
ax.plot(x, z, label='casos novos')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_title("Grafico")
ax.legend(cidade)
plt.show()

