#-*- coding: UTF-8 -*-

from colorama import Fore, Back, Style
import codecs
import random
import time
import os
import choix
os.system('cls')

class Wordle:
    
    def __init__(self):
        self.count = 0
        self.liste = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.l = []
        self.choose_length()
        self.pc_word = random.choice(self.words())
        with open("essays.txt", "w") as file:
            file.truncate()
            file.close()
        self.actions()
        
    def words(self):
        with codecs.open('liste_francais.txt', 'r') as file:
            for line in file:
                if len(line) == int(self.nr)+1:
                    self.l+=line.lower().split()
        file.close()
        return self.l
    
    def choose_length(self):
        self.number = str(input("\n"*100+"Choisissez la " + Fore.YELLOW+ "longueur" +Fore.WHITE+ " du mot que vous voulez trouver" + Fore.LIGHTRED_EX+ " (minimum taille 2 et maximum taille 15)"+Fore.WHITE+", tapez "+Fore.YELLOW+ 'help'+Fore.WHITE +" pour savoir comment jouer, tapez "+Fore.YELLOW+ 'fermer' +Fore.WHITE+" pour fermer le programme ou tapez "+Fore.YELLOW+ 'menu' +Fore.WHITE+" pour revenir à l'accueil: \n --> "))
        self.nr = ''
        if self.number.lower() == "help":
            return self.helping()
        elif self.number.lower() == "fermer":
            exit()
        elif self.number.lower() == "menu":
            print("\n"*20)
            return choix.Choix()
        else:
            for i in range(len(self.number)):
                if self.number[i] in "0123456789":
                    self.nr += self.number[i]
                else:
                    print("Veuillez entrer un nombre entier ou taper 'help' ou 'fermer' !\n")
                    return (self.choose_length())
        if int(self.nr) < 2:
            print("Le mot doit contenir au moins 2 lettres !")
            return self.choose_length()
        elif int(self.nr) > 15:
            print("Choisissez une taille inférieure ou égale à 15 !\n\n")
            return self.choose_length()
        return self.nr
                
    def actions(self):
        self.user_word = input("\nChoisissez un mot de taille "+Fore.LIGHTBLUE_EX+str(len(self.pc_word))+Fore.WHITE+" (si vous voulez abandonner, tapez" + Fore.YELLOW + " exit" + Fore.WHITE + "):\n-->  ")
        self.count += 1
        if self.user_word == "exit":
            print("\nLe mot qu'il fallait trouver était "+Fore.LIGHTGREEN_EX+self.pc_word+Fore.WHITE+ " !\n"
                  "Attendez 5 secondes s'il vous plaît\n")
            time.sleep(5)
            with open("essays.txt", "w") as file:
                file.truncate()
                file.close
            return Wordle().actions()
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
        self.help1 = ("\n"*100 + "BIENVENUE SUR "+ Fore.LIGHTGREEN_EX + 'MyWords !\n' + Fore.WHITE + "\n\nLe but du jeu est de trouver le mot auquel l'"+Fore.LIGHTBLUE_EX+"ordinateur " + Fore.WHITE + "pense, et cela en "+Fore.LIGHTYELLOW_EX+ "6 "+Fore.WHITE+"coups maximum!\n\n"
                      "Lorsque vous insérez un mot (en fontion de la taille du mot que vous auriez choisie):\n"
                      "\t- Si une ou plusieurs lettres de votre mot se trouve(nt) au même endroit que dans celui de l'ordinateur,\n elle(s) sera/seront de couleur "+Fore.LIGHTGREEN_EX+"VERTE "+Fore.WHITE+": [M] [A] [I] ["+Fore.LIGHTGREEN_EX+"S"+Fore.WHITE+"] [O] [N]\n"
                      "\t- Si une ou plusieurs lettres de votre mot se trouve(nt) dans le mot de l'ordinateur mais pas au même endroit,\n elle(s) sera/seront de couleur "+Fore.LIGHTYELLOW_EX+"JAUNE "+Fore.WHITE+": [M] [A] [I] ["+Fore.LIGHTYELLOW_EX+"S"+Fore.WHITE+"] [O] [N]\n\n"
                      "Si vous décidez de donner votre langue au chat, l'ordinateur vous montrera le mot auquel il pensait, il suffit d'écrire exit !\n\n\n"
                      "Bonne chance !\n\n\n\n")
        print(self.help1)
        choix = str(input("Tapez "+Fore.LIGHTRED_EX+"fermer "+Fore.WHITE+"pour fermer l'aide\n--> ")).lower()
        if choix == "fermer":
            print("\n"*100)
            return self.choose_length()
        elif choix != "fermer":
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
                return Wordle().actions()
        time.sleep(5)
        return Wordle().actions()
    
    def show_answers(self):
        with open("essays.txt", "r") as file: # content = file.readlines()
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
        for i in self.user_word.lower():
            if i not in self.pc_word and i in self.liste:
                del self.liste[self.liste.index(i)]
        return self.show_answers