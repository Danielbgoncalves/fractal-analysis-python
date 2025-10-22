import pandas as pd
import os

from ScriptLACDF3Distances import scriptLACDF3Distances 
from ScriptPercLACDF3Distances import scriptPercLACDF3Distances
def saveCSVPercCLACDF3Distances(origem, destino, All_FEATURES=True):
    '''
        Salva os resultados em um csv, por padrão apenas o DF e o LAC, mas podendo salvar também a percolação
    '''
    resultado = []
    if All_FEATURES: 
        print('Calculando perc, LAC e DF')
        resultado_perc = scriptPercLACDF3Distances(origem)
        resultado_LACDF = scriptLACDF3Distances(origem) 
        
        resultado = resultado_perc + resultado_LACDF  
    else:
        print('calculando LAC e DF')
        resultado = scriptLACDF3Distances(origem) 

    df = pd.DataFrame(resultado)
    os.makedirs(destino, exist_ok=True)  
    caminho_csv_final = os.path.join(destino, 'resultados_completos.csv')
    df.to_csv(caminho_csv_final, index=False, sep=';')

    print(f"Salvo em {caminho_csv_final}")

if __name__ == "__main__":
    import sys

    origem = sys.argv[1]
    destino = sys.argv[2]
    
    All_FEATURES = sys.argv[3].lower() == "true" 

    saveCSVPercCLACDF3Distances(origem, destino, All_FEATURES)


