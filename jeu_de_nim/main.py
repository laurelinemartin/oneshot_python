jeu=[]
curseur=19

for i in range(20):
	jeu.append("|")


while '|' in jeu:
	print("".join(jeu)+"")
	reponse = int(input("1,2,3 ? "))
	if reponse !=1 and reponse !=2 and reponse!=3:
		print('  ') 
		continue
	
	for c in range(reponse):
		jeu[curseur] = " "
		curseur = curseur-1

	if reponse == 1:
		for c in range(3):
			jeu[curseur] = " "
			curseur = curseur-1
		print ("Je prends 3")
	elif reponse == 2:
		for c in  range(2):
			jeu[curseur] = " "
			curseur= curseur -1
		print ("Je prends 2")
	elif reponse == 3:
		for c in range(1):
			jeu[curseur] = " "
			curseur= curseur -1
		print ("Je prends 1")

print ("C'est perdu...")
