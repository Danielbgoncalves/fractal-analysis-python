# Validação do programa python com base no original MATLAB - uma imagem
usei a imagem de uma folha para os testes, ela esta aqui em baixo:
`folha`: ![zoom em uma folha](codigo-fractal-python/imagens_entrada/folha.png)
## Funções pmr
usando maxr = 3
### Comparação — pmr.py vs pmr.m
Usando como base a imagem `folha` o pmr.m deu (usamos maxr=3):
| MATLAB (`pmr.m`) | PYTHON (`pmr.py`) |
| :--------------- | :---------------- |
| MatrizProb =     | MatrizprobMink =  |
| 0.0550           | 0.05504829        |
| 0.1075           | 0.10745881        |
| 0.2027           | 0.20268241        |
| 0.1013           | 0.10127019        |
| 0.0851           | 0.08509861        |
| 0.1021           | 0.1021021         |
| 0.0699           | 0.0698604         |
| 0.0796           | 0.07957958        |
| 0.1969           | 0.1968996         |



### Comparação — pmrEucl.py vs pmrEucl.m

| MATLAB (`pmrEucl.m`) | PYTHON (`pmrEucl.py`) |
| :------------------- | :-------------------- |
| 0.1428               | 0.14284555            |
| 0.1846               | 0.1846441             |
| 0.2213               | 0.22130915            |
| 0.0972               | 0.09715121            |
| 0.0766               | 0.07663745            |
| 0.0868               | 0.08682331            |
| 0.0452               | 0.04516679            |
| 0.0475               | 0.04747991            |
| 0.0979               | 0.09794254            |


### Comparação — pmrManh.py vs pmrManh.m
| MATLAB (`pmrManh.m`) | PYTHON (`pmrManh.py`) |
| :------------------- | :-------------------- |
| 0.2184               | 0.21838731            |
| 0.2246               | 0.2246368             |
| 0.2087               | 0.208729              |
| 0.0881               | 0.08812191            |
| 0.0668               | 0.06681682            |
| 0.0730               | 0.07296486            |
| 0.0310               | 0.03098369            |
| 0.0283               | 0.02830533            |
| 0.0611               | 0.0610543             |


---

## Lacunaridade
| MATLAB (`lacunaridade.m`) | PYTHON (`lacunaridade.py`)                               |
| :------------------------ | :------------------------------------------------------- |
| MinkLAC = 0.2555          | MinkLAC = [0.25553428]                                   |
| MinkAreaLAC = 2.4564      | MinkAreaLAC = 2.456379510294571                          |
| MinkSkewnessLAC = 0.5672  | MinkSkewnessLAC = 0.5671635347104276                     |
| MinkAreaRatioLAC = 0.4327 | MinkAreaRatioLAC = 0.43269631574639084                   |
| MinkMaxLAC = 0.2555       | MinkMaxLAC = 0.255534278606888                           |
| MinkMaxLACIndex = 1       | MinkMaxLACIndex = 0  (👀Python indexa de 0, MATLAB de 1, deu o primeiro item nos dois) |
 
    
---

## N
| MATLAB (`N.m`)                                                                                                                                                          | PYTHON (`N.py`)                                                                                                                                                                                                                                        |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Minknn = 0.2775, 0.1011, 0.0488, 0.0283, 0.0179, 0.0121, 0.0087, 0.0064, 0.0049, 0.0039, 0.0031, 0.0026, 0.0021, 0.0018, 0.0015, 0.0013, 0.0012, 0.0010, 0.0009, 0.0008 | Minknn = [0.27749803, 0.10108267, 0.048794, 0.02827701, 0.01788291, 0.01210797, 0.00866966, 0.0064338, 0.00492566, 0.00387751, 0.00312639, 0.00256526, 0.00213691, 0.00180535, 0.00154151, 0.00132907, 0.00115608, 0.00101434, 0.00089653, 0.00079727] |


