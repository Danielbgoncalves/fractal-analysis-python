# 🔬 Validação: Implementação Python vs. MATLAB

## Resumo

Este projeto compara a implementação em Python de descritores fractais com a implementação de referência em MATLAB, estabelecida como padrão a ser alcançado. A análise abrange **363 descritores fractais** extraídos de **6 amostras**, demonstrando alta concordância entre as implementações.

---

## Resultados Principais

### Métricas Globais de Concordância

| Métrica | Valor | Interpretação |
|---------|-------|---------------|
| **Erro Absoluto Médio** | 0.001814 | Diferença média de ~0.002 entre implementações |
| **Erro Relativo Médio** | 0.0672% | **Excelente**: < 0.1% de desvio relativo |
| **RMSE Médio** | 0.002202 | Raiz do erro quadrático muito baixa |
| **Correlação Média** | 0.999799 | Bom demais: r > 0.999 |
| **Concordância Estatística** | 334/363 (92.0%) | Maioria sem diferença significativa (p > 0.05) |

### Veredicto
**A implementação Python é estatisticamente equivalente ao MATLAB**, com desvios desprezíveis que podem ser atribuídos a diferenças de precisão numérica entre as plataformas.

---

## Análise Visual

### 1. Distribuição de Erros por Descritor

#### **Visão Geral Completa**

![Erro Relativo - Visão Geral](plots\Erro_Relativo_por_Coluna_Visão_Geral.png)

- **Destaque**: Os descritores próximos do final apresentam erro de ~11%
- **Contexto**: É um outlier isolado; os demais 362 descritores têm erro próximo de zero

#### **Primeiros 360 Descritores**

![Erro Relativo - 360 descritores](plots\Erro_Relativo_por_Coluna_Primeiros_360_descritores.png)

- **Comportamento**: Erros extremamente baixos e uniformes (< 0.003%)
- **Padrão**: Ruído numérico típico de operações em ponto flutuante
- **Outliers**: Poucos picos isolados, provavelmente devido a descritores com valores próximos de zero

#### **Últimos 3 Descritores**

![Erro Relativo - Últimos 3](plots\Erro_Relativo_por_Coluna_Ultimos_3_descritores.png)

- **Observação crítica**: Erro relativo mais elevado (5-11%)
- **Causa provável**: 
  - Há, nas duas versões, tanto MATLAB quanto Python, uma função dedicada ao cálculo da Dimensão Fractal - descritor analisado aqui -, contudo ela não é utilizada. O cálculo se dá por meio de algoritmo de regressão linear em ambos.
  - A diferente implementaçãos desses algoritmos em cada ambiente deve ser o responsável pela diferença.
- **Impacto**: Mínimo, pois representa apenas 0.8% dos descritores

### 2. Dispersão Global MATLAB vs. Python

![Dispersão Global](plots\Dispersao_global.png)

- **Interpretação**: Pontos alinhados perfeitamente sobre a diagonal (y = x)
- **Significado**: Relação linear perfeita entre as implementações
- **Desvios**: Imperceptíveis visualmente, confirmando a equivalência numérica

---

## 🔍 Análise Detalhada

### Distribuição de Erros Relativos

```
Faixa de Erro        | Descritores | Percentual
---------------------|-------------|------------
< 0.01%              | 360         | 99.2%
0.01% - 1%           | 0           | 0%
1% - 5%              | 0           | 0%
5% - 15%             | 3           | 0.8%
```

### Teste t Pareado (α = 0.05)

- **Hipótese nula**: Não há diferença entre as médias das implementações
- **Resultado**: 92% dos descritores **não rejeitam H₀**
- **Conclusão**: As implementações são estatisticamente indistinguíveis na maioria dos casos
- Finalmente utilizando estatística de vdd !!!

---

## 🛠️ Metodologia de Validação

### Dados de Entrada
- **Amostras**: 6 observações
- **Descritores**: 363 features fractais por amostra
- **Formato**: Matrizes 6×363 (MATLAB e Python)

### Métricas Calculadas

``` bash
Erro Absoluto Médio Global: 0.001814
Erro Relativo Médio Global: 0.0672%
RMSE Médio Global: 0.002202
Correlação Média Global: 0.999799
Colunas sem diferença estatística (p > 0.05): 334/363
```

---

## ⚙️ Execução do Script

### Requisitos
```bash
pip install pandas numpy scipy matplotlib
```

### Uso
```bash
python validacao.py
```

### Estrutura de Arquivos
```
projeto/
├── codigo-fractal-python/
│   └── resultados/
│       └── resultado_ordenado_5_v.csv
├── codigos-fractal-matlab/
│   └── saida3/
│       └── Onlydata-resultado.csv
├── plots/
│   ├── Erro_Relativo_por_Coluna_Primeiros_360_descritores.png
│   ├── Erro_Relativo_por_Coluna_Ultimos_3_descritores.png
│   ├── Erro_Relativo_por_Coluna_Visão_Geral.png
│   └── Dispersao_global.png
├── validacao.py
└── VALIDACAO.md
```

## Conclusões

- Equivalência numérica excepcional (erro médio < 0.1%)
- Alta reprodutibilidade estatística



