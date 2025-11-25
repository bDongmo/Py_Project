class Article:
    '''
    Classe pour instancier un article
    '''
    def __init__(self): # nom, prix, quantite
        '''
        constructeur d'un article
        '''
        self.nom  = "" #nom
        self.prix = 0.0 #prix
        self.quantite = 0 #quantite
        self.taux = 0.0

    def affiche_un_article(self):
        '''
        fonction pour afficher un article
        :return: aucun
        '''
        un_article = """
                article:  {}
                prix:     {}
                quantité: {}""".format(self.nom, self.prix, self.quantite)
        print (un_article)

    def affiche_les_articles(self, liste_article):
        '''
        fonction pour afficher une liste d'articles. Elle itere la fonction ffiche_un_article
        sur la liste qui lui est passée
        :param liste_article:
        :return: aucun
        '''
        underigne ="="*25
        for item in liste_article:
            item.affiche_un_article()
            print(underigne.center(50) )

    def rabais_sur_articles(self, items_list):
        '''
        fonction pour calculer un le rabbais sur un article.
        :param items_list: list de produit
        :return: liste d'articles en rabais
        '''
        article_en_rabais = []
        for item in items_list:
            if int(item.quantite) <= int(self.quantite):
                new_price =(1 - self.taux) * float (item.prix)
                item.prix = str("%.2f" % new_price)
                item.nom = item.nom.upper()
            article_en_rabais.append(item)
        return article_en_rabais