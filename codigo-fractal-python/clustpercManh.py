import numpy as np
from joblib import Parallel, delayed
from scipy.ndimage import label
from scipy.stats import skew


def analisar_um_raio(k, r_k, img_aux):
    '''
    Essa função a análise de cluster/percolação para um único raio ed caixa r_k
    '''
    
    ncaixas = (img_aux.shape[0] - r_k + 1) * (img_aux.shape[1] - r_k + 1)
    if ncaixas <= 0: 
        return k, 0.0, 0.0, 0.0

    vetBigClusteres = np.zeros(ncaixas, dtype=np.float64) # armazena a ocupação do maior custer na caixa de tamanho k
    ptemp, gtemp = 0, 0
    lim = (r_k / 2) - 0.5

    #percorrer os pixels centrais
    caixa_idx = 0
    for x in range(int(lim), int(img_aux.shape[0] - lim) ):
        for y in range(int(lim), int(img_aux.shape[1] - lim) ):
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
                    dist = (
                        abs(img_aux[i, j, 0] - img_aux[x, y, 0]) + \
                        abs(img_aux[i, j, 1] - img_aux[x, y, 1]) + \
                        abs(img_aux[i, j, 2] - img_aux[x, y, 2])
                        )
                    if dist <= r_k:
                        box[a,b] = 1
                        percCount += 1
                    else:
                        box[a, b] = 0

            structure = np.array([[0, 1, 0],
                                  [1, 1, 1],
                                  [0, 1, 0]], dtype=np.int8)
            
            labeled, num_features = label(box, structure=structure)

            labels_pos = labeled[labeled > 0]
            if labels_pos.size > 0:
                _, counts = np.unique(labels_pos, return_counts=True)
                tamanho_maior_cluster = np.max(counts)
            else:
                tamanho_maior_cluster = 0

            vetBigClusteres[caixa_idx] = tamanho_maior_cluster/(r_k ** 2)
            ptemp += num_features
            if (percCount / r_k ** 2) >= 0.59275:
                gtemp += 1
            caixa_idx += 1

    p_k = ptemp / ncaixas
    g_k = gtemp / ncaixas
    h_k = np.mean (vetBigClusteres)

    return k, p_k, g_k, h_k


def clustpercManh(img, maxr):
    aux = img.astype(np.float64)
    r = list(range(3, maxr + 1, 2)) # [3,5,7,...maxr]

    g = np.zeros(len(r))   # valores de percolação para cada tamanho de r
    p = np.zeros(len(r))   # valores de de n aglomerados para cada tamanho de r
    h = np.zeros(len(r))   # valores do maior aglomerado para cada tamanho de r

    # para cada tamanho caixa *executar em paralelo*
    results = Parallel(n_jobs=-1)(
        delayed(analisar_um_raio)( k, r[k], aux) for k in range(len(r))
    )

    for (k, p_k, g_k, h_k) in results:
        p[int(k)] = p_k
        g[int(k)] = g_k
        h[int(k)] = h_k


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


    return {
        'ManhMaxClusterIndex': MaxClusterIndex,
        'ManhMaxPercIndex': MaxPercIndex,
        'ManhMaxMaxClusterIndex': MaxMaxClusterIndex,
        'ManhAreaRatioMaxCluster': AreaRatioMaxCluster,
        'ManhMaxMaxCluster': MaxMaxCluster,
        'ManhSkewnessMaxCluster': SkewnessMaxCluster,
        'ManhAreaMaxCluster': AreaMaxCluster,
        'ManhAreaRatioCluster': AreaRatioCluster,
        'ManhAreaRatioPerc': AreaRatioPerc,
        'ManhMaxCluster': MaxCluster,
        'ManhMaxPerc': MaxPerc,
        'ManhSkewnessCluster': SkewnessCluster,
        'ManhSkewnessPerc': SkewnessPerc,
        'ManhAreaPerc': AreaPerc,
        'ManhAreaCluster': AreaCluster,
        'Manhp': p,
        'Manhg': g,
        'Manhh': h
    }
