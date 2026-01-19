# Ensemble de Redes Neurais para Classificação de Displasia Oral 🦷 🧫

## O DESAFIO

<table>
<tr>
<td width="50%">

### O Problema

- **Área**: Análise de imagens de epitélio oral
- **Objetivo**: Diferenciar tecido **saudável** de **displasia oral grave**
- **Desafio**: Alcançar alta precisão na classificação binária
- **Dataset**: 228 imagens (114 healthy + 114 severe)

</td>
<td width="50%">

### Representações Testadas

- **Imagens Originais** 
- **Recurrence Plots (F-RecPlot)** gerados a partir de **descritores fractais**:
  - Dimensão Fractal (FD)
  - Lacunaridade
  - Medidas de Percolação

</td>
</tr>
</table>

---

## A SOLUÇÃO: Ensemble com 4 Cenários

```
┌─────────────────────────────────────────────┐
│   Combinação de 2 Redes Neurais !! com      │
│        Regra da Soma (Sum Rule)            │
└─────────────────────────────────────────────┘
```

### Arquiteturas Base

- **MobileNetV2**: Modelo leve, otimizado para dispositivos móveis
- **EfficientNet-B0**: Modelo eficiente com bom balanço entre performance e tamanho

### Cenários de Ensemble

| Cenário | Modelos | Entrada | Estratégia |
|---------|---------|---------|-----------|
| **1** | 2× MobileNetV2 | Original + RecPlot | Combinar ambas representações |
| **2** | MobileNetV2 + EfficientNet-B0 | Original + RecPlot | Diversidade de arquitetura |
| **3** | MobileNetV2 + EfficientNet-B0 | Apenas Original | Só imagens originais |
| **4** | MobileNetV2 + EfficientNet-B0 | Apenas RecPlot | Só características fractais |

---

## METODOLOGIA

### Treinamento: K-Fold Cross-Validation (K=5)

```
┌─────────────────────────────────────┐
│  Dados de Treino e Validação        │
│  (114 healthy + 114 severe)         │
└─────────────────────────────────────┘
           ↓
  ┌───────────────────────┐
  │   StratifiedKFold     │
  │   K = 5 folds         │
  │   Shuffle = True      │
  │   Random State = 42   │
  └───────────────────────┘
           ↓
  ├─ Fold 1: 4/5 treino, 1/5 validação
  ├─ Fold 2: 4/5 treino, 1/5 validação
  ├─ Fold 3: 4/5 treino, 1/5 validação
  ├─ Fold 4: 4/5 treino, 1/5 validação
  └─ Fold 5: 4/5 treino, 1/5 validação
```

### Hiperparâmetros

```python
IMG_SIZE = 224 × 224          # Tamanho padrão MobileNet/EfficientNet
BATCH_SIZE = 32               # Imagens por batch
EPOCHS = 20                   # Épocas de treinamento por fold
OPTIMIZER = Adam              # Learning rate: 0.0001
LOSS = CrossEntropyLoss       # Função de perda
```

### Fusão de Predições: Sum Rule

```
Cada modelo produz probabilidades [P(healthy), P(severe)]

Predição Final = argmax(P_mobilenet + P_efficientnet)
```

---

## RESULTADOS

### Comparação dos 4 Cenários

Teste realizado em **44 imagens** (22 healthy + 22 severe)

### RANKING DE DESEMPENHO

```
🥇 1º LUGAR (EMPATE): Cenário 1 e Cenário 4
   Acurácia: 97.73% | F1 Score: 0.9773
   
🥈 2º LUGAR: Cenário 2
   Acurácia: 95.45% | F1 Score: 0.9545
   
🥉 3º LUGAR: Cenário 3
   Acurácia: 86.36% | F1 Score: 0.8611
```

---

### DETALHAMENTO COMPLETO

#### Cenário 1: 2 MobileNets (Original + RecPlot)

```
Acurácia:      97.73%
F1 Score:      0.9773

Matriz de Confusão:
               Predito Healthy  Predito Severe
Realmente Healthy     21               1
Realmente Severe       0              22

Erros: 1 falso positivo
```

---

#### Cenário 2: MobileNet + EfficientNet (Original + RecPlot)

```
Acurácia:      95.45%
F1 Score:      0.9545

Matriz de Confusão:
               Predito Healthy  Predito Severe
Realmente Healthy     20               2
Realmente Severe       0              22

Erros: 2 falsos positivos
```

---

#### Cenário 3: MobileNet + EfficientNet (Apenas Original)

```
Acurácia:      86.36%
F1 Score:      0.8611

Matriz de Confusão:
               Predito Healthy  Predito Severe
Realmente Healthy     16               6
Realmente Severe       0              22

Erros: 6 falsos positivos
```

---

#### Cenário 4: MobileNet + EfficientNet (Apenas RecPlot)

```
Acurácia:      97.73%
F1 Score:      0.9773

Matriz de Confusão:
               Predito Healthy  Predito Severe
Realmente Healthy     21               1
Realmente Severe       0              22

Erros: 1 falso positivo
```

---

### ANÁLISE COMPARATIVA

| Métrica | Cenário 1 | Cenário 2 | Cenário 3 | Cenário 4 |
|---------|-----------|-----------|-----------|-----------|
| **Acurácia** | 🏆 97.73% | 95.45% | 86.36% | 🏆 97.73% |
| **F1 Score** | 🏆 0.9773 | 0.9545 | 0.8611 | 🏆 0.9773 |
| **Falsos Positivos** | 1 | 2 | 6 | 1 |
| **Falsos Negativos** | 0 | 0 | 0 | 0 |
| **Recall** | 100% | 100% | 100% | 100% |
| **Especificidade** | 95.45% | 90.91% | 72.73% | 95.45% |


---

## COMO USAR

### Prerequisitos

```bash
pip install torch torchvision
pip install pandas numpy scikit-learn matplotlib pillow
```

### Executar o Notebook

1. Preparar dataset na estrutura esperada:
```
dataset/
├── treino_e_validacao/
│   ├── healthy/
│   │   ├── originais/
│   │   └── F-RecPlot/
│   └── severe/
│       ├── originais/
│       └── F-RecPlot/
└── testes/
    ├── healthy/
    │   ├── originais/
    │   └── F-RecPlot/
    └── severe/
        ├── originais/
        └── F-RecPlot/
```

2. Executar `ensembles.ipynb` no Jupyter/Colab

---

## INFORMAÇÕES ADICIONAIS

**Imagens do Experimento**  
As imagens usadas no experimento são as **originais + as geradas usando a técnica do RecPlot**.

**Dataset**  
A pasta com a organização utilizada no notebook está disponível no GitHub, na área de releases.
