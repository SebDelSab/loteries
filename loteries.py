import random
import sys

#################################
#####  Arguments function  ######
#################################

nbboules = 0
first_col = 0
nbboules_c = 0

def get_arg():
	arg_l=[]
	for arg in sys.argv: 
		arg_l.append(arg)
	return(arg_l)

def input_file():
	global nbboules
	global nbboules_c
	global first_col
	loto = "./data/loto.csv"
	euromillions = "./data/euromillions.csv"
	args = get_arg()
	if args[1]=="-i" or args[1]=="--input":
		if args[2] == "loto": 
			nbboules = 49;
			nbboules_c = 10
			first_col = 4
			return(loto)
		elif args[2] == "euromillions":
			nbboules = 50
			first_col = 5
			nbboules_c = 12
			return(euromillions)
		else:
			return(args[2]+" is not a correct argument : use 'loto' or 'euromillions' instead")
	else:
		return(args[1]+" is not a correct argument, use -i or --input to choose the file to convert")

#################################
########  Main program  #########
#################################

game = input_file()
f=open(game,"r")
content = f.read()
lines = content.split('\n')
del(lines[-1]) 
del(lines[0])
f.close()

dico_col1 = {}
dico_col2 = {}
dico_col3 = {}
dico_col4 = {}
dico_col5 = {}
dico_cole1 = {}
dico_cole2 = {} 
tirage = []
tirage_e = []
tot_tirages = len(lines)


l = range(1,nbboules + 1) 
for i in l:
	dico_col1[i] = 0
	dico_col2[i] = 0
	dico_col3[i] = 0
	dico_col4[i] = 0
	dico_col5[i] = 0

l2 = range(1,nbboules_c+1)
for i in l2:
	dico_cole1[i] = 0
	dico_cole2[i] = 0 


##################
# première boule # 
##################

##########################################
# première boule : traitement du tableau # 
##########################################

###########################################################
# Je pars du principe qu'on tend vers l'équilibre         #
# on choisira donc la boule parmi les nombres qui tombent #
# le moins                                                #
###########################################################

dmin_b1 = {}

for i in lines :
 	cells = i.split(';')
 	dico_col1[int(cells[first_col])] = dico_col1[int(cells[first_col])] + 1 

for k in dico_col1.keys():
	dico_col1[k] = dico_col1[k]/tot_tirages
	if dico_col1[k] < 1/nbboules :                                 
		dmin_b1[k] = dico_col1[k]

##########################################
# première boule : choix du nombre       # 
##########################################

boule_1 = random.choice(list(dmin_b1.keys()))
tirage.append(boule_1)

##################
# deuxième boule # 
##################

##########################################
# deuxième boule : traitement du tableau # 
##########################################

dmin_b2 = {}

for i in lines :
	cells = i.split(';')
	if int(cells[first_col+1]) not in tirage:
		dico_col2[int(cells[first_col+1])] = dico_col2[int(cells[first_col+1])] + 1
	else:
		dico_col2[int(cells[first_col+1])] = "tirée"

for k in dico_col2.keys():
	if dico_col2[k]!="tirée":
		dico_col2[k] = dico_col2[k]/tot_tirages
		if dico_col2[k] < 1/(nbboules-1) :
			dmin_b2[k] = dico_col2[k]


##########################################
# deuxième boule : choix du nombre       # 
##########################################

boule_2 = random.choice(list(dmin_b2.keys()))
tirage.append(boule_2)

###################
# troisième boule # 
###################

dmin_b3 = {}

for i in lines :
	cells = i.split(';')
	if int(cells[first_col+2]) in tirage:
		dico_col3[int(cells[first_col+2])] = "tirée"
	else:
		dico_col3[int(cells[first_col+2])] = dico_col3[int(cells[first_col+2])] + 1

for k in dico_col3.keys():
	if dico_col3[k]!="tirée":
		dico_col3[k] = dico_col3[k]/tot_tirages
		if dico_col3[k] < 1/(nbboules-2) :
			dmin_b3[k] = dico_col3[k]

