from colorama import Fore, Back, Style
import Singleplayer.wordle as sp
import Multiplayer.wordle_multi as mp
import Other.istats as st
import time

class Choix:
    
    def __init__(self):
        self.choix()
    
    def choix(self):
        self.mode_de_jeu = str(input("\n\n\n\n\n\n\n\nBonjour, choisissez votre mode de jeu ! \n\t- Pour Joueur vs Ordi, tapez 1\n\t- Pour Joueur vs Joueur, tapez 2\n\t- Pour afficher les statistiques ou les effacer, tapez 3\n\t- Pour fermer le programme, tapez 4\n--> "))
        if self.mode_de_jeu == "1":
            return sp.Player()
        elif self.mode_de_jeu == "2":
            return mp.Player()
        elif self.mode_de_jeu == "3":
            self.choose = str(input("Voulez-vous afficher les statistiques ou les effacer ?\n\n\n\tTapez 1 pour les afficher\n\n\tTapez 2 pour les effacer\n\n>> "))
            if self.choose == "1":
                return st.Stats().show_stats()
            elif self.choose == "2":
                return st.Stats().choose_name()
            else:
                print("Choisissez entre 1 et 2!")
                time.sleep(3)
                return Choix()
        elif self.mode_de_jeu == "4":
            exit()
        else:
            print(Fore.LIGHTRED_EX+"\n\n\n:(\n\n\n"+Fore.WHITE)
            time.sleep(2)
            return self.choix()