#-*- coding: UTF-8 -*-

#import choix
from colorama import Fore, Back, Style
import codecs
import random
import time


class Wordle_multi:
    
    def __init__(self):
        self.count = 0
        self.liste = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.l = []
        self.pc_word = str(input("\n"*100+"Veuillez entrer un mot qui existe dans la langue française et qui contient 2 caractères minimum et 15 caractères maximum (tapez "+Fore.LIGHTYELLOW_EX+"exit"+Fore.WHITE+" si vous voulez fermer le programme):\n--> "))
        if self.pc_word.lower() == "exit":
            exit()
        self.words()
        if len(self.pc_word) < 2 or len(self.pc_word) > 15:
            print("Entrez une longueur plus grande ou égale à 2 ou une longueur plus petite ou égale à 15 !")
            time.sleep(5)
            return Wordle_multi()
        elif self.pc_word not in self.l:
            print("Veuillez entrer un mot qui existe dans le dictionnaire !")
            time.sleep(5)
            return Wordle_multi()
        self.choose_length()
        with open("essays.txt", "w") as file:
            file.truncate()
            file.close()
        
    def words(self):
        with codecs.open('liste_francais.txt', 'r') as file:
            for line in file:
                if len(line) == len(self.pc_word)+1:
                    self.l+=line.lower().split()
        file.close()
        return self.l
    
    def choose_length(self):
        self.number = str(input("\n"*100+"Tapez "+Fore.YELLOW+ 'help'+Fore.WHITE +" pour savoir comment jouer, tapez "+Fore.YELLOW+ 'fermer' +Fore.WHITE+" pour fermer le programme ou tapez \n"
                                +Fore.YELLOW+"passer "+Fore.WHITE+"pour passer ces consignes: \n --> "))
        if self.number.lower() == "help":
            return (self.helping())
        elif self.number.lower() == "fermer":
            exit()
        elif self.number.lower() == "passer":
            return (self.actions())
        else:
            print("Veuillez taper 'help' ou 'fermer' !\n")
            return (self.choose_length())
                
    def actions(self):
        self.user_word = input("\n\nChoisissez un mot de taille "+Fore.LIGHTBLUE_EX+str(len(self.pc_word))+Fore.WHITE+" (si vous voulez abandonner, tapez" + Fore.YELLOW + " exit" + Fore.WHITE + "):\n-->  ")
        self.count += 1
        if self.user_word == "exit":
            print("\nLe mot qu'il fallait trouver était "+Fore.LIGHTGREEN_EX+self.pc_word+Fore.WHITE+ " !\n"
                  "Attendez 5 secondes s'il vous plaît\n")
            time.sleep(5)
            with open("essays.txt", "w") as file:
                file.truncate()
                file.close
            return Wordle_multi().actions()
        elif len(self.user_word) != len(self.pc_word):
            print("Votre mot a une longueur différente de celle du mot choisi.\n")
            self.count -= 1
            return (self.actions())
        elif self.user_word.lower() not in self.l:
            print("Votre mot n'est pas dans le dictionnaire.\n")
            self.count -= 1
            return (self.actions())
        return self.essays_mots()
        
    def helping(self):
        self.help1 = ("\n"*100 + "BIENVENUE SUR "+ Fore.LIGHTGREEN_EX + 'MyWords !\n' + Fore.WHITE + "\n\nLe but du jeu est de trouver le mot auquel votre "+Fore.LIGHTBLUE_EX+"ami " + Fore.WHITE + "pense, et cela en "+Fore.LIGHTYELLOW_EX+ "6 "+Fore.WHITE+"coups maximum!\n\n"
                      "Lorsque vous insérez un mot (en fontion de la taille du mot que vous auriez choisie):\n"
                      "\t- Si une ou plusieurs lettres de votre mot se trouve(nt) au même endroit que dans celui de votre ami,\n elle(s) sera/seront de couleur "+Fore.LIGHTGREEN_EX+"VERTE "+Fore.WHITE+": [M] [A] [I] ["+Fore.LIGHTGREEN_EX+"S"+Fore.WHITE+"] [O] [N]\n"
                      "\t- Si une ou plusieurs lettres de votre mot se trouve(nt) dans le mot de votre ami mais pas au même endroit,\n elle(s) sera/seront de couleur "+Fore.LIGHTYELLOW_EX+"JAUNE "+Fore.WHITE+": [M] [A] [I] ["+Fore.LIGHTYELLOW_EX+"S"+Fore.WHITE+"] [O] [N]\n\n"
                      "Si vous décidez de donner votre langue au chat, l'ordinateur vous montrera le mot auquel il pensait, il suffit d'écrire exit !\n\n\n"
                      "Bonne chance !\n\n\n\n")
        print(self.help1)
        self.choix = str(input("Tapez "+Fore.LIGHTRED_EX+"fermer "+Fore.WHITE+"pour fermer l'aide\n--> ")).lower()
        if self.choix == "fermer":
            print("\n"*100)
            return self.choose_length()
        elif self.choix != "fermer":
            print(">:(")
            time.sleep(2)
            return self.helping()      
    
    def essays_mots(self):
        with open("essays.txt", "a") as file:
            file.write(self.user_word.upper()+"\n")
            file.close()
            self.show_answers()
            return self.check_lines()
            
    def check_lines(self):     
        with open("essays.txt", "r") as file:
            for line in file:
                if line != "\n":
                    if self.user_word.lower() == self.pc_word.lower():
                        return self.erase_lines()
                    elif self.count == 6:
                        file.close()
                        return self.erase_lines()
        file.close()
        return self.actions()
    
    def erase_lines(self):
        with open("essays.txt", "w") as file:
            file.truncate()
            if self.user_word.lower() != self.pc_word:
                print("\n" + Fore.LIGHTRED_EX + "Vous avez épuisé vos essais !\n"+Fore.WHITE)
                print("Le mot qu'il fallait trouver était " + Fore.LIGHTGREEN_EX + self.pc_word + Fore.WHITE + "!")
            elif self.user_word.lower() == self.pc_word.lower():
                print("Bravo, le mot qu'il fallait trouver était "+ Fore.LIGHTGREEN_EX + self.pc_word + Fore.WHITE + " et vous l'avez trouvé en " + Fore.LIGHTBLUE_EX + str(self.count) + Fore.WHITE + " coups !")
                time.sleep(5)
                return Wordle_multi().actions()
        time.sleep(5)
        return Wordle_multi().actions()
    
    def show_answers(self):
        with open("essays.txt", "r") as file:
            for line in file:
                answer = ""
                for i in range(len(line.split()[0])):
                    if line.split()[0][i] == self.pc_word.upper()[i]:
                        answer+=str(" ["+Fore.LIGHTGREEN_EX+line.split()[0][i]+Fore.WHITE+"] ")
                    elif line.split()[0][i] != self.pc_word.upper()[i] and line.split()[0][i] in self.pc_word.upper():
                        answer+=str(" ["+Fore.LIGHTYELLOW_EX+line.split()[0][i]+Fore.WHITE+"] ")
                    else:
                        answer+=str(" ["+line.split()[0][i]+"] ")
                print(answer+"\n")
                self.check_letters()
            print("Il vous reste ces lettres à utiliser: "+Fore.LIGHTBLUE_EX+str(self.liste)+Fore.WHITE+" !\n")
            if self.count == 5:
                print("Il vous reste "+Fore.LIGHTBLUE_EX+str(6-self.count)+Fore.WHITE+" essai.\n")
            else:
                print("Il vous reste "+Fore.LIGHTBLUE_EX+str(6-self.count)+Fore.WHITE+" essais.\n")
        file.close()
    
    def check_letters(self):
        for i in self.liste:
            if i in self.user_word:
                if i not in self.pc_word:
                    self.liste.remove(i)
        return self.show_answers
        
        
#Wordle_multi().actions()