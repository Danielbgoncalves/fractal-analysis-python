import numpy as np

def pmr(img, maxr=41):
    '''
    Calcula a matriz de probabilidades de uma imagem
    img deve ser uma ndarray numpy convertido em uint8 para float64
    maxr é o limite superior do rio, deve ser impar.
    '''

    '''
    Tem como vetorizar em numpy pra deixar mais rápido
    '''

    aux = img.astype(np.float64)
    r = range(3, maxr + 1, 2) # [3, 5, 7, ... maxr]
    p = np.zeros((r[-1]**2, len(r)), dtype=np.float64)

    # para cada tamanho de caixa
    for k in range(len(r)):
        ncaixas = (img.shape[0] - r[k]+1) * (img.shape[1] - r[k]+1)
        lim = (r[k]/2) - 0.5

        # percorrer os pixels centrais
        for x in range(int(lim), img.shape[0] - int(lim)):
            for y in range(int(lim), img.shape[1] - int(lim)):
                m = 0
                xi = int( x - lim )
                xf = int( x + lim )
                yi = int( y - lim )
                yf = int( y + lim )

                # deslizar a caixa
                for i in range(xi, xf + 1):
                    for j in range(yi, yf + 1):
                        dist = abs(aux[i,j,0] - aux[x,y,0])
                        if dist <= r[k]:
                            dist = abs(aux[i,j,0] - aux[x,y,1])
                            if dist <= r[k]:
                                dist = abs(aux[i,j,0] - aux[x,y,2])
                                if dist <= r[k]:
                                    m += 1
                p[m,k] += 1
        p[:,k] = p[:,k]/ncaixas
    return p