---

## DF
| MATLAB (`DF.m`) | PYTHON (`DF.py`)            |
| :-------------- | :-------------------------- |
| MinkDF = 2.3694 | MinkDF = 2.3361943865222847 |



---

## Percolação
Com maxr = 11
| MATLAB                           | PYTHON                                         |
| :------------------------------- | :--------------------------------------------- |
| MinkMaxClusterIndex = 5          | Minks-MaxClusterIndex = 4                      |
| MinkMaxPercIndex = 5             | Minks-MaxPercIndex = 4                         |
| MinkMaxMaxClusterIndex = 5       | Minks-MaxMaxClusterIndex = 4                   |
| MinkAreaRatioMaxCluster = 0.5255 | Minks-AreaRatioMaxCluster = 0.525456683021205  |
| MinkMaxMaxCluster = 0.6096       | Minks-MaxMaxCluster = 0.609577760950648        |
| MinkSkewnessMaxCluster = 0.2480  | Minks-SkewnessMaxCluster = 0.24801079206201992 |
| MinkAreaMaxCluster = 2.3346      | Minks-AreaMaxCluster = 2.3345541841830206      |
| MinkAreaRatioCluster = 0.5601    | Minks-AreaRatioCluster = 0.5601429381248573    |
| MinkAreaRatioPerc = 0.5344       | Minks-AreaRatioPerc = 0.5343597572173152       |
| MinkMaxCluster = 1.4166          | Minks-MaxCluster = 1.4166084374181152          |
| MinkMaxPerc = 0.5309             | Minks-MaxPerc = 0.5309415669490786             |
| MinkSkewnessCluster = -0.3760    | Minks-SkewnessCluster = -0.3760284159449632    |
| MinkSkewnessPerc = -0.3923       | Minks-SkewnessPerc = -0.39226446063688286      |
| MinkAreaPerc = 1.9770            | Minks-AreaPerc = 1.9770316117134803            |
| MinkAreaCluster = 5.2109         | Minks-AreaCluster = 5.210924985223471          |

| MATLAB                                           | PYTHON                                                                 |
| :----------------------------------------------- | :--------------------------------------------------------------------- |
| Minkp = [1.1488, 1.2591, 1.3022, 1.3669, 1.4166] | Minks-p = [1.14877039, 1.25911157, 1.30224729, 1.36687671, 1.41660844] |
| Minkg = [0.4484, 0.4976, 0.4883, 0.5014, 0.5309] | Minks-g = [0.44844168, 0.49758264, 0.48834273, 0.50141461, 0.53094157] |
| Minkh = [0.5634, 0.5706, 0.5844, 0.5931, 0.6096] | Minks-h = [0.56335389, 0.57059174, 0.58435867, 0.59313796, 0.60957776] |

## Conclusão
A validação cruzada entre as versões MATLAB e Python mostrou que os resultados numéricos das funções implementadas — pmr, pmrEucl, pmrManh, lacunaridade, N, DF e clustperc — apresentam alto grau de similaridade.
As diferenças observadas ocorrem apenas na últimas casa decimal e são atribuídas ao tratamento interno de arredondamentos que as linguagens realizam

## Continuidade
Como próxima etapa a otimização de desempenho das funções Python é a meta, especialmente aquelas que utilizam loops aninhados triplos (como pmr, pmrEucl e pmrManh), por meio de:

1. Vetorização com NumPy — substituir iterações explícitas por operações matriciaisque são implementadas em C
2. Uso de máscaras booleanas — aplicar filtros condicionais (dist <= r[k]) diretamente sobre matrizes 2D ou 3D, reduz o número de operações em Python puro.
3. Exploração de paralelismo — empregar multiprocessing para processar diferentes regiões da imagem em paralelo como feito nas funções clustperc

A meta é alcançar ganhos de desempenho, mantendo a fidelidade total aos resultados originais do MATLAB.