import random
import string
from mots import mots

def getMots(mots):
	return random.choice(mots).upper()

def getLettres(mot):
	return set(mot)

def demandeUtilisateur():
	return input("Donnez une lettre : ").upper()

def initMotCache(mot):
	return [" _ " for _ in range(len(mot))  ]

def pendu(mots):
	vie = 5
	mot = getMots(mots)
	lettres_mots = getLettres(mot)
	u_mot = initMotCache(mot)
	while lettres_mots and vie != 0:
		print(" ".join(u_mot)+" ")
		u = demandeUtilisateur()
		if u in lettres_mots:
			for i in range(len(mot)):
				if mot[i] == u:
					u_mot[i] = u
					if u in lettres_mots :
						lettres_mots.remove(u)
		else :
			vie -= 1
	print(" ".join(u_mot)+" ")

pendu(mots)
