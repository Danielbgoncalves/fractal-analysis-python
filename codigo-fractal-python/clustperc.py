import numpy as np
from joblib import Parallel, delayed
from scipy.ndimages import label
from scipy.stats import skew


def analisar_um_raio(p, g, h, k, r_k, img_aux):
    '''
    Essa função a análise de cluster/percolação para um único raio ed caixa r_k
    '''
    
    ncaixas = (img_aux.shape[0] - r_k + 1) * (img_aux.shape[1] - r_k + 1)
    if ncaixas <= 0: return (0, 0, 0)

    vetBigClusteres = np.zeros(ncaixas) # armazena a ocupação do maior custer na caixa de tamanho k
    ptemp, gtemp = 0, 0
    lim = (r_k / 2) - 0.5

    #percorrer os pixels centrais
    caixa_idx = 0
    for x in range(int(lim), int(img_aux[0] - lim)):
        for y in range(int(lim), int(img_aux[1] - lim)):
            xi = int( x - lim )
            xf = int( x + lim )
            yi = int( y - lim )
            yf = int( y + lim )
            percCount = 0

            box = np.zeros((xf - xi + 1, yf - yi + 1))
            a = -1
            for i in range(xi, xf + 1):
                a += 1
                b = -1
                for j in range(yi, yf + 1):
                    b += 1
                    if(
                        abs(img_aux[i, j, 0] - img_aux[x, y, 0]) <= r_k and
                        abs(img_aux[i, j, 1] - img_aux[x, y, 1]) <= r_k and
                        abs(img_aux[i, j, 2] - img_aux[x, y, 2]) <= r_k
                    ):
                        box[a,b] = 1
                        percCount += 1
                    else:
                        box[a, b] = 0
        structure = np.assray = ([[0, 1, 0],
                                  [1, 1, 1],
                                  [0, 1, 0]])
        L, ROTULO = label(box, structure=structure)
        if L > 0:
            labels = L[L>0]
            unique_labels, counts = np.unique(labels, return_counts=True)
            tamanho_maior_cluster = np.max(counts)
        else:
            tamanho_maior_cluster = 0
        vetBigClusteres[caixa_idx] = tamanho_maior_cluster/(r_k ** 2)
        ptemp += ROTULO
        if (percCount / r_k ** 2) >= 0.59275:
            gtemp += 1
        caixa_idx += 1
    p[k] = ptemp / ncaixas
    g[k] = gtemp / ncaixas
    h[k] = np.mean (vetBigClusteres)

                



def clustperc(img, maxr):
    aux = img.astype(np.float64)
    r = list(range(3, maxr + 1, 2)) # [3,5,7,...maxr]
    g = np.zeros((1, len(r)))   # valores de percolação para cada tamanho de r
    p = np.zeros((1, len(r)))   # valores de de n aglomerados para cada tamanho de r
    h = np.zeros((1, len(r)))   # valores do maior aglomerado para cada tamanho de r

    # para cada tamanho caixa *executar em paralelo*
    p, g, h = Parallel(n_jobs=-1)(
        delayed(analisar_um_raio)(p, g, h, k, r[k], aux) for k in range(len(r))
    )

    AreaCluster = np.trapz(p) # área sobre a curva, uma integral
    AreaPerc = np.trapz(g)
    AreaMaxCluster = np.trapz(h)
    SkewnessCluster = skew(p) # o quão assimétrica é a curva
    SkewnessPerc = skew(g)
    SkewnessMaxCluster = skew(h)
    [MaxCluster,MaxClusterIndex] = np.max(p), np.argmax(p) # o maior valor e seu index (da curva)
    [MaxPerc,MaxPercIndex] = np.max(g), np.argmax(g)
    [MaxMaxCluster,MaxMaxClusterIndex] = np.max(h), np.argmax(h)
    half = int(np.ceil(len(p)/2))
    AreaRatioCluster = np.trapz(p[half:])/np.trapz(p[:half])
    AreaRatioPerc = np.trapz(g[half:])/np.trapz(g[:half])
    AreaRatioMaxCluster = np.trapz(h[half:])/np.trapz(h[:half])


    return MaxClusterIndex, MaxPercIndex, MaxMaxClusterIndex, AreaRatioMaxCluster, MaxMaxCluster, SkewnessMaxCluster, AreaMaxCluster, AreaRatioCluster, AreaRatioPerc, MaxCluster, MaxPerc, SkewnessCluster, SkewnessPerc, AreaPerc, AreaCluster, p,g,h

