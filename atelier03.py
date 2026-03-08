class Voiture:
    def __init__(self, matricule, marque, couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur

    def afficher_infos(self):
        print(f"Matricule:{self.matricule} Marque:{self.marque} Couleur: {self.couleur}")

class Parc:
    def __init__(self, id, adresse, capacite):
        self.id = id
        self.adresse = adresse
        self.capacite = capacite
        self.listeVoitures = []

    def entrerVoiture(self, voiture):
        if voiture in self.listeVoitures:
            print("La voiture existe déjà dans le parc.")
        elif len(self.listeVoitures) >= self.capacite:
            print("Le parc est plein.")
        else:
            self.listeVoitures.append(voiture)
            print("Voiture ajoutée.")