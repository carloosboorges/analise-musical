import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o dataset
df = pd.read_csv("tracks.csv")

# Verificar as primeiras linhas
print(df.head())

# ---------- NOVO GRÁFICO 1 ----------
# Gráfico de barras: quantidade de músicas explícitas vs não explícitas
plt.figure(figsize=(7, 5))
explicit_counts = df["explicit"].value_counts()
explicit_labels = ["Não explícita", "Explícita"]
plt.bar(explicit_labels, explicit_counts, color=["lightgreen", "salmon"], edgecolor="black")
plt.title("Quantidade de Músicas Explícitas vs Não Explícitas")
plt.ylabel("Quantidade de Músicas")
plt.tight_layout()
plt.grid(axis="y")
plt.show()

# ---------- NOVO GRÁFICO 2 ----------
# Gráfico de dispersão: duração vs danceabilidade
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="duration_ms", y="danceability", hue="explicit", alpha=0.6)
plt.title("Relação entre Duração e Danceabilidade das Músicas")
plt.xlabel("Duração (ms)")
plt.ylabel("Danceabilidade")
plt.legend(title="Explícita")
plt.tight_layout()
plt.grid(True)
plt.show()

# ---------- NOVO GRÁFICO 3 ----------
# Boxplot: distribuição da energia das músicas por década
df["year"] = pd.to_numeric(df["year"], errors="coerce")
df["decade"] = (df["year"] // 10) * 10
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="decade", y="energy", palette="coolwarm")
plt.title("Distribuição da Energia das Músicas por Década")
plt.xlabel("Década")
plt.ylabel("Energia")
plt.tight_layout()
plt.grid(True)
plt.show()
