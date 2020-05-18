import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
df=pd.read_csv("https://raw.githubusercontent.com/seade-R/dados-covid-sp/master/data/dados_covid_sp.csv", sep=";", encoding="utf-8")
f=open("saida.txt", "a")
def dados(cidade):
	print(cidade)
	f.write(cidade + '\n')
	filt=df['nome_munic'] == cidade
	pop=df[filt]['pop'].tolist()
	print("Populacao:" + str(pop[0]))
	f.write("Populacao:" + str(pop[0]) + '\n')
	total = df[filt]['obitos'].tolist()
	print("Obitos:" + str(total[len(total)-1]))
	f.write("Obitos:" + str(total[len(total)-1]) + '\n')
	print("Indice (obitos):" + str(total[len(total)-1]/pop[0]))
	f.write("Indice (obitos):" + str(total[len(total)-1]/pop[0]) + '\n')
	total=df[filt]['casos'].tolist()
	print("Total de casos:" + str(total[len(total)-1]))
	f.write("Total de casos:" + str(total[len(total)-1]) + '\n')
	print("Indice (casos):" + str(total[len(total)-1]/pop[0]))
	f.write("Indice (casos):" + str(total[len(total)-1]/pop[0]) + '\n')
	hoje=df[filt]['casos_novos'].tolist()
	print("Casos hoje:" + str(hoje[len(total)-1]))
	f.write("Casos hoje:" + str(hoje[len(total)-1])+ '\n')
	print("***************************************************")
	f.write("***************************************************\n")
cidades=df['nome_munic'].tolist()
cidades_un = list(dict.fromkeys(cidades))
cidades_un.sort()

for cidade in cidades_un:
	dados(cidade)
f.close()
