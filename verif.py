import json

class Verif:
    def __init__(self, question, reponse):
        self.question = question
        self.reponse = reponse

    def imprimer_resultat_generate(self):
        print("voici ce que vous avez demandé:", self.question)
        print("et voici le résultat:", self.reponse)

    def veirf_Json(self):
        try:
            pass
        except:
            print("Ce n'est pas un objet JSON")