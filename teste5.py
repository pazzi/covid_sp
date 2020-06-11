import csv
import requests

url = 'https://raw.githubusercontent.com/seade-R/dados-covid-sp/master/data/dados_covid_sp.csv'
response = requests.get(url)        

with open('out.csv', 'w') as f:
	writer = csv.writer(f)
	for line in response.iter_lines():
		writer.writerow(line.decode('utf-8').split(','))

with open('out.csv') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=';')
	den=[]
	print(reader)
	for row in reader:
		print(row['nome_munic'])
		den.append(row['nome_munic'])
print(den)

