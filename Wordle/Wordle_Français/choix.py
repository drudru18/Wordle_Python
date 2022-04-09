from colorama import Fore, Back, Style
import wordle
import wordle_multi
import time

class Choix:
    
    def __init__(self):
        self.choix()
        
    
    def choix(self):
        '''with open("logo.txt", "r") as file:
            for line in file:
                print(line)
        print("\n"*10)'''
        self.mode_de_jeu = str(input("Bonjour, choisissez votre mode de jeu ! \n\t- Pour Joueur vs Ordi, tapez 1\n\t- Pour Joueur vs Joueur, tapez 2\n\t- Pour fermer le programme, tapez 3\n--> "))
        if self.mode_de_jeu == "1":
            return wordle.Wordle()
        elif self.mode_de_jeu == "2":
            return wordle_multi.Wordle_multi()
        elif self.mode_de_jeu == "3":
            exit()
        else:
            print(Fore.LIGHTRED_EX+"\n\n\n:(\n\n\n"+Fore.WHITE)
            time.sleep(2)
            return self.choix()
        
Choix()