import numpy as np

def N(matriz):
    # Tradução direta
    # MaxR, MaxC = matriz.shape
    # NL = np.array((MaxR, MaxC))

    # for i in range(MaxR):
    #     for j in range(MaxC):
    #         NL[i][j] = matriz[i][j]/ (i+1)

    # NLf = np.sum(NL, axis=0)

    # Tradução numpy
    maxR, _ = matriz.shape

    divisores = np.array(range(1,maxR)).reshape(-1,1) # [1,2,3..] vira coluna 
    NL = matriz / divisores
    NLf = np.sum(NL, axis=0)
    
    return NLf