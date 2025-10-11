# Análise de Texturas com Fractais, Lacunaridade e Percolação

## Visão Geral

Este projeto de Iniciação Científica (IC) realiza a extração de características fractais de texturas em imagens, utilizando três métricas principais: Dimensão Fractal, Lacunaridade e Percolação, aplicadas com três diferentes métricas de distância (Minkowski/Chebyshev, Euclidiana e Manhattan). As imagens de entrada são processadas e redimensionadas para 224x224 antes da análise.

O projeto tem como objetivo explorar técnicas matemáticas e computacionais para análise quantitativa de texturas e gerar um conjunto robusto de features que pode ser usado em pesquisas científicas ou modelos de aprendizado de máquina.

---

## Conceitos Fundamentais

### 🔷 Dimensão Fractal (FD)

Mede a **complexidade estrutural de uma imagem em múltiplas escalas**. Uma linha possui dimensão 1, uma superfície lisa tem dimensão 2. Texturas reais podem ter dimensão **fractal não inteira**, como 1.27 ou 1.85, indicando níveis intermediários de complexidade.

* O método utilizado é o **Box-Counting Adaptado por Semelhança de Cor**.
* Para cada tamanho de caixa `r` (3, 5, 7, ..., 41), calcula-se **N(r): a média de pixels semelhantes ao pixel central** dentro da caixa.
* A **Dimensão Fractal é obtida por regressão log-log** sobre N(r).

### 🔷 Lacunaridade

Avalia **o quão homogênea ou esburacada é uma textura**, complementando a FD.

* **Baixa lacunaridade** → textura uniforme e contínua.
* **Alta lacunaridade** → grandes vazios, buracos e heterogeneidade.
* Usa-se a matriz de probabilidade `p(m, k)`, onde **m é a contagem de pixels semelhantes** e **k indexa o tamanho da caixa**.
* Calcula-se:

  * **M1** = média de m para aquela escala
  * **M2** = segundo momento
  * [ **Lac(k) = (M2 - M1²)² / M1²** ]

### 🔷 Percolação e Clusterização de Texturas

Analisa **como regiões de pixels semelhantes se conectam espacialmente**.

* Para cada caixa e pixel central, é gerada uma **imagem binária** destacando apenas os pixels parecidos com limite de tolerância.
* Usa-se **bwlabel** para detectar clusters conectados.
* 3 curvas são extraídas:

  * **p(k)** → número médio de clusters distintos
  * **g(k)** → **probabilidade de percolação** (estrutura conectada atravessa a caixa ao superar limiar crítico ≈ 0.59275)
  * **h(k)** → tamanho relativo do **maior cluster** encontrado

---

## Organização dos Códigos MATLAB Originais

### 🎯 Scripts Principais

* `ScriptPercLACDF3Distances.m` → Extrai **todas as features** (percolação + lacunaridade + FD).
* `ScriptLACDF3Distances.m` → Versão reduzida **SEM percolação** (mais rápido).

### 📊 Cálculo de Matrizes de Probabilidade

* `pmr.m` (Minkowski)
* `pmrEucl.m` (Euclidiana)
* `pmrManh.m` (Manhattan)

### 🔍 Clusterização e Percolação

* `clustperc.m` (Minkowski)
* `clustpercEucl.m` (Euclidiana)
* `clustpercManh.m` (Manhattan)

### 📈 Extração Final dos Valores

* `Lacunaridade.m` → Recebe `p(m,k)` e retorna vetor Lac(k)
* `N.m` → Extrai média N(r) para FD
* `D.m` → Alternativa direta para FD

### 💾 Salvamento Automatizado

* `SaveCSVPercoCLACDF3Distances.m` → Agrupa features de **todas as imagens** em um CSV final estruturado para Machine Learning.

---

## Pipeline de Processamento (Visão Geral)

1. Carregar todas as imagens `.png` de um diretório
2. Redimensionar para 224×224
3. Para cada imagem e cada `r ∈ {3, 5, ..., 41}`:

   * Gerar matriz de probabilidade `p(m,k)` (3 versões: Mink, Eucl, Manh)
   * Extrair FD (regressão log-log de N(r))
   * Extrair Lacunaridade
   * Extrair Percolação (se habilitado)
4. Salvar cada métrica em tabela estruturada
5. Unificar todas as imagens no CSV final