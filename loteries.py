import random
import sys

#################################
#####  Arguments function  ######
#################################

nbboules = 0
first_col = 0
nbboules_c = 0
frequencies = []
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

def proba(lines,col_dic,f_col,nb_b):
	for i in lines:
		cells = i.split(';')
		col_dic[int(cells[f_col])] = col_dic[int(cells[f_col])] + 1
	for k in col_dic.keys():
		col_dic[k] = col_dic[k]/tot_tirages
	return(col_dic)


		# if col_dic[k] < 1/nbboules :                                 
		# 	dmin_b1[k] = dico_col1[k]

def number_choice(col_dic,nb_b,tir):
	dmin = {}
	for k in col_dic.keys():
		if col_dic[k]<1/nb_b :
			dmin[k] = col_dic[k]
	b = random.choice(list(dmin.keys()))
	while(b in tir):
		b = random.choice(list(dmin.keys()))
	return(b)


	

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

dico_col1=proba(lines,dico_col1,first_col,nbboules)

##########################################
# première boule : choix du nombre       # 
##########################################

boule_1 = number_choice(dico_col1,nbboules,tirage)
tirage.append(boule_1)

##################
# deuxième boule # 
##################

##########################################
# deuxième boule : traitement du tableau # 
##########################################

dico_col2 = proba(lines,dico_col2,first_col+1,nbboules-1)

##########################################
# deuxième boule : choix du nombre       # 
##########################################

boule_2 = number_choice(dico_col2,nbboules-1,tirage)
tirage.append(boule_2)

###################
# troisième boule # 
###################

dico_col3=proba(lines,dico_col3,first_col+2,nbboules-2)

##########################################
# troisème boule : choix du nombre       # 
##########################################

boule_3 = number_choice(dico_col3,nbboules-2,tirage)
tirage.append(boule_3)

###################
# quatrième boule # 
###################

dmin_b4 = {}
dico_col4=proba(lines,dico_col4,first_col+3,nbboules-3)

# ##########################################
# # quatrième boule : choix du nombre      # 
# ##########################################

boule_4 = number_choice(dico_col4,nbboules-3,tirage)
tirage.append(boule_4)

###################
# cinquième boule # 
###################

dico_col5=proba(lines,dico_col5,first_col+4,nbboules-4)

##########################################
# cinquième boule : choix du nombre      # 
##########################################

boule_5 = number_choice(dico_col5,nbboules-4,tirage)
tirage.append(boule_5)


#####################
# Première étoile   # 
#####################

dico_cole1 = proba(lines,dico_cole1,first_col+5,nbboules_c)

##########################################
# première étoile : choix du nombre      # 
##########################################

boule_e1 = number_choice(dico_cole1,nbboules_c,tirage_e)
tirage_e.append(boule_e1)

#####################
# Deuxième étoile   # 
#####################


euOrlo = get_arg()

if euOrlo[2] == "euromillions":
	dico_cole2 = proba(lines,dico_cole2,first_col+6,nbboules_c-1)

##########################################
# deuxième étoile : choix du nombre      # 
##########################################

	boule_e2 = number_choice(dico_cole2,nbboules_c-1,tirage_e)
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


# if len(euOrlo)>3:
# 	if euOrlo[3] == "-opt":
# 		if len(euOrlo)>4 and euOrlo[4] == "analyse":
#  			print("première boule : ")
#  			res_1 = input()
#  			print("deuxième boule : ")
#  			res_2 = input()
#  			print("troisème boule : ")
#  			res_3 = input()
#  			print("quatrième boule : ")
#  			res_4 = input()
#  			print("cinquième boule : ")
#  			res_5 = input()
#  			tirage_vrai = []
#  			if euOrlo[2] == "euromillions":
#  				frequencies.extend((dico_col1,dico_col2,dico_col3,dico_col4,dico_col5,dico_cole1,dico_cole2))
#  				print("première étoile : ")
#  				eto_1 = input()
#  				print("deuxième étoile : ")
#  				eto_2 = input()
#  				tirage_vrai.extend((res_1,res_2,res_3,res_4,res_5,eto_1,eto_2))
#  				print(tirage_vrai)
#  				i=0
#  				while i<len(tirage_vrai):
#  					if(frequencies[i][int(tirage_vrai[i])]>1/(nbboules-i)):							
#  						print(tirage_vrai[i] + " fait partie de ceux qui sortent le plus")
#  					else:
#  						print(tirage_vrai[i] + " fait partie de ceux qui sortent le moins")
#  					i = i+1
#  			elif euOrlo[2] == "loto":
#  				frequencies.extend((dico_col1,dico_col2,dico_col3,dico_col4,dico_col5,dico_cole1))
#  				print("numéro chance : ")
#  				num_cha = input()
#  				tirage_vrai.extend((res_1,res_2,res_3,res_4,res_5,num_cha))
#  				print(tirage_vrai)
#  				while i<len(tirage_vrai):
#  					if(frequencies[i][int(tirage_vrai[i])]>1/(nbboules-i)):							
#  						print(tirage_vrai[i] + " fait partie de ceux qui sortent le plus")
#  					else:
#  						print(tirage_vrai[i] + " fait partie de ceux qui sortent le moins")
#  					i = i+1				


##############
##   To do  ##
##############


'''

- readme
- Tout en anglais
- Ne pas faire de tirage quand en mode analyse
- Rajouter les plus
- Création d'un fichier d'analyse :
	- info sur la proba du numéro qui est sorti
	- nombre de fois qu'un numéro sorti à fait partie des plus ou des moins
	- 




'''