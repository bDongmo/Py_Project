import pymysql.cursors
import logging
import sys

class Credential:
    '''
    Classe pour construire un utilisateur qui va se connceter avec la bd
    '''
    # User credential
    def __init__(self):
        self.db_user = "root"
        self.db_password = ""
        self.db_host = "localhost"
        self.db_name = "northwindmysql"

class Database:
    '''
    Classe pour la gestion de la connection avec la base de donnee Mysql
    '''
    def __init__(self, config):
        self.host = config.db_host
        self.username = config.db_user
        self.password = config.db_password
        self.dbname = config.db_name
        self.cursorclass = pymysql.cursors.DictCursor
        self.connector = None

    def open_connection(self):
        '''
        instanciation ou construction d'une connection
        :return:aucun
        '''
        try:
            self.connector = pymysql.connect(self.host,
                                        user=self.username,
                                        passwd=self.password,
                                        db=self.dbname,
                                        cursorclass = self.cursorclass)
        except pymysql.OperationalError as err:
            logging.error(err)
            sys.exit()
        finally:
            logging.info('Connection opened successfully.')

    def creation_table(self, cree_table):
        '''
        fonction de création d'une table dans la base de bd "northwindmysql"
        :param cree_table: Requette de creation de la table
        :return: aucun
        '''
        try:
            self.open_connection()
            with self.connector.cursor() as curs:
                curs.execute(cree_table)
                curs.close()
        except pymysql.MySQLError as err:
            logging.error(err)
            sys.exit()
        finally:
            self.connector.close()
            self.connector = None
            logging.info('Database connection closed.')

    def insert_dans_table(self, insertion, val):
        '''
        :param insertion: Requette pour l'insertion des valeurs (val) dans la table
        :param val: tableau de tuple des objets en insérer
        :return: aucun
        '''
        try:
            self.open_connection()
            with self.connector.cursor() as curs:
                    results= curs.executemany(insertion, val)
                    self.connector.commit()
                    affected = f"{curs.rowcount}."
                    curs.close()
                    return affected
        except pymysql.MySQLError as err:
            print(err)
        finally:
            self.connector.close()
            self.connector = None
            logging.info('Database connection closed.')

    def obtenir_de_table(self, selection):
        '''
        fonction pour lire des données depuis une table
        :param selection: Requette pour la selection
        :return: aucun
        '''
        try:
            self.open_connection()
            with self.connector.cursor() as curs:
                list_articles = []
                curs.execute(selection)
                resultat = curs.fetchall()
                for row in resultat:
                    list_articles.append(row)
                curs.close()
                return list_articles
        except pymysql.MySQLError as err:
            print(err)
        finally:
            self.connector.close()
            self.connector = None
            logging.info('Database connection closed.')

