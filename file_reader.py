import  csv
from article import Article

class LectureFichier:
    '''
    Classe pour la gestion(ouveture, lecture d'un fichier)
    '''
    def __init__(self, filename):
        '''
        constructeur d'un lecteur de fichier
        :param filename: nom de fichier
        '''
        self.nom_fichier = filename
        self.liste_sortie = []

    def lire_fichier(self):
        '''
        fonction pour la lecture de d'un fichier
        :return: retourne une liste d'objet article
        '''
        with open(self.nom_fichier) as fich:
            lecteur = csv.reader(fich, delimiter=",")
            for ligne in lecteur:
                un_item = ligne[0].split()
                article = Article()
                article.nom = un_item[0]
                article.prix = un_item[2]
                article.quantite = un_item[1]
                self.liste_sortie.append(article)
        return self.liste_sortie

    def ecrire_produit_rabbais(self, lits_rabbais):
        '''
        fonction pour écrire une liste dasn une fichier
        :param lits_rabbais:
        :return: aucun
        '''
        with open("rabais.csv", "a", newline="") as fic:
            ecrivain = csv.writer(fic, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
            for product in lits_rabbais:
                ecrivain.writerow((product.nom, product.prix, product.quantite))

    def lire_fichier_tuple(self):
        '''
        fonction qui lie un fichier et retourne le contenue comme une liste de tuple
        :return: aucun
        '''
        with open("article.csv") as  fich:
            lecteur = csv.reader(fich, delimiter=",")
            items_list = []
            for ligne in lecteur:
                an_item = ligne[0].split()
                items_list.append((an_item[0], an_item[1], an_item[2]))
            return items_list