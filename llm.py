
from gpt4all import GPT4All

class Llm:
    def __init__(self):
        # model
        # self.model = GPT4All('orca-mini-3b-gguf2-q4_0.gguf')
        self.model = GPT4All('mistral-7b-instruct-v0.1.Q4_0.gguf')
        # story
        self.path = 'stories/story2.txt'
        self.story = open(self.path, 'r').read()

        self.columns = ['verbes']



    def generate(self):
        # prompt = f"Formatte moi sous format json l'histoire suivante : \n HISTOIRE : {self.story}\n avec comme paramètre de recherche les {self.columns[0]}\n"
        # prompt = f"Réponds moi uniquement par [oui] ou [non]. Est ce que cette histoire : '{self.story}' contient le mot 'prairie' ?"
        prompt = """Tâche : Créez une sortie json à partir d'une histoire en entrée et renvoie les verbes présents sous forme de liste JSON.

        Entrée : Il était une fois un chevalier qui courait dans la prairie.

        Sortie : Une liste JSON des verbes extraits de l'histoire.

        Instructions : Traitez l'entrée pour extraire les verbes et retournez-les en tant que liste JSON sans doublons, ordonnée alphabétiquement.

        Exemple :

        Entrée : 'Jean marchait lentement vers la rivière.'

        Sortie : {'verbes': ['marchait']}"""


        output = self.model.generate(prompt, max_tokens=100)
        return output

