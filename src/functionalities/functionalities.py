import json
import os

from utils.dicoutils import *

class Data_base():

    def __init__(self):
        file = open("../res/data/dicomusic.dat", "r")
        str_dico = file.read()
        self.__dico = json.loads(str_dico)
        file.close()
        os.system("clear")
        print("Base de données chargée.")

    def get_dico(self):
        return self.__dico

    def add_music(self, artist, music):
        """
        Ajoute une musique dans la base de donnée.
        """
        self.__dico[music] = artist

    def remove_music(self, music):
        """
        Retire une musique de la base de donnée.
        """
        dico = self.get_dico()
        os.system("clear")
        remove_element(dico, music)

    def show_data_base(self):
        """
        Affiche le dictionnaire contenant les musiques.
        """
        dico = self.__dico
        os.system("clear")
        print_dico(dico)

    def __del__(self):
        file = open("../res/data/dicomusic.dat", "w")
        str_dico = self.__dico
        json_dico = json.dumps(str_dico)
        file.write(json_dico)
        file.close()
        print("Base de données mise à jour.")
