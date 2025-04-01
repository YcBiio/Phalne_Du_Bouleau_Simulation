import matplotlib.pyplot as plt
from collections import deque
from simulation import genes, NB_PHALENES

# Historique des populations
historique_noires = deque(maxlen=50)
historique_blanches = deque(maxlen=50)
generation = 0

def update_graph():
    """ Met à jour le graphique d'évolution des populations """
    global generation
    generation += 1

    nb_noires = sum(1 for c in genes if c == 0)
    nb_blanches = NB_PHALENES - nb_noires

    historique_noires.append(nb_noires)
    historique_blanches.append(nb_blanches)

    plt.clf()
    plt.plot(historique_noires, label="Phalènes Noires", color="black")
    plt.plot(historique_blanches, label="Phalènes Blanches", color="gray")
    plt.legend()
    plt.xlabel("Générations")
    plt.ylabel("Population")
    plt.title("Évolution des Phalènes")
    plt.pause(0.01)
