import csv
import pandas as pd

# Open
print("Abrindo arquivos usando o open")
file = open("pessoal.csv", "r")
content = file.read()
print(content)

# CSV 
with open("pessoal.csv", "r") as file:
  file_csv = csv.reader(file, delimiter=";")
  for i, linha in enumerate(file_csv):
    if i == 0:
      print(f"Cabecalho: {str(linha)}")
    else:
      print(f"Valor: {str(linha)}")

# Pandas
table = pd.read_csv("pessoal.csv",  sep=";")
print(table)