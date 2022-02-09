import pandas as pd
import numpy as np 

# nous ouvrons tous nos dossiers et les renommons pour plus de clarté 
sous_nutri= pd.read_csv("sous_nutrition.csv")
dispo_ali= pd.read_csv("dispo_alimentaire.csv")
popu= pd.read_csv("population.csv")
aide_ali= pd.read_csv("aide_alimentaire.csv")

Requetes Marc : 
# nous selectionnons les valeurs de l'Année 2017 en prenant l'intervalle 2016-2018
sous_nutri_2017 = sous_nutri.loc[sous_nutri["Année"] == '2016-2018'] 
sous_nutri_2017 ['Population'] = pd.to_numeric(sous_nutri_2017 ['Population'], errors='coerce')
sous_nutri_2017 .fillna(0, inplace=True)

# nous créons une variable b correspondant à la population mondial en 2017
popu_2017 = popu.loc[popu["Année"]== 2017]

# on fusionne nous deux dataframe en une en fusionnant les zones
tableau = pd.merge(sous_nutri_2017 ,popu_2017, on = ["Zone"])

# on supprime les colonnes inutiles 
del tableau["Année_x"]

# on réorganise les zone et les renommons 
tableau = tableau[["Zone","Année_y","Population_x","Population_y"]]
tableau.columns = ["Zone","Année","Population en sous nutrition", "Population mondial"]

# on réajuste les colonnes au même grandeur
tableau["Population en sous nutrition"] = tableau["Population en sous nutrition"] * 1000000
tableau["Population mondial"] = tableau["Population mondial"] * 1000

# on crée une nouvelle colonne moyenne en faisant le pourcentage de sous nutrition par zone et on arrondi à 1
tableau.insert(4, "moyenne", ((tableau["Population en sous nutrition"]*100) / tableau["Population mondial"]))
tableau["moyenne"] = tableau["moyenne"].round(1)

# on crée une nouvelle colonne moyenne total en faisant le pourcentage total de sous nutrition dans le monde 
tableau.insert(5, "moyenne total", ( (tableau["Population en sous nutrition"].sum() * 100) / tableau["Population mondial"].sum() ))
tableau["moyenne total"] = tableau["moyenne total"].round(1)
tableau


La proportion des personnes en état de sous nitrition dans le monde est de 7.1 %
# Requete 2 : le nombre théorique de personnes qui pourraient être nourries ;

# On raseemble la dispo ali et la population année 2017 
dispo_ali_pop = dispo_ali.merge(popu.loc[popu['Année'] == 2017, ["Zone", "Population"]], on= 'Zone')
# On calcul la dispo total en miltipliant par le nbrs d'habitant et par le nbrs de jour pour 1 an 
dispo_ali_pop['dispo_kcal'] = dispo_ali_pop['Disponibilité alimentaire (Kcal/personne/jour)'] * dispo_ali_pop['Population'] * 365 
print("dispo alimentaire total en kcal est de: ", dispo_ali_pop['dispo_kcal'].sum(), "kcal")
# On calcul la moyenne des kcal qu'a besoin un être humain
moy = (2700 + 1800) /2
# on fait la sommes que l'on divise par la moyenne * 365 jour pour 1 an 
total_humain_kcal = round(dispo_ali_pop['dispo_kcal'].sum()/(moy * 365))
print("Le total d'être humain pouvant être nourris est de: ", total_humain_kcal, "être humain ")

print("Proportion :", "{:.2f}".format(total_humain_kcal*100/popu.loc[popu['Année'] == 2017,"Population"].sum()), "%")


# Requete 3: a disponibilité alimentaire des produits végétaux ;

# On selectionne la dispo ali uniquement de végétaux 
dispo_ali_vege = dispo_ali[(dispo_ali['Origine'] == "vegetale") & (dispo_ali['Disponibilité alimentaire (Kcal/personne/jour)'])]
# On la fusionne avec l'année 2017 de population et on effectue le même calcul que précédent 
dispo_ali_pop_vege = dispo_ali_vege.merge(popu.loc[popu['Année'] == 2017, ["Zone", "Population"]], on= 'Zone')
dispo_ali_pop_vege['dispo_kcal'] = dispo_ali_pop_vege['Disponibilité alimentaire (Kcal/personne/jour)'] * dispo_ali_pop_vege['Population'] * 365 
print("dispo alimentaire végétal total en kcal est de: ", dispo_ali_pop_vege['dispo_kcal'].sum(), "kcal")

moy = (2700 + 1800) /2

total_humain_kcal_vege = round(dispo_ali_pop_vege['dispo_kcal'].sum()/(moy * 365))
print("Le total d'être humain pouvant être nourris est de: ", total_humain_kcal_vege, "être humain ")
print("Proportion :", "{:.2f}".format(total_humain_kcal_vege*100/popu.loc[popu['Année'] == 2017,"Population"].sum()), "%")
# requete 4 : l’utilisation de la disponibilité intérieure ; 