##########################################
# troisème boule : choix du nombre       # 
##########################################

boule_3 = random.choice(list(dmin_b3.keys()))
tirage.append(boule_3)

###################
# quatrième boule # 
###################

dmin_b4 = {}

for i in lines :
	cells = i.split(';')
	if int(cells[first_col+3]) in tirage:
		dico_col4[int(cells[first_col+3])] = "tirée"
	else:
		dico_col4[int(cells[first_col+3])] = dico_col4[int(cells[first_col+3])] + 1

for k in dico_col4.keys():
	if dico_col4[k]!="tirée":
		dico_col4[k] = dico_col4[k]/tot_tirages
		if dico_col4[k] < 1/(nbboules-3) :
			dmin_b4[k] = dico_col4[k]

# ##########################################
# # quatrième boule : choix du nombre      # 
# ##########################################

boule_4 = random.choice(list(dmin_b4.keys()))
tirage.append(boule_4)

###################
# cinquième boule # 
###################

dmin_b5 = {}

for i in lines :
	cells = i.split(';')
	if int(cells[first_col+4]) in tirage:
		dico_col5[int(cells[first_col+4])] = "tirée"
	else:
		dico_col5[int(cells[first_col+4])] = dico_col5[int(cells[first_col+4])] + 1

for k in dico_col5.keys():
	if dico_col5[k]!="tirée":
		dico_col5[k] = dico_col5[k]/tot_tirages
		if dico_col5[k] < 1/(nbboules-4) :
			dmin_b5[k] = dico_col5[k]

##########################################
# cinquième boule : choix du nombre      # 
##########################################

boule_5 = random.choice(list(dmin_b5.keys()))
tirage.append(boule_5)


#####################
# Première étoile   # 
#####################

dmin_e1 = {}

for i in lines :
	cells = i.split(';')
	dico_cole1[int(cells[first_col+5])] = dico_cole1[int(cells[first_col+5])] + 1

for k in dico_cole1.keys():
	dico_cole1[k] = dico_cole1[k]/tot_tirages
	if dico_cole1[k] < 1/nbboules_c :
		dmin_e1[k] = dico_cole1[k]

##########################################
# première étoile : choix du nombre      # 
##########################################

boule_e1 = random.choice(list(dmin_e1.keys()))
tirage_e.append(boule_e1)

#####################
# Deuxième étoile   # 
#####################


euOrlo = get_arg()

if euOrlo[2] == "euromillions":
	dmin_e2 = {}

	for i in lines :
		cells = i.split(';')
		if int(cells[first_col+6]) in tirage_e:
			dico_cole2[int(cells[first_col+6])] = "tirée"
		else:
			dico_cole2[int(cells[first_col+6])] = dico_cole2[int(cells[first_col+6])] + 1
	for k in dico_cole2.keys():
		if dico_cole2[k]!="tirée":
			dico_cole2[k] = dico_cole2[k]/tot_tirages
			if dico_cole2[k] < 1/(nbboules_c-1) :
				dmin_e2[k] = dico_cole2[k]
##########################################
# deuxième étoile : choix du nombre      # 
##########################################

	boule_e2 = random.choice(list(dmin_e2.keys()))
	tirage_e.append(boule_e2)




############
# Résultat # 
############

print("Tirage proposé :\n"+str(tirage[0])+"-"+str(tirage[1])+"-"+str(tirage[2])+"-"+str(tirage[3])+"-"+str(tirage[4]))
if euOrlo[2] == "euromillions":
	print("étoiles : "+str(tirage_e[0])+"-"+str(tirage_e[1]))
elif euOrlo[2] == "loto":
	print("numéro chance : "+str(tirage_e[0]))


#########################################
# Vérification de l'hypothèse de départ # 
#########################################

print(euOrlo)
if len(euOrlo)>3:
	if euOrlo[3] == "-opt":
		if len(euOrlo)>4 and euOrlo[4] == "analyse":
			print("première boule : ")
			res_1 = input()
			print("deuxième boule : ")
			res_2 = input()
			print("troisème boule : ")
			res_3 = input()

