import pandas as pd
import matplotlib.pyplot as plt
# from io import StringIO

# ---- Load the CSVs from user content ----

# 1. LBP
lbp = pd.read_csv("LBP_results/results_LBP.csv")

# 2. Fractal
fractal = pd.read_csv("LBP_results/results_fractal.csv")

# 3. Flatten
flat = pd.read_csv("LBP_results/results_imgs_originais.csv")

# 4. Fractal images
fimg = pd.read_csv("LBP_results/flaten_imgs.csv")

# 5. CNN fractal images
cnn = pd.read_csv("LBP_results/mobilenet_kfold.csv")

# ---- Combine all ----
df = pd.concat([lbp, fractal, flat, fimg, cnn], ignore_index=True)

# ---- Heatmap pivot (Mean Accuracy) ----
pivot = df.pivot_table(values="Mean Accuracy", index="Descritor", columns="Modelo")

plt.figure(figsize=(8,6))
plt.imshow(pivot, aspect='auto')
plt.xticks(range(len(pivot.columns)), pivot.columns, rotation=45)
plt.yticks(range(len(pivot.index)), pivot.index)
plt.colorbar()
plt.title("Heatmap – Mean Accuracy")

plt.show()

# ---- Bar plot: accuracy by model x descritor ----
plt.figure(figsize=(10,5))
for descritor in df["Descritor"].unique():
    subset = df[df["Descritor"] == descritor]
    plt.bar(subset["Modelo"] + " (" + descritor + ")", subset["Mean Accuracy"])

plt.xticks(rotation=90)
plt.title("Comparação de Accuracy entre modelos e descritores")
plt.ylabel("Accuracy")
plt.tight_layout()
plt.show()

# ---- Ranking plot ----
ranking = df.sort_values("Mean Accuracy", ascending=False)

plt.figure(figsize=(8,6))
plt.barh(ranking["Descritor"] + " - " + ranking["Modelo"], ranking["Mean Accuracy"])
plt.gca().invert_yaxis()
plt.xlabel("Accuracy")
plt.title("Ranking Geral dos Métodos")
plt.tight_layout()
plt.show()
