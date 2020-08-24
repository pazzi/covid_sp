import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

def dados(cidade,df1,x):
        print(x)
        print(cidade)
        f.write(str(x) + ' - ')
        f.write(cidade + '\n')
        filt=df1['nome_munic'] == cidade
        dia=df1[filt]['datahora'].tolist()
        print("Dia:{}".format(dia[0]))
        f.write("Dia:{}".format(dia[0]) + '\n')
        pop=df1[filt]['pop'].tolist()
        print("Populacao:" + str(pop[0]))
        f.write("Populacao:" + str(pop[0]) + '\n')
        total = df1[filt]['obitos'].tolist()
        print("Obitos:{}".format(total[0]))
        f.write("Obitos:" + str(total[0]) + '\n')
        print("Indice (obitos):" + str(total[0]/pop[0]))
        f.write("Indice (obitos):" + str(total[0]/pop[0]) + '\n')
        total=df1[filt]['casos'].tolist()
        print("Total de casos:" + str(total[0]))
        f.write("Total de casos:" + str(total[0]) + '\n')
        print("Indice (casos):" + str(total[0]/pop[0]))
        f.write("Indice (casos):" + str(total[0]/pop[0]) + '\n')
        hoje=df1[filt]['casos_novos'].tolist()
        print("Casos hoje:" + str(hoje[0]))
        f.write("Casos hoje:" + str(hoje[0])+ '\n')
        print("***************************************************")
        f.write("***************************************************\n")

df=pd.read_csv("https://raw.githubusercontent.com/seade-R/dados-covid-sp/master/data/dados_covid_sp.csv", sep=";", encoding="utf-8")
f=open("saida.txt", "a")
df.sort_values(by=['casos'], inplace=True, ascending=False)
filt = (df['datahora'] == df['datahora'].max())
df1 = df[filt]
cidades=df1['nome_munic'].tolist()
cidades_un = list(dict.fromkeys(cidades))
#cidades_un.sort()
x=0
for cidade in cidades_un:
	if cidade != "Ignorado":
		x+=1
		dados(cidade,df,x)
f.close()
