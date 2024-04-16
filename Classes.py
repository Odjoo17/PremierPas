# Exercice en ligne permettant d'apprendre la notion de classes
class Etudiant: # 1ère classe

    def __init__(self,d_nom,d_prenom,d_notes = []) -> None:
        self.nom = d_nom
        self.prenom = d_prenom
        self.notes = d_notes
    
    def moyenne (self) :
        notes = self.notes
        if len(notes) == 0 :
            print(f"L'étudiant {self.nom} n'a pas encore de notes")
        else : 
            print(f"L'étudiant {self.nom} a {sum(notes)/len(notes)} de moyenne")

etudiant_1 = Etudiant("Jean","Pascal",[20,10,0])
etudiant_2 = Etudiant("Anne","Claire")
# etudiant_1.moyenne()
# etudiant_2.moyenne()

class Rectangle: # Exercice 1 
    def __init__(self,d_longueur = 0, d_largeur = 0) -> None:
        self.longueur = d_longueur
        self.largeur = d_largeur
    
    def Perimetre(self):
        return 2*(self.longueur+self.largeur)

    def Surface(self):
        return self.longueur * self.largeur

class Parallelepipede(Rectangle):
    def __init__(self, d_longueur=0, d_largeur=0, d_hauteur = 0) -> None:
        Rectangle.__init__(self,d_longueur, d_largeur)
        self.hauteur = d_hauteur
    
    def Volume(self):
        return self.longueur * self.largeur * self.hauteur

# monRectangle = Rectangle(7, 5)
# monParallelepipede = Parallelepipede(7,5,2)
# print("Le périmètre de mon rectangle est :",monRectangle.Perimetre())
# print("La surface de mon rectangle est :", monRectangle.Surface())
# print("Le volume de mon parallelepipede est :", monParallelepipede.Volume())

class CompteBancaire : # Exercice 2
    def __init__(self,numeroCompte : int, nom : str, solde) -> None:
        self.numeroDeCompte = numeroCompte
        self.nom = nom
        self.solde = solde

    def Versement(self,montant : int):
        self.solde += montant
    
    def Retrait(self,montant : int):
        if self.solde < montant :
            print("Impossible d'effectuer l'opération")
        else :
            self.solde -= montant
    
    def Agios(self) :
        self.solde *= 95/100
    
    def Afficher(self):
        print(f"le client {self.nom} de numéro de compte {self.numeroDeCompte} a un solde de {self.solde}.")

# monCompte = CompteBancaire(16168891, " Bouvier David", 22300)
# monCompte.Versement(1500)
# monCompte.Retrait(24000)
# #monCompte.Agios()
# monCompte.Afficher()

import numpy as np
class Cercle :
    def __init__(self,a,b,r) -> None:
        self.a = a
        self.b = b
        self.r = r

    def Perimetre(self) :
        return 2*np.pi*self.r
    def Surface(self) :
        return np.pi*(self.r)**2

    def testAppartenance(self,coord : tuple = (0,0)) :
        return (np.sqrt((coord[0]-self.a)**2+(coord[1]-self.b)**2)) < self.r

class Vehicule():
    def __init__(self,marque,modele,annee) -> None:
        self.marque = marque
        self .modele = modele
        self.annee = annee
    def demarrer():
        pass
    def arreter():
        pass

class Voiture(Vehicule):
    def __init__(self,marque,modele,annee,nombre_de_portes) -> None:
        super().__init__(self,marque,modele,annee)
        self.nombre_de_portes = nombre_de_portes

class Moto():
    def __init__(self,marque,modele,annee,cylindree) -> None:
        Vehicule.__init__(self,marque,modele,annee)
        self.cylindree = cylindree