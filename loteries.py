import random
import sys

#################################
#####      Functions       ######
#################################

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

def number_choice(col_dic,nb_b,tir):
	dmin = {}
	for k in col_dic.keys():
		if col_dic[k]<1/nb_b :
			dmin[k] = col_dic[k]
	b = random.choice(list(dmin.keys()))
	while(b in tir):
		b = random.choice(list(dmin.keys()))
	return(b)

def f_analysis(nbboules,nbboules_c,game,d1,d2,d3,d4,d5,de1,de2):
	#print("analysis mode launched")
	frequencies = []
	frequencies_bonus = []		
	print("première boule : ")
	res_1 = input()
	print("deuxième boule : ")
	res_2 = input()
	print("troisème boule : ")
	res_3 = input()
	print("quatrième boule : ")
	res_4 = input()
	print("cinquième boule : ")
	res_5 = input()
	test_combi = []
	test_combie = []
	if game == True:
		frequencies.extend((d1,d2,d3,d4,d5))
		frequencies_bonus.extend((de1,de2))
		print("première étoile : ")
		eto_1 = input()
		print("deuxième étoile : ")
		eto_2 = input()
		test_combi.extend((res_1,res_2,res_3,res_4,res_5))
		test_combie.extend((eto_1,eto_2))
		i=0
		j=0
		while i<len(test_combi):
			if(frequencies[i][int(test_combi[i])]>1/(nbboules-i)):							
				print(test_combi[i] + " fait partie de ceux qui sortent le plus")
			else:
				print(test_combi[i] + " fait partie de ceux qui sortent le moins")
			i = i+1
		while j<len(test_combie):
			if(frequencies_bonus[j][int(test_combie[j])]>1/(nbboules_c-j)):							
				print(test_combie[j] + " fait partie de ceux qui sortent le plus")
			else:
				print(test_combie[j] + " fait partie de ceux qui sortent le moins")
			j = j+1			
	elif game == False:
		frequencies.extend((d1,d2,d3,d4,d5))
		print("numéro chance : ")
		num_cha = input()
		test_combi.extend((res_1,res_2,res_3,res_4,res_5))
		i = 0
		while i<len(test_combi):
			if(frequencies[i][int(test_combi[i])]>1/(nbboules-i)):							
				print(test_combi[i] + " fait partie de ceux qui sortent le plus")
			else:
				print(test_combi[i] + " fait partie de ceux qui sortent le moins")
			i = i+1
		if(de1[int(num_cha)]>1/(nbboules_c-i)):			
			print(num_cha + " fait partie de ceux qui sortent le plus")
		else:
			print(num_cha + " fait partie de ceux qui sortent le moins")

def draw(nbboules,nbboules_c,df1,df2,df3,df4,df5,df6,df7,booli):
	tirage = []
	tirage_e = []
	boule_1 = number_choice(df1,nbboules,tirage)
	tirage.append(boule_1)
	boule_2 = number_choice(df2,nbboules-1,tirage)
	tirage.append(boule_2)
	boule_3 = number_choice(df3,nbboules-2,tirage)
	tirage.append(boule_3)
	boule_4 = number_choice(df4,nbboules-3,tirage)
	tirage.append(boule_4)
	boule_5 = number_choice(df5,nbboules-4,tirage)
	tirage.append(boule_5)
	boule_e1 = number_choice(df6,nbboules_c,tirage_e)
	tirage_e.append(boule_e1)
	if booli == True:
		boule_e2 = number_choice(df7,nbboules_c-1,tirage_e)
		tirage_e.append(boule_e2)
	print("Tirage proposé :\n"+str(tirage[0])+"-"+str(tirage[1])+"-"+str(tirage[2])+"-"+str(tirage[3])+"-"+str(tirage[4]))
	if booli == True:
		print("étoiles : "+str(tirage_e[0])+"-"+str(tirage_e[1]))
	else:
		print("numéro chance : "+str(tirage_e[0]))


###############################################
########  Main program initialization #########
###############################################

nbboules = 0
first_col = 0
nbboules_c = 0
euro = False
analysis = False
simulation = False
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

program_args = get_arg()
if program_args[2] == "euromillions":
	euro = True
if program_args[3] == "analysis":	 
	analysis = True
elif program_args[3] == "simulation":
	simulation = True
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


##########################
# first ball dictionnary # 
##########################

dico_col1=proba(lines,dico_col1,first_col,nbboules)


###########################
# second ball dictionnary # 
###########################

dico_col2 = proba(lines,dico_col2,first_col+1,nbboules-1)

##########################
# third ball dictionnary # 
##########################

dico_col3=proba(lines,dico_col3,first_col+2,nbboules-2)

###########################
# fourth ball dictionnary # 
###########################

dico_col4=proba(lines,dico_col4,first_col+3,nbboules-3)


###########################
#### fifth dictionnary #### 
###########################

dico_col5=proba(lines,dico_col5,first_col+4,nbboules-4)


###########################
# First star dictionnary  # 
###########################

dico_cole1 = proba(lines,dico_cole1,first_col+5,nbboules_c)

#############################
# Second star dictionnary   # 
#############################


euOrlo = get_arg()

if euro == True:
	dico_cole2 = proba(lines,dico_cole2,first_col+6,nbboules_c-1)

######################
###  Main programm ###
######################

if simulation == True:
	draw(nbboules,nbboules_c,dico_col1,dico_col2,dico_col3,dico_col4,dico_col5,dico_cole1,dico_cole2,euro)
if analysis == True:
	f_analysis(nbboules,nbboules_c,euro,dico_col1,dico_col2,dico_col3,dico_col4,dico_col5,dico_cole1,dico_cole2)
##############
##   To do  ##
#############
print(dico_cole1)

'''

- Tout en anglais
- Ne pas faire de tirage quand en mode analyse
- Rajouter les plus
- Création d'un fichier d'analyse :
	- info sur la proba du numéro qui est sorti
	- nombre de fois qu'un numéro sorti à fait partie des plus ou des moins
- Ajouter sécurité sur les arguments
- essayer de faire sans les while et les répétitions dans analysis
- fonction update





'''