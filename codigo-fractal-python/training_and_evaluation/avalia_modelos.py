from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import StratifiedKFold
import pandas as pd
import numpy as np

'''
    Treina 3 modelos de predição diferentes 
    - Random Forest
    - Suport Vector Machine
    - Rede Neural Artificial 
    na predição de carcinoma ou não nas mesmas imagens, roda com 2 CSVs:
        - LBP
        - Fractais
    A ideia é comparar os resultados.
'''

def avaliar_modelos(x, y, descritor, destino):

    skf = StratifiedKFold(n_splits = 5, shuffle=True, random_state=42)

    modelos = {
        "RF": RandomForestClassifier(random_state=42),
        "SVM": SVC(random_state=42),
        "RNA": MLPClassifier( hidden_layer_sizes=(512, 256),
                                max_iter=1000,
                                solver='adam',
                                activation='relu',
                                learning_rate_init=0.0005,
                                early_stopping=True,
                                validation_fraction=0.1,
                                n_iter_no_change=20,
                                random_state=42),
    }

        # RF - Random Forest
        # SVM - Support Vector Machine
        # RNA - Redes Neurais

    resultados = []

    for nome, modelo in modelos.items():
        acc_scores = []
        f1_scores = []

        for train, test in skf.split(x,y):         
            modelo.fit(x.iloc[train], y.iloc[train])
            pred = modelo.predict(x.iloc[test])
            acc_scores.append(accuracy_score(y[test], pred))
            f1_scores.append(f1_score(y[test], pred, average='macro'))

        resultados.append({
            "Descritor": descritor,
            "Modelo": nome,
            "Mean Accuracy": np.mean(acc_scores),
            "Mean f1-score": np.mean(f1_scores),
            "ACC Fold 1": acc_scores[0],
            "ACC Fold 2": acc_scores[1],
            "ACC Fold 3": acc_scores[2],
            "ACC Fold 4": acc_scores[3],
            "ACC Fold 5": acc_scores[4],
            "F1 Fold 1": f1_scores[0],
            "F1 Fold 2": f1_scores[1],
            "F1 Fold 3": f1_scores[2],
            "F1 Fold 4": f1_scores[3],
            "F1 Fold 5": f1_scores[4]
        })

        df = pd.DataFrame(resultados)
        path = f'{destino}/results_{descritor}.csv'
        df.to_csv(path, index=False)


if __name__ == '__main__':
    import pandas as pd
    import sys
    import os
    import glob
    import cv2

    destino = sys.argv[1]

    # LBP
    lbp = pd.read_csv('LBP_results/descritores_lbp.csv')
    lbp_y = lbp['rotulo']
    lbp_x = lbp.drop(columns=['rotulo'])

    # FRACTAIS
    fractal = pd.read_csv('../extract_features/resultados/result_228imgs_v_rotulado.csv')
    fractal_y = fractal['rotulo']
    fractal_x = fractal.drop(columns=['rotulo'])

    # FLATTEN sobre imagens originais
    # Caminhos
    padrao_saudavel = os.path.join('../feature_to_image/saida/healthy/F-RecPlot', '*.png')
    padrao_severo = os.path.join('../feature_to_image/saida/severe/F-RecPlot', '*.png')

    imagens = glob.glob(padrao_saudavel) + glob.glob(padrao_severo)

    imgs_y = [0 if i < len(glob.glob(padrao_saudavel)) else 1 for i in range(len(imagens))]

    flattened_imgs = []
    for img_path in imagens:
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if img is not None:
            flattened_imgs.append(img.flatten())
        else:
            print("Imagem não carregada:", img_path)

    # Transformar em DataFrame
    imgs_x = pd.DataFrame(flattened_imgs)
    imgs_y = pd.Series(imgs_y)

    print("Avaliando ")
    avaliar_modelos(lbp_x, lbp_y, 'LBP', destino)
    avaliar_modelos(fractal_x, fractal_y, 'fractal', destino)
    avaliar_modelos(imgs_x, imgs_y, 'imgs_f-recplot4', destino)


# def load_dataset(path):
#     X_fd = []
#     X_lbp = []
#     X_rp = []
#     X_seq = []
#     y = []

#     for label, clss in enumerate(sorted(os.listdir(path))):
#         class_path = os.path.join(path, clss)

#         for arq in os.listdir(class_path):
#             img_path = os.path.join(class_path, arq)
#             img = cv2.imread(img_path)

#             if img is None:
#                 continue

#             gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#             seq = image_to_sequence(gray)

#             # FD
#             fd = higuchi_fd(seq)

#             # LBP
#             lbp_hist = extract_lbp(img)

#             # RP
#             rp_img = recurrence_image(seq)
#             rp_flat = rp_img.flatten()

#             X_fd.append([fd])
#             X_lbp.append(lbp_hist)
#             X_rp.append(rp_flat)
#             y.append(label)

#     return np.array(X_fd), np.array(X_lbp), np.array(X_rp), np.array(y)