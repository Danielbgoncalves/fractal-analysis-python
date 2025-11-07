# Otimizações de Performance

tentando aplicar vetorização com numpy, paralelismo e Numba

## Funções pmr
São funções muito demoradas, para imagens 224x224 com maxr=41levam cerca de 10 minutos cada
Usar vetorização não parece ser a solução, muito complexo (pra mim pelo menos é) e esta dando muitos estouros de memória. Há tentativas de alocação de quse 2G que dão erro quando maxr cresce.
A solução parece ser usar Numba.


---

22 de Novembro de 2025