# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nw537B3GW4n7lG2Brsa7FTfv5suJ9X49
"""

import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("La lista debe contener nueve números")

    # Convertir la lista en una matriz 3x3
    matrix = np.array(list).reshape(3, 3)

    # Calcular las estadísticas
    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum()]
    }

    return calculations

# Ejemplo de uso
result = calculate([0,1,2,3,4,5,6,7,8])
print(result)