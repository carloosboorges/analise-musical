import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("tracks.csv")

# Mostra as 5 primeiras linhas
print(df.head())


# Gráfico 1 - histograma da popularidade
print(df.columns)
plt.figure(figsize=(10, 6))
plt.hist(df["popularity"], bins=20, color="skyblue", edgecolor="black")
plt.title("Distribuição da Popularidade das Músicas")
plt.xlabel("Popularidade")
plt.ylabel("Quantidade de Músicas")
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico 2 - gráfico de linha da popularidade média por anos
df["year"] = pd.to_numeric(df["year"], errors="coerce")
df_grouped = df.groupby("year")["popularity"].mean().reset_index()

plt.figure(figsize=(10, 6))
plt.plot(df_grouped["year"], df_grouped["popularity"], marker="o", linestyle="-", color="green")
plt.title("Popularidade Média das Músicas ao Longo dos Anos")
plt.xlabel("Ano")
plt.ylabel("Popularidade Média")
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico 3 – Estilo onda suave com média móvel de 'energy'
valores = df["energy"].head(200)
media_movel = valores.rolling(window=10).mean()

plt.figure(figsize=(12, 4))
plt.plot(media_movel, color="dodgerblue", linewidth=2)
plt.title("Variação Suave da Energia das Músicas (Estilo Onda)")
plt.xlabel("Índice da Música")
plt.ylabel("Energy (com média móvel)")
plt.grid(True)
plt.tight_layout()
plt.show()



