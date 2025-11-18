import arff
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import os

def generar_graficas():
    # Cargar dataset
    df = load_kdd_dataset("DataSet/datasets/NSL-KDD/KDDTrain+.arff")

    # Particionamiento
    train_set, val_set, test_set = train_val_test_split(df, stratify='protocol_type')

    # Carpeta static
    static_path = os.path.join(os.path.dirname(__file__), '..', 'static')
    if not os.path.exists(static_path):
        os.makedirs(static_path)

    # Crear y guardar gráficas
    graficas = []
    for nombre, data in zip(['df', 'train', 'val', 'test'], 
                            [df, train_set, val_set, test_set]):
        plt.figure()
        data['protocol_type'].hist()
        archivo = f"{nombre}_hist.png"
        plt.savefig(os.path.join(static_path, archivo))
        plt.close()
        graficas.append(archivo)

    return graficas

# Funciones auxiliares
def load_kdd_dataset(data_path):
    with open(data_path, 'r') as f:
        dataset = arff.load(f)
        attributes = [attr[0] for attr in dataset["attributes"]]
        return pd.DataFrame(dataset["data"], columns=attributes)

def train_val_test_split(df, rstate=42, shuffle=True, stratify=None):
    strat = df[stratify] if stratify else None
    train_set, test_set = train_test_split(df, test_size=0.4, random_state=rstate, shuffle=shuffle, stratify=strat)
    strat = test_set[stratify] if stratify else None
    val_set, test_set = train_test_split(test_set, test_size=0.5, random_state=rstate, shuffle=shuffle, stratify=strat)
    return train_set, val_set, test_set
