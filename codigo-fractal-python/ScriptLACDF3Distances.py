import glob
import os
import time
from PIL import Image
import numpy as np

def scriptLACDF3Distances(diretorio_org, destino):
    '''
    Extração de atributos DF LAC
    com uso das métricas de distância Chessboard, Euclidiana e Manhatan a partir de imagens RGB.
    ######################
    Daniel Borges gonçalves
    Outubro de 2015
    '''

    # valor máximo de L
    maxr = 41

    # Classe 1
    diretorio_org='C:/Users/thais/Documents/Doutorado/Bases de imagens/LiverGender/1'; #imagens
    destino='C:/Users/thais/Documents/Doutorado/Bases de imagens/LiverGender/1'; #local onde será salvo o arquivo .mat

    padrao_de_busca = os.path.join(diretorio_org, '*.png')
    imagens =  glob.glob(padrao_de_busca) # caminhos pras imagens
    tipo = diretorio_org.split('/')

    print('Coletando características Fractais das Imagens - ', tipo[-1] )

    tic = time.time()

    for n in imagens:
        originais = os.path.basename(n)
        fullname = n
        img_pil = Image.open(fullname)
        PIC = np.array(img_pil)

        # falta continuar linha 27 adiante

    toc = time.time()


