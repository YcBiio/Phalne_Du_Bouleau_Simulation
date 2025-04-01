import random
from config import NB_PHALENES, FREQ_MUTATION, PREDATEUR_EFFICACITE, COULEUR_ARBRE

phalènes = []
genes = []  # 0 = noire, 1 = blanche

def init_phalenes():
    """ Génère une population initiale de phalènes avec des allèles """
    global phalènes, genes
    phalènes = [(random.uniform(0, 1), random.uniform(0, 1)) for _ in range(NB_PHALENES)]
    genes = [random.choice([0, 1]) for _ in range(NB_PHALENES)]

def chasse():
    """ Simule la chasse des prédateurs en fonction de la visibilité """
    global phalènes, genes
    survivants = []
    survivants_genes = []

    for i in range(len(phalènes)):
        x, y = phalènes[i]
        couleur = genes[i]

        # Calcul de la visibilité selon la couleur de l’arbre
        contraste = abs(COULEUR_ARBRE - (255 if couleur == 1 else 0)) / 255

        # Probabilité d'être mangé selon la visibilité et l'efficacité du prédateur
        if random.random() > contraste * PREDATEUR_EFFICACITE:
            survivants.append((x, y))
            survivants_genes.append(couleur)

    # Mise à jour des populations
    phalènes = survivants
    genes = survivants_genes

    # Reproduction des survivants avec mutations
    while len(phalènes) < NB_PHALENES:
        parent = random.choice(survivants_genes)
        if random.random() < FREQ_MUTATION:
            parent = 1 - parent  # Mutation

        phalènes.append((random.uniform(0, 1), random.uniform(0, 1)))
        genes.append(parent)
