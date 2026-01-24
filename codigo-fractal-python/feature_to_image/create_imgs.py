import pandas as pd
import numpy as np
import time

from reshapeRecPlot import reshapeRecPlot
from reshapeClassical import reshapeClassical

def create_imgs(origem, destino):

    tic = time.time()

    df = pd.read_csv(origem, sep=',')
    features = df.to_numpy(dtype=np.float64)

    reshapeRecPlot(destino, features)
    #reshapeClassical(destino, features)

    toc = time.time()
    intervalo = toc - tic
    print(f'Imagens salvas em {destino}')
    print(f"Concluído em {intervalo:.3f} segundos")

if __name__ == "__main__":
    import sys

    origem = sys.argv[1]
    destino = sys.argv[2]

    create_imgs(origem, destino)