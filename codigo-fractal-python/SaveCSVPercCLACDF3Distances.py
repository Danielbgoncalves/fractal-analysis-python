import pandas as pd
import os
import numpy as np
import time 

from util import reorganizar_e_expandir_df, reorganizar_e_expandir_csv2, gerar_df_exemplo


from ScriptLACDF3Distances import scriptLACDF3Distances 
from ScriptPercLACDF3Distances import scriptPercLACDF3Distances


def saveCSVPercCLACDF3Distances(origem, destino, All_FEATURES=True):
    '''
        Salva os resultados em um csv, por padrão apenas o DF e o LAC, mas podendo salvar também a percolação
    '''
    tic = time.time()

    if All_FEATURES: 
        print('==== Calculando PERC, LAC e DF ====')
        resultado_perc = scriptPercLACDF3Distances(origem)
        resultado_LACDF = scriptLACDF3Distances(origem)
        
        resultado = []
        for d_perc, d_lacdf in zip(resultado_perc, resultado_LACDF):
            combinado = {**d_perc, **d_lacdf}
            resultado.append(combinado)
    else:
        print('==== Calculando LAC e DF ====')
        resultado = scriptLACDF3Distances(origem) 

    print(resultado)

    df = pd.DataFrame(resultado)
    for col in df.columns:
        df[col] = df[col].apply(lambda x: x.tolist() if isinstance(x, np.ndarray) else x)

    # df = gerar_df_exemplo()

    df = reorganizar_e_expandir_df(df)
    # print(df)

    caminho_csv_final = os.path.join(destino, 'resultado_ordenado_3.csv')
    df.to_csv(caminho_csv_final, index=False, sep=';', decimal=',')  

    # os.makedirs(destino, exist_ok=True)  
    # caminho_csv_final = os.path.join(destino, 'resultados_completos2.csv')
    # df.to_csv(caminho_csv_final, index=False, sep=',')
    toc = time.time()
    tempo_gasto = toc - tic
    print(f"Salvo em {caminho_csv_final}")
    print(f"Tempo de execução total {tempo_gasto:.2f} segundos")

if __name__ == "__main__":
    import sys

    origem = sys.argv[1]
    destino = sys.argv[2]
    
    All_FEATURES = sys.argv[3].lower() == "true" 

    saveCSVPercCLACDF3Distances(origem, destino, All_FEATURES)