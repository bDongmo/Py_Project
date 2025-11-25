import sys
from article import Article
from file_reader import LectureFichier
#-----------------------------------------------------------------------------------------------------------------------
#####                                        Constante.
#-----------------------------------------------------------------------------------------------------------------------
FILENAME = "article.csv"
QUANTITE_LIMITE = 30
RABBAIS_MAXIMUN = 0.25

MESSSAGE1 = "Affichage de la liste en console"
MESSSAGE2 = "Rabbais de produits"
MESSSAGE3 = "Ecrire les produits en Rabbais dans un fichier"
MSG_QUANTITE_LIMITE = "S.P.V, entrer la quantite limite pour faire le tri des produits a rabaisser [1 à 30]: "
MSG_TAUX_LIMITE = "S.P.V, entrer un taux de rabbais [0.0 à 0.25]: "
MESSSAGE_REXECUTION = "Voulez-vous faire une autre execution(Y/N)? (Y pour Yes et N pour No)\n"


#-----------------------------------------------------------------------------------------------------------------------
#####                                         Requettes.
#-----------------------------------------------------------------------------------------------------------------------

REQ_CREE_TABLE = """ CREATE TABLE IF NOT EXISTS Magasin ( 
    article_id INT AUTO_INCREMENT UNIQUE,
    nom VARCHAR(30) NOT NULL,
    prix FLOAT,
    quantite INT UNSIGNED,
    PRIMARY KEY (article_id, nom)
    )"""

REQ_INSERTION = "INSERT INTO Magasin (nom ,quantite, prix) VALUES (%s, %s, %s)"
REQ_SELECTION = "SELECT nom, quantite, prix FROM Magasin"


#-----------------------------------------------------------------------------------------------------------------------
#####                                  Fonctions utiles de test
#-----------------------------------------------------------------------------------------------------------------------
def saisir_taux(msg, limite):
    '''
    fonction d'invite à la saisie d'une valeur de type float (taux de rabais) avec
    validation d'une limite reelle definie constante
    :param msg: string
    :param limite: float (Constante: taux maximale de rabais)
    :return: float (taux de rabais limite voulu par l'utilisateur) .
    '''
    valeur = 0
    while not (0< valeur <= limite):
        valeur = float(input(msg))
    return valeur

#-----------------------------------------------------------------------------------------------------------------------
#                                     fonction saisir_quantite()
#-----------------------------------------------------------------------------------------------------------------------
def saisir_quantite(msg, limite):
    '''
    fonction d'invite à la saisie d'une valeur de type int (limite pour le choix des produit a rabaisser)
    avec validation d'une limite entière
    :param msg: string
    :param limite: int (Constante: limite des quantités a rabaisser)
    :return: int (valeur limite lue)
    '''
    valeur = 0
    while not (1<= valeur <= limite):
        valeur = int(input(msg))
    return valeur

#-----------------------------------------------------------------------------------------------------------------------
#                                     fonction saisir_entrer()
#-----------------------------------------------------------------------------------------------------------------------
def saisir_entrer(msg):
    '''
    fonction d'invite à la saisie d'une valeur entre 1 et 4 pour le choix du menu
    :param msg: string (message de d'invite)
    :return: int (valeur lue)
    '''
    entrer = 0
    while not 1 <= entrer <=4 :
        entrer= int(input(msg))
    return entrer

#-----------------------------------------------------------------------------------------------------------------------
#                                     fonction demande_rexecution()
#-----------------------------------------------------------------------------------------------------------------------
def demande_rexecution(menu, msgre):
    '''
    fonction de demande de reexecution du menu
    :param menu: string du menu
    :param msgre: message d'invite
    :return: string (Y ou N pour Yes or No)
    '''
    lue = input(msgre)
    if lue =="Y":
        entree = saisir_entrer(menu)
        return entree
    elif lue =="N":
        print("Vous avez terminé l'exécution: Fin du programme.")
        sys.exit()

#-----------------------------------------------------------------------------------------------------------------------
#                                     fonction execution_1()
#-----------------------------------------------------------------------------------------------------------------------
def execution_1(fich_lue):
    '''
    Cette fonction exécute la lecture d'un objet fichier et affiche son contenu
    grace a la fonction affiche_les_articles() de la classe articles
    :param fich_lue: objet fihcier
    :return: aucune valeur de retour
    '''
    print(MESSSAGE1)
    print("="*35)
    article1 =Article()
    liste_articles = fich_lue.lire_fichier()
    article1.affiche_les_articles(liste_articles)

#-----------------------------------------------------------------------------------------------------------------------
#                                     fonction execution_2()
#-----------------------------------------------------------------------------------------------------------------------
def execution_2(fich_lue):
    '''
    Cette fonction effectue un rabbais sur des articles grace a la fonction
    rabais_sur_article de la classe article
    :param fich_lue: objet fihcier
    :return: liste d'articles
    '''
    print(MESSSAGE2)
    print("=" * 35)
    quantite = saisir_quantite(MSG_QUANTITE_LIMITE, QUANTITE_LIMITE)
    taux = saisir_taux(MSG_TAUX_LIMITE, RABBAIS_MAXIMUN)
    article2= Article()
    article2.quantite = quantite
    article2.taux = taux
    liste_art = fich_lue.lire_fichier()
    article_rabaisser = article2.rabais_sur_articles(liste_art)
    article2.affiche_les_articles(article_rabaisser)
    return article_rabaisser

#-----------------------------------------------------------------------------------------------------------------------
#                                     fonction affiche_list_dictionnaire()
#-----------------------------------------------------------------------------------------------------------------------
def affiche_list_dictionnaire(liste):
    '''
    Cette fonction effectue l'affichage d'une liste de dictionnaires qu'on lui fournie
    :param liste:
    :return: aucun
    '''
    for item in liste:
        print(" article: {}\n prix:     {}\n quantité: {}".\
              format(item["nom"], item["prix"], item["quantite"]))
        print("*"*35)

#-----------------------------------------------------------------------------------------------------------------------
#                                     fonction affiche_list_tuple()
#-----------------------------------------------------------------------------------------------------------------------
def affiche_list_tuple(une_liste):
    '''
    Cette fonction effectue l'affichage d'une liste de tuple qu'on lui fournie
    :param une_liste:
    :return: aucun
    '''
    for item in une_liste:
        print(" article: {}\n quantite:     {}\n prix: {}".\
              format(item[0], item[1], item[2]))
        print("*"*35)


#-----------------------------------------------------------------------------------------------------------------------
#                                     fonction rabais_liste_dictionnaire()
#-----------------------------------------------------------------------------------------------------------------------
def rabais_liste_dictionnaire(in_liste, quant_limit, taux):
    '''
    fonction pour calculer le rabais sur les articles
    :param in_liste: liste de dictionnaire à trier et a effectuer le rabais
    :param quant_limit: int (quantite limite pour le tri des articles)
    :param taux:float (taux de rabbais sur le produit)
    :return: out_list (liste de tuple)
    '''
    out_list = []
    for item in in_liste:
        if item["quantite"] <= quant_limit:
            item["prix"] = ("%.2f") % (item["prix"]*(1-taux))
            out_list.append((item["nom"].upper(), item["quantite"], item["prix"]))
    return out_list
