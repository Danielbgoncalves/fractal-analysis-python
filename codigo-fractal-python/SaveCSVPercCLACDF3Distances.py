import pandas as pd
import os

from ScriptLACDF3Distances import scriptLACDF3Distances 
from ScriptPercLACDF3Distances import scriptPercLACDF3Distances
def saveCSVPercCLACDF3Distances(origem, destino, All_FEATURES=True):
    '''
        Salva os resultados em um csv, por padrão apenas o DF e o LAC, mas podendo salvar também a percolação
    '''

    if All_FEATURES: 
        resultado = scriptPercLACDF3Distances(origem)
    else:
        resultado = scriptLACDF3Distances(origem) 

    df = pd.DataFrame(resultado)
    os.makedirs(destino, exist_ok=True)  # garante que a pasta exista
    caminho_csv_final = os.path.join(destino, 'resultados_completos.csv')
    df.to_csv(caminho_csv_final, index=False, sep=';')

    print(f"Salvo em {caminho_csv_final}")

if __name__ == "__main__":
    import sys

    origem = sys.argv[1]
    destino = sys.argv[2]
    
    All_FEATURES = sys.argv[3].lower() == "true" if len(sys.argv) > 3 else True

    saveCSVPercCLACDF3Distances(origem, destino)


