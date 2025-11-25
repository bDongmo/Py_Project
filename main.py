from mod_fonctions import *
from database import Credential, Database

#-----------------------------------------------------------------------------------------------------------------------
###                                         Module Main
#-----------------------------------------------------------------------------------------------------------------------

MENU = """                         Bienvenu(e)!

            ------------------------- partie 1 -------------------------------
    (1). Appuyer "1" pour lire et  afficher la liste d' articles du fichier en console
            ------------------------- partie 2 et 3 --------------------------
    (2). Appuyer "2" pour effectuer un rabais sur certains articles et afficher en console 
                            et écire dans un fichier
            ------------------------- partie 4 --------------------------
    (3). Appuyer "3" pour refaire les parties 1 à 3 avec une base de donnée Mysql.
            ------------------------- partie 5 --------------------------
    (4). Appuyer "4" pour quitter le programme et le ré-exécuter.

"""

def main(entree, menu, msgre):

    fichier_lue = LectureFichier(FILENAME)

    while 1<= entree <= 4:
        if   entree ==1:
            execution_1(fichier_lue)
            entree = demande_rexecution(menu,msgre)
        elif entree == 2:
            liste_art_rabaisser = execution_2(fichier_lue)
            fichier_lue.ecrire_produit_rabbais(liste_art_rabaisser)
            entree = demande_rexecution(menu, msgre)
        elif entree == 3:
            print("execution partie 4 ")
            values = fichier_lue.lire_fichier_tuple()
            config = Credential()
            db = Database(config)
            print("création de la table dans la bd par défaut <<northwindmysql>>.\n")
            db.creation_table(REQ_CREE_TABLE)
            print("insertion du fichier lue dans la bd.\n")
            affected1 = db.insert_dans_table(REQ_INSERTION, values)
            list_articles = db.obtenir_de_table(REQ_SELECTION)
            print("nombre de lignes insérer dans la bd {}".format(affected1))
            affiche_list_dictionnaire(list_articles)
            quantite = saisir_quantite(MSG_QUANTITE_LIMITE, QUANTITE_LIMITE)
            taux = saisir_taux(MSG_TAUX_LIMITE, RABBAIS_MAXIMUN)
            rabais_list = rabais_liste_dictionnaire(list_articles,quantite,taux)
            print("affichage de produits en rabbais:\n")
            affiche_list_tuple(rabais_list)
            print("Nouvelle écriture dans la base de données")
            affected2 = db.insert_dans_table(REQ_INSERTION, rabais_list)
            print("nombre de lignes rajoutés dans la bd {}".format(affected2))
            entree = demande_rexecution(menu, msgre)
        else:
            print("Vous avez arreter l'execution. Fin du programme.")
            sys.exit()



entree = saisir_entrer(MENU)

main(entree, MENU, MESSSAGE_REXECUTION)




