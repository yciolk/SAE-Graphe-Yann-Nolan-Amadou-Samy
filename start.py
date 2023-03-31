import random

####################### INITIALISATION ############################

liste_produits= ["Saucisson de porc 4 ans d’âge", "Saucisses sèches Justin Bridou", "Saucissons aux noix", "Œufs de poules fermières françaises",
                 "Crème fraiche", "Beurre doux", "Beurre salé ", "Lait de vache", "Pommes bio, françaises et locales", "Poires bio, françaises et locales",
                 "Contrat de propriété immobilière pour résidence 4 pièces à Nantes", "Actions dans l’entreprise immobilière Landmaster",
                 "Côte Rôtie du Domaine David 2019", "Champagne Krug 2021", "« Vin » de la Cour écarlate", "Tomme de Savoie", "Chèvre Frais", "Raclette",
                 "Mimolette", "Pain aux graines", "Baguette Paysanne", "Baguette", "Baguette tradition", "Baguette aux lardons", "Pain à l'ail", "Tomates",
                 "Pommes de terre", "Chou", "Chou rouge", "Carotte", "Poireau", "Citrouille", "Potimarron", "Marron", "Pomme", "Clémentine", "Orange",
                 "Kiwi", "Ananas", "Grenade", "Cerise", "Fruit de la passion", "Framboise", "Fraise", "Amandes", "Céréales", "Noisettes", "Chips",
                 "Bretzels", "Crouton", "Tour Eifel", "Yoyos ", "Dromadaire de poche", "Jus de Pomme", "Jus de Raisin", "Jus d'Orange", "Yaourt",
                 "Pâtes feuilletées", "Pâte brisée", "Fromage", "Lardons", "Jambon", "Poulet", "Dindon", "Oie", "Rillettes", "Jambon sec", "Rosette",
                 "Cilit BANG", "Canard", "Ajax", "Herbes", "Curry", "Ail des ours", "Paprika", "Cannelle", "Savon de Marseille", "Gel douche", "Rasoir",
                 "Gel", "Cire", "Shampoing", "Truite", "Bar", "Anchois", "Bigorneau", "Pavé de Bœuf", "Cordon Bleu", "Agneau", "Faux filet", "Poulet Roti",
                 "Cochon à la broche", "Hachis Parmentier", "Bouchée à la reine"]
liste_course:list=[]

liste_localisation_produits=[(0,1),(0,2)]

liste_non_access=[(0,5)]


# plateau 51x50
# {ligne :{ colonne : accecible, clé_liste } }

plan={0 :{0 : (1, 0), 1 : (1, 0), 2 : (1, 0), 3 : (1, 0), 4 : (1, 0), 5 : (1, 1), 6 : (1, 0), 7 : (1, 0), 8 : (1, 0), 9 : (1, 0), 10 : (1, 0), 11 : (1, 0), 12 : (1, 0), 13 : (1, 0), 14 : (1, 0),  15 : (1, 0), 16 : (1, 0), 17 : (1, 0), 18 : (1, 0), 19 : (1, 0), 20 : (1, 0), 21 : (1, 0), 22 : (1, 0), 23 : (1, 0), 24 : (1, 0), 25 : (1, 0), 26 : (1, 0), 27 : (1, 0), 28 : (1, 0), 29 : (1, 0), 30 : (1, 0), 31 : (1, 0), 32 : (1, 0), 33 : (1, 0), 34 : (1, 0), 35 : (1, 0), 36 : (1, 0), 37 : (1, 0), 38 : (1, 0), 39 : (1, 0), 40 : (1, 0), 41 : (1, 0), 42 : (1, 0), 43 : (1, 0), 44 : (1, 0), 45 : (1, 0), 46 : (1, 0), 47 : (1, 0), 48 : (1, 0), 49 : (1, 0), 50 : (1, 0), 51 : (1, 0)}}


longueur_plan=51
largeur_plan=50

##################### FONCTIONS #########################

def creation_lite_course():
    
    i:int=1
    taille=len(liste_produits)
    n:int=0
    
    for i in range (20):
        n=random.randint(1,taille-1)
        liste_course.append(liste_produits[n])
    return liste_course
    
def init_accecibilite(plan):
    
    i:int=0
    j:int=0
    
    for i in range (longueur_plan):
        for j in range (largeur_plan):
            for k in liste_non_access:
                if k==(i,j):
                    copie_article = plan[i][j][1]
                    plan[i].update({j : (0,copie_article)})
    return plan
                
def init_item_pos(plan):
    
    i:int=0
    j:int=0
    
    for i in range (longueur_plan):
        for j in range (largeur_plan):
            for k in range(len(liste_localisation_produits)):
                if liste_localisation_produits[k]==(i,j):
                    copie_access = plan[i][j][0]
                    plan[i].update({j : (copie_access,k)})
    return plan

###################################################################
############################# MAIN ################################
###################################################################

if __name__ == '__main__':
    liste=creation_lite_course()
    print (liste)
    
    access=init_accecibilite(plan)
    print (access)
    
    placement_items=init_item_pos(plan)
    print(plan)