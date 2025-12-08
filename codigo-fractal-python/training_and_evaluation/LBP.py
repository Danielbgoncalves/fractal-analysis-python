'''
Extrair descritores das imagens saudáveis e com carcinoma severo por meio da tecnica LBP
para comparar com a extração de descritores da imagem

A ideia é comparar com o que extraimos com descritores fractais e comparar qual técnica é melhor 
para o aprendizado.
'''

import cv2
from skimage.feature import local_binary_pattern
import pandas as pd
import os
import glob
import numpy as np

def extrai_lbp_features(diretorio_org, destino):
    '''
    diretorio_org: origem das imagens
    destino: onde salvar o csv após extração
    '''

    padrao_saudavel = os.path.join(f'{diretorio_org}/healthy', '*.tif').replace("\\", "/")
    padrao_severo = os.path.join(f'{diretorio_org}/severe', '*.tif').replace("\\", "/")

    imagens = glob.glob(padrao_saudavel) + glob.glob(padrao_severo)

    dados = []

    for caminho in imagens:

        gray_image = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)

        radius = 1
        n_points = 8 * radius

        lbp_image = local_binary_pattern(gray_image, n_points, radius, method='uniform')

        hist, _ = np.histogram(lbp_image.ravel(), bins=np.arange(0, 59+1), range=(0, 59))

        #hist  = cv2.calcHist([lbp_image.astype("uint8")], [0], None, [256], [0, 256])

        # hist, _ = np.histogram(
        #             lbp_image.ravel(),
        #             bins=np.arange(0, n_points + 3),
        #             range=(0, n_points + 2)
        #         )

        # 0 saudavel 1 doente
        classe = os.path.basename(os.path.dirname(caminho))
        rotulo = 0 if classe == 'healthy' else 1
        
        registro = {f"hist_{i}": hist[i] for i in range(len(hist))}
        registro["rotulo"] = rotulo

        dados.append(registro)
    
    df = pd.DataFrame(dados)
    path = f'{destino}\descritores_lbp.csv'
    df.to_csv(path, index=False)

if __name__ == "__main__":
    import sys

    origem = sys.argv[1]
    destino = sys.argv[2]

    extrai_lbp_features(origem, destino)