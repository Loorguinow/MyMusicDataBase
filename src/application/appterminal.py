from time import sleep
import os

from functionalities.functionalities import Data_base

class Appterminal():
    """
    Permet de créer l'application utilisateur dans le terminal de commande
    de l'utilisateur.
    """

    def __init__(self):
        self.__data_base = Data_base()
        self.__running = True
        self.create_application()

    def create_application(self):
        """
        Créée l'application sur le terminal.
        """
        while self.__running :
            print("\n\n\n\n\n\n\n\n\n\nVoulez-vous :\n-Consulter vos musiques\n-Ajouter une musique\n-Retirer une musique\n-Quitter le programme")
            choice = input("\n\n\n\t\t")

            if choice in "consulterCONSULTER":
                self.__data_base.show_data_base()

            elif choice in "ajouterAJOUTER":
                while choice != "":
                    sleep(0.5)
                    print("Quel est le nom de votre artiste : ")
                    name = input()
                    if name == "":
                        choice = ""
                        os.system("clear")
                        break
                    print("et le titre de la musique : ")
                    title = input()
                    if title == "":
                        choice = ""
                        os.system("clear")
                        break
                    self.__data_base.add_music(name, title)
                    sleep(0.5)
                    print("\n\n\n\n\nMusique ajoutée.")

            elif choice in "retirerRETIRER":
                while choice != "":
                    sleep(1)
                    print("Quel est le titre de votre musique : ")
                    name = input()
                    if name == "":
                        choice = ""
                        os.system("clear")
                        break
                    self.__data_base.remove_music(name)
                    sleep(0.5)
                    print("\n\n\n\n\nMusique effacée.")

            elif choice in "quitterQUITTER":
                print("Arrêt du programme...")
                sleep(2)
                running = False

            else:
                "Vous avez écrit une coquille, réessayez (>OxO)>"
