import glob
import time
import os
from PIL import Image
import numpy as np

from clustperc import clustperc
from clustpercEucl import clustpercEucl
from clustpercManh import clustpercManh

def scriptPercLACDF3Distances(diretorio_org):
    '''
    Extração de atributos DF LAC 
    com uso das métricas de distância Chessboard, Euclidiana e Manhatan a partir de imagens RGB.
    
    Daniel Borges gonçalves
    Outubro de 2025
    '''

    maxr = 41

    padrao_de_busca = os.path.join(diretorio_org, '*.png').replace("\\", "/")
    imagens =  glob.glob(padrao_de_busca) # caminhos pras imagens

    lista_de_resultados = []

    nome_da_classe = os.path.basename(diretorio_org)
    print('Coletando características Fractais das Imagens - ', nome_da_classe )


    for caminho in imagens:
      
        img_pil = Image.open(caminho)
        img_pil_resized = img_pil.resize((224, 224), Image.BILINEAR)
        PIC = np.array(img_pil_resized)

        Minsk_perc = clustperc(PIC, maxr)
        Eucl_perc = clustpercEucl(PIC, maxr)
        Manh_perc = clustpercManh(PIC, maxr)

        resultado_parc = {**Minsk_perc, **Eucl_perc, **Manh_perc}
        lista_de_resultados.append(resultado_parc)
        
    return lista_de_resultados