# On fait appelle a toutes les sommes des variables que l'on aura besoin 
animal = dispo_ali['Aliments pour animaux'].sum()
perte = dispo_ali['Pertes'].sum()
ali_humaine = dispo_ali['Nourriture'].sum()
dispo_int = dispo_ali['Disponibilité intérieure'].sum()

# On calcul la part de la dispo alimentaire pour animaux 
dispo_int_animal = (animal * 100) / dispo_int
print('La part de la disponibilité intérieur utilisé pour les animaux est de : ', dispo_int_animal,'%') 
print()
# On calcul la part de la dispo alimentaire pour les pertes 
dispo_int_perdue = (perte * 100) / dispo_int 
print('La part de la disponibilité intérieur perdue est de : ', dispo_int_perdue,'%')
print()
# On calcul la part de la dispo alimentaire pour la nourriture 
dispo_int_nourriture = (ali_humaine * 100) / dispo_int
print("La part de la disponibilité intérieur utilisé pour l'alimentation humaine  est de : ", dispo_int_nourriture,'%')

Requetes Melanie :
# nous selectionnons les valeurs de l'Année 2017 en prenant l'intervalle 2016-2018
sous_nutri_2017 = sous_nutri.loc[sous_nutri["Année"] == '2016-2018'] 
sous_nutri_2017 ['Population'] = pd.to_numeric(sous_nutri_2017 ['Population'], errors='coerce')
sous_nutri_2017 .fillna(0, inplace=True)

# nous créons une variable b correspondant à la population mondial en 2017
popu_2017 = popu.loc[popu["Année"]== 2017]

# on fusionne nous deux dataframe en une en fusionnant les zones
tableau = pd.merge(sous_nutri_2017 ,popu_2017, on = ["Zone"])

# on supprime les colonnes inutiles 
del tableau["Année_x"]

# on réorganise les zone et les renommons 
tableau = tableau[["Zone","Année_y","Population_x","Population_y"]]
tableau.columns = ["Zone","Année","Population en sous nutrition", "Population mondial"]

# on réajuste les colonnes au même grandeur
tableau["Population en sous nutrition"] = tableau["Population en sous nutrition"] * 1000000
tableau["Population mondial"] = tableau["Population mondial"] * 1000

# on crée une nouvelle colonne moyenne en faisant le pourcentage de sous nutrition par zone et on arrondi à 1
tableau.insert(4, "moyenne", ((tableau["Population en sous nutrition"]*100) / tableau["Population mondial"]))
tableau["moyenne"] = tableau["moyenne"].round(1)

# on crée une nouvelle colonne moyenne total en faisant le pourcentage total de sous nutrition dans le monde 
tableau.insert(5, "moyenne total", ( (tableau["Population en sous nutrition"].sum() * 100) / tableau["Population mondial"].sum() ))
tableau["moyenne total"] = tableau["moyenne total"].round(1)

# On trie les données par les pays ayant le plus fort taux de sous nutrition 
tableau.sort_values(by = 'moyenne',ascending= False).head(10)

Voici les 10 pays ayant la plus forte proportion de sous nitrition dans le monde 
# Requete 2: Pays ayant bénéficié du plus d’aide depuis 2013;

aide= aide_ali[['Pays bénéficiaire',"Quantité d'aide(T)"]].groupby("Pays bénéficiaire").sum()
aide.sort_values(by = "Quantité d'aide(T)",ascending= False).head(10)
# requete 3: le plus/le moins de disponibilité/habitant;

dispo_pays_total = dispo_ali[['Zone','Produit','Disponibilité alimentaire (Kcal/personne/jour)']].groupby('Zone').sum()
dispo_pays_total.sort_values(by="Disponibilité alimentaire (Kcal/personne/jour)", ascending= False).head(10)
dispo_pays_total = dispo_ali[['Zone','Produit','Disponibilité alimentaire (Kcal/personne/jour)']].groupby('Zone').sum()
dispo_pays_total.sort_values(by="Disponibilité alimentaire (Kcal/personne/jour)").head(10)

Requetes Julien :
dispo_manioc = dispo_ali['Produit']== 'Manioc'
manioc = dispo_ali[dispo_manioc]
part_manioc = manioc['Exportations - Quantité'].sum()
print("La part total de manioc exporter dans le monde est de: ", part_manioc, "millier de tonnes")
dispo_manioc_thaï = dispo_ali[(dispo_ali['Produit']== 'Manioc') & (dispo_ali['Zone'] == 'Thaïlande')]
export_manioc = dispo_manioc_thaï['Exportations - Quantité'].sum() 
print("La part d'exportation du manioc de Thaïlande est: ", export_manioc, "millier de tonnes")
part_thaï_export = (export_manioc * 100) / part_manioc
print("La part en pourcentage de l'export du manioc par la Thaïlande est de: ",round(part_thaï_export, 2), "%")
