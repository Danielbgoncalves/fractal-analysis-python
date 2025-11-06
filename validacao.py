import pandas as pd
import numpy as np
from scipy.stats import pearsonr, ttest_rel
import matplotlib.pyplot as plt


# Ler arquivos
df_python = pd.read_csv('codigo-fractal-python/resultados/resultado_ordenado_v.csv', sep=',')
df_python[[c for c in df_python.columns if c.endswith('Index')]] += 1 # Pra ficar igual ao do matlab (indexado pelo 1)

df_matlab = pd.read_csv('codigos-fractal-matlab\saida3\Onlydata-resultado.csv', sep=',', header=None)
df_matlab = df_matlab.iloc[:, :-1]

# Eles *precisam* ter mesmo formanto
assert df_matlab.shape == df_python.shape, "Os CSVs têm tamanhos diferentes!"
print(f"Formato dos dados: {df_matlab.shape}")

M = df_matlab.to_numpy(dtype=np.float64)
P = df_python.to_numpy(dtype=np.float64)
n_rows, n_cols = M.shape

erros_abs = np.mean(np.abs(M - P), axis=0)
# média das magnitudes das duas implementações (evita divisão por zero)
mag_media = np.mean(np.abs(M) + np.abs(P), axis=0) / 2
erros_rel = np.where(mag_media > 1e-8, erros_abs / mag_media, np.nan)
rmse = np.sqrt(np.mean((M - P)**2, axis=0))

corrs = []
for j in range(n_cols):
    m_col, p_col = M[:, j], P[:, j]
    if np.allclose(m_col, p_col):  # são idênticas
        corrs.append(1.0)
    elif np.std(m_col) == 0 or np.std(p_col) == 0:  # uma das colunas é constante
        corrs.append(0.0)
    else:
        corrs.append(pearsonr(m_col, p_col)[0])
corrs = np.array(corrs)

p_values = np.array([ttest_rel(M[:, j], P[:, j]).pvalue for j in range(n_cols)])
sem_diferenca = np.sum(p_values > 0.05)

print("\n===== RESULTADOS GLOBAIS (corrigidos) =====")
print(f"Erro Absoluto Médio Global: {np.nanmean(erros_abs):.6f}")
print(f"Erro Relativo Médio Global: {np.nanmean(erros_rel)*100:.4f}%")
print(f"RMSE Médio Global: {np.nanmean(rmse):.6f}")
print(f"Correlação Média Global: {np.nanmean(corrs):.6f}")
print(f"Colunas sem diferença estatística (p > 0.05): {sem_diferenca}/{n_cols}")

# --- Visualizações ---
plt.figure(figsize=(10, 4))
plt.plot(np.nan_to_num(erros_rel)*100, label='Erro Relativo (%)')
plt.xlabel('Descritor (coluna)')
plt.ylabel('Erro Relativo (%)')
plt.title('Erro Relativo por Coluna - Visão Geral')
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(np.nan_to_num(erros_rel[:360])*100, label='Erro Relativo')
plt.xlabel('Descritor (coluna)')
plt.ylabel('Erro Relativo (%)')
plt.title('Erro Relativo por Coluna - Primeiros 360 descritores (%)')
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(6, 4))
plt.plot(np.nan_to_num(erros_rel[360:])*100, label='Erro Relativo')
plt.xlabel('Descritor (coluna)')
plt.ylabel('Erro Relativo (%)')
plt.title('Erro Relativo por Coluna - Últimos 3 descritores (%)')
plt.grid(True)
plt.legend()
plt.show()

plt.figure(figsize=(5, 5))
plt.scatter(M.flatten(), P.flatten(), s=10, alpha=0.6)
plt.xlabel('MATLAB')
plt.ylabel('Python')
plt.title('Dispersão global: MATLAB x Python')
plt.plot([M.min(), M.max()], [M.min(), M.max()], 'r--')
plt.grid(True)
plt.show()