import json
import time
import Other.choix as ch
import os.path

class Stats:
    def __init__(self):
        self.file = os.path.realpath("Other/stats.json")
        self.lis = []
    
    def load_stat_content(self):
        with open(self.file, "r") as f:
            return json.load(f)
    
    def write_stat_content(self, stat_dic):
        with open(self.file, "w") as f:
            json.dump(stat_dic, f, indent=4)
        
    def write_stat(self, name, total_win, total_losses, total_games, total_attempts, win_rate):
        content = self.load_stat_content()
        if name in content:
            data = content[name]
            data["Total Number of Win"] += total_win
            data["Total Number of Losses"] += total_losses
            data["Total Number of Games"] += total_games
            data["Total Number of Attempts"] += total_attempts
            if data["Total Number of Losses"] == 0:
                data["Win Rate"] = 100
            else:
                data["Win Rate"] = round((data["Total Number of Win"]/data["Total Number of Games"])*100, 2)
        else:
            new_data = {
                "Total Number of Win": total_win,
                "Total Number of Losses": total_losses,
                "Total Number of Games": total_games,
                "Total Number of Attempts": total_attempts,
                "Win Rate": win_rate,
            }
            data = new_data
        content[name] = data

        self.write_stat_content(content)
    
    def show_stats(self):
        self.content = self.load_stat_content()
        if self.content == {}:
            print("Jouez une partie pour pouvoir afficher les statistiques!")
            time.sleep(3)
            return ch.Choix()
        else:
            stri = ""
            for player, data in self.content.items():
                stri+= "\n"*10+"Nom d'utilisateur: "+player.upper()+"\t\tParties gagnées: "+str(data["Total Number of Win"])+"\n\nParties perdues: "+str(data["Total Number of Losses"])+"\t\tNombre Total de Parties: "+str(data["Total Number of Games"])+"\n\nNombre Total d'essais: "+str(data["Total Number of Attempts"])+"\tTaux de Matchs gagnés: "+str(data["Win Rate"])+"%\n\n----------------------------------------------------------------------\n\n"
            print(stri)
            input("Tapez sur la touche 'Enter' pour revenir au menu\n>> ")
            return ch.Choix()
    
    def choose_name(self):
        self.content = self.load_stat_content()
        if self.content == {}:
            print("La base de données est vide! Jouez une partie pour la remplir")
            time.sleep(3)
            return ch.Choix()
        else:
            self.name_choice = str(input("\n"*20+"Ecrivez un nom d'utilisateur que vous voudriez effacer \nQuand vous aurez fini, tapez sur la touche Enter\n\n>> "))
            while self.name_choice != "":
                self.lis.append(self.name_choice.lower())
                self.choose_name()
            self.delete_stat()
    
    def delete_stat(self):
        for i in range(len(self.lis)):
            if self.lis[i] in self.content:
                self.content.pop(self.lis[i])
                self.write_stat_content(self.content)
                print("\n\n"+self.lis[i]+" effacé")
                time.sleep(1)
            else:
                print("\n\n"+self.lis[i]+" n'a pas encore joué de parties")
                time.sleep(1)
        print("\n\n\nOK")
        time.sleep(3)
        print("\n"*30)
        return ch.Choix()