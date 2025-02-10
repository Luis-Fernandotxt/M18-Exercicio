import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_csv("gasolina.csv")

# Criar o gráfico
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='dia', y='venda', marker='o', linestyle='-')
plt.xlabel("Dia")
plt.ylabel("Preço da Gasolina (R$)")
plt.title("Variação do Preço da Gasolina por Dia")
plt.grid(True)

# Salvar o gráfico
plt.savefig("gasolina.png")

# Exibir o gráfico
plt.show()
