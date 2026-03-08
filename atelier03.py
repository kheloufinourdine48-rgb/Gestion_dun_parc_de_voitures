class Voiture:
    def __init__(self, matricule, marque, couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur

    def afficher_infos(self):
        print(f"Matricule:{self.matricule} Marque:{self.marque} Couleur: {self.couleur}")

