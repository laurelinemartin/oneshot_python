# Chiffrement de César
import random

#Retrouver le code ascii pour 'a' et 'z'
def affiche_code_ascii():
	print(ord('A'), " ", ord('Z'))

#Première fonction à coder
#Fonction qui chiffre à +3
def encrypt3(strg):
	enc = ""
	for c in strg:
		enc += chr(ord(c) + 3)
	return enc

#Deuxième fonction à coder
#Cette fonction chiffre que les lettres minuscules et laisses le reste de la ponctuation en état
#Toujour à +3
def encrypt_only_min(strg):
	enc = ""
	for c in strg:
		#Si le code ASCII de c est dans l'intervalle [97; 122] alors le chiffrer
		if ord(c) >= 97 and ord(c) <= 122 :
			temp = ord(c) + 3
			if temp > 122:
				enc += chr((temp % 122) + 96)
			else:
				enc += chr(temp)
		else:
			enc += c
	return enc

#Troisième fonctions à coder
#Cette fonction chiffre les lettres seulement en majuscules en laissant les caractères spéciaux.
#Toujour à +3
def encrypt_only_maj(strg):
	enc = ""
	for c in strg:
		if ord(c) >= 65 and ord(c) <= 90 :
			temp = ord(c) + 3
			if temp > 90:
				enc += chr((temp % 90) + 64)
			else:
				enc += chr(temp)
		else:
			enc += c
	return enc

#Quatrième fonction à coder
#Cette fonction chiffre les lettres majuscules et minisucules en laissant les caractères spéciaux en état
#Toujour à +3
def encrypt_all_letters(strg):
	enc = ""
	for c in strg:
		if ord(c) >= 97 and ord(c) <= 122:
			enc += encrypt_only_min(c)
		elif ord(c) >= 65 and ord(c) <= 90:
			enc += encrypt_only_maj(c)
		else:
			enc += c
	return enc

#Cinquième, sixième et septième fonctions à coder
#Prendre pour argument le décalage en plus de la chaine
def encrypt_only_min_dec(c, dec):
	enc = chr(ord(c) + dec)
	if ord(enc) > 122:
		enc = chr((ord(enc) % 122) + 96)
	return enc

def encrypt_only_maj_dec(c, dec):
	enc = chr(ord(c) + dec)
	if ord(enc) > 90:
		enc = chr((ord(enc) % 90) + 64)
	return enc	

def encrypt(strg, dec):
	enc = ""
	for c in strg:
		temp = ord(c)
		if temp >= 65 and temp <= 90:
			enc += encrypt_only_maj_dec(c, dec)
		elif temp >= 97 and temp <= 122:
			enc += encrypt_only_min_dec(c, dec)
		else:
			enc += c
	return enc

#Huitième fonction à coder
#Déchiffrer 
#ahah c'est le piège, il suffit d'entrer "-la valeur"

#Neuvième fonction à coder
#Ok mais si on ne connait pas la valeur du chiffré ?
#Réitérer 25 fois et écrire les phrases dans un fichier !
def decrypt(strg):
	i = 1
	f = open('cypher/dechiffre.txt', 'w')
	while(i < 26):
		f.write(encrypt(strg, i))
		f.write("\n")
		i = i+1
	print("Fin de séquence")
	f.close()

#Dixième fonction
#On peut implémenter une fonction pour chiffrer les caractères spéciaux par exempl

#Onzième fonction
#On peut implémenter une fonction pour lire un fichier contenant une phrase ou plus à chiffrer/déchiffrer

#Douzième fonction
#Choisir aléatoirement un nombre entre 1 et 25 pour chiffrer son message
def decalage_aleatoire():
	return random.randint(1, 25)


# -----------------------------------------------------------

chaine = ""
#affiche_code_ascii()
chaine = input("Entrez une chaîne à déchiffrer : ")
# decalage = input("Entrez le décalage à appliquer : ")
# print(encrypt3(chaine))
# print(encrypt_only_min(chaine))
# print(encrypt_all_letters(chaine))
# print(encrypt(chaine, (int(decalage))))
# chaine = encrypt(chaine, decalage_aleatoire())
# print(chaine)
decrypt(chaine)
