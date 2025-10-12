import pandas as pd
import os

from ScriptLACDF3Distances import ScriptLACDF3Distances 
from ScriptPercLACDF3Distances import ScriptPercLACDF3Distances

def SaveCSVPercCLACDF3Distances(origem, destino, LAC_DF_ONLY=True):
    '''
        Salva os resultados em um csv, por padrão apenas o DF e o LAC, mas podendo salvar também a percolação
    '''

    if LAC_DF_ONLY: 
        resultado = ScriptLACDF3Distances(origem)
    else:
        resultado = ScriptPercLACDF3Distances(origem)

    df = pd.DataFrame(resultado)
    caminho_csv_final = os.path.join(destino, 'resultados_completos.csv')
    df.to_csv(caminho_csv_final, index=False)

    print(f"Slavo em {caminho_csv_final}")


