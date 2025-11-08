# Análise de Texturas Fractais e Estatísticas

## O que é o projeto e por que ele existe
- Análise de texturas com base em conceitos fractais e estatísticos.  
- Parte de uma **Iniciação Científica**, com foco em **comparar e validar algoritmos científicos entre MATLAB e Python**.  
- Gera **descritores matemáticos** que ajudam a representar texturas de imagens — úteis em **classificação, segmentação e diagnóstico**.

## O problema que ele resolve
- O MATLAB é ótimo, mas **caro e limitado**.  
- O Python é gratuito, mas **inicialmente muito mais lento**.  
- O projeto busca **reproduzir fielmente os resultados** do MATLAB em Python e **otimizá-los** até superar o desempenho original.

## O que foi feito
- Implementação e tradução fiel dos algoritmos originais (FD, Lac, Percolação).  
- Validação numérica completa (**erro < 0.1% em 99% do casos**).  
- Otimização com Numba que permitiu resultados em minutos.  
- Geração automática de **363 descritores fractais por imagem**.

## O resultado final
- Uma **biblioteca aberta** para análise fractal de texturas em Python.  
- Equivalente ao MATLAB em precisão e muito mais rápida.  
- Validada estatisticamente.