# Validação: Implementação Python vs. MATLAB

## Resumo

Este projeto compara a implementação em Python de descritores fractais com a implementação de referência em MATLAB, estabelecida como padrão a ser alcançado. A análise abrange **363 descritores fractais** extraídos de **20 amostras**, demonstrando alta concordância entre as implementações.

---

## Resultados Principais

### Métricas Globais de Concordância

| Métrica | Valor | Interpretação |
|---------|-------|---------------|
| **Erro Absoluto Médio** | 0.002432 | Diferença média de ~0.002 entre implementações |
| **Erro Relativo Médio** | 0.0823% | **Excelente**: < 0.1% de desvio relativo |
| **RMSE Médio** | 0.002969 | Raiz do erro quadrático muito baixa |
| **Correlação Média** | 0.999719 | Bom demais: r > 0.999 |
| **Concordância Estatística** | 332/363 (91.46%) | Maioria sem diferença significativa (p > 0.05) |

### TL; DR
**A implementação Python é estatisticamente equivalente ao MATLAB**, com desvios desprezíveis que podem ser atribuídos a diferenças de precisão numérica entre as plataformas.

---

## Análise Visual

### 1. Distribuição de Erros por Descritor

#### **Visão Geral Completa**

![Erro Relativo - Visão Geral](plots\Erro_Relativo_por_Coluna_Visão_Geral.png)

- **Destaque**: Os descritores próximos do final apresentam erro de ~12%
- **Contexto**: É um outlier isolado; os demais 360 descritores têm erro próximo de zero

#### **Primeiros 360 Descritores**

![Erro Relativo - 360 descritores](plots\Erro_Relativo_por_Coluna_Primeiros_360_descritores.png)

- **Comportamento**: Erros extremamente baixos e uniformes (< 0.003%)
- **Padrão**: Ruído numérico típico de operações em ponto flutuante
- **Outliers**: Poucos picos isolados, provavelmente devido a descritores com valores próximos de zero (talvez?)

#### **Últimos 3 Descritores**

![Erro Relativo - Últimos 3](plots\Erro_Relativo_por_Coluna_Ultimos_3_descritores.png)

- **Observação crítica**: Erro relativo mais elevado (5-12%)
- **Causa provável**: 
  - Há, nas duas versões, tanto MATLAB quanto Python, uma função dedicada ao cálculo da Dimensão Fractal - descritor analisado aqui -, contudo ela não é utilizada. O cálculo é feito por meio de algoritmo de regressão linear em ambos.
  - A diferente implementação desses algoritmos em cada ambiente deve ser o responsável pela diferença.
- **Impacto**: Mínimo, pois representa apenas 0.8% dos descritores

### 2. Dispersão Global MATLAB vs. Python

![Dispersão Global](plots\Dispersao_global.png)

- **Interpretação**: Pontos alinhados perfeitamente sobre a diagonal (y = x)
- **Significado**: Relação linear perfeita entre as implementações
- **Desvios**: Imperceptíveis visualmente, confirmando a equivalência numérica

---

## Análise Detalhada

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
## Otimizações de Performance

Durante a validação inicial, a implementação em Python apresentou tempos de execução muito superiores ao MATLAB, especialmente nas funções da família **`pmr`**, que são naturalmente intensivas em operações numéricas.  

Foram investigadas diferentes abordagens de otimização, incluindo **vetorização com NumPy**, **paralelismo**, e finalmente o uso do **Numba**, que se mostrou a alternativa mais eficiente e estável.

### Funções `pmr`

Essas funções estavam entre os maiores gargalos de desempenho. Para imagens de **224×224 pixels** e `maxr = 41`, cada execução levava cerca de **10 minutos**.  

Tentativas de **vetorização com NumPy** resultaram em estouros de memória — algumas tentativas resultaram em operações que exigiam alocação de quase **2 GB** em arrays temporários, tornando a abordagem inviável.  

A solução definitiva foi o uso do **decorador `@njit` do Numba**, que converte o código Python puro em código nativo otimizado (similar a C). Essa simples modificação reduziu o tempo de execução de **minutos para segundos**, mantendo exatamente o mesmo resultado numérico.

### Funções `clustperc`

Nessa parte do código, houve necessidade de substituir a função de rotulagem de componentes conectados da biblioteca `scikit-image` (`label`) por uma implementação customizada, chamada **`_label_4conn`**.  

Essa nova versão foi escrita em Python puro, mas com o **Numba** aplicado para compilação JIT (Just-In-Time). Além de eliminar dependências externas, ela trouxe grande ganho de velocidade ao evitar overheads de interface entre Python e C durante laços internos.

### Comparativo de Tempos (20 imagens)

| Ambiente | Tempo Total | Observações |
|-----------|--------------|-------------|
| **MATLAB** | 35,17 min | Implementação de referência |
| **Python (com Numba)** | 5,8 min | Redução drástica de tempo com mesmo resultado |
| **Python (sem Numba)** | ≈ 5 horas (6 imagens) | Execução inviável para datasets maiores |

> **Resumo:** As otimizações com Numba tornaram a implementação Python não apenas equivalente numericamente ao MATLAB, mas também **significativamente mais rápida**, viabilizando análises em larga escala.

---

## Requisitos
```bash
pip install pandas numpy numba matplotlib
```

---



## Conclusões

- Equivalência numérica muito boa (erro médio < 0.1%)
- Alta reprodutibilidade estatística
- 🤓🤩