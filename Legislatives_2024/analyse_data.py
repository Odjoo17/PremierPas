import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from utils import create_pickle,use_pickle,init_logger


def analyse(pickle_name):
    data = use_pickle(pickle_name)
    print("analyse:",data)
    # Sélectionner les colonnes pour le graphique : On prend les 5 premières lignes, qui sont les 5 partis avec le plus de voix obtenus lors du second tour
    x = data['Liste des nuances_premier_tour'].iloc[:7]
    y1 = data['Voix_premier_tour'].iloc[:7]
    y2 = data['Voix_second_tour'].iloc[:7]

    # Tracer le graphique avec Matplotlib
    plt.figure(figsize=(10,4))

    plt.plot(x, y1, marker='o', linestyle='-', color='b', label='Voix_premier_tour')
    plt.plot(x, y2, marker='s', linestyle='--', color='r', label='Voix_second_tour')

    plt.title('Nb de voix par partis aux législatives 2024')
    plt.xlabel('Listes des partis')
    plt.ylabel('Nb de voix')
    # Légende verticale
    plt.legend()

    plt.grid(True)
    plt.tight_layout()

    plt.show()