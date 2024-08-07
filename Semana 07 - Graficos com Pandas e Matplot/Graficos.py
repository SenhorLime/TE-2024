import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("dados.xlsx")

notasDf = pd.DataFrame(
    {
        "Aluno": df["Nome do Aluno"],
        "LP2": df["DELCOMCON.050"],
        "LLP2": df["DELCOMCON.051"],
    },
)


notasDf.plot.bar(x="Aluno")

plt.xlabel("Alunos")
plt.ylabel("Notas")
plt.show()
