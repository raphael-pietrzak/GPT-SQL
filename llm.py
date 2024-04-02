
from gpt4all import GPT4All

class Llm:
    def __init__(self):
        # model
        self.model = GPT4All('mistral-7b-instruct-v0.1.Q4_0.gguf')
        # story
        self.path = 'stories/story2.txt'
        self.story = open(self.path, 'r').read()

        self.columns = ['verbs']



    def generate(self):
        prompt = f"Réponds moi uniquement par [oui] ou [non]. Est ce que cette histoire contient des {self.columns[0]} ? \n HISTOIRE : {self.story}\n"
        output = self.model.generate(prompt)
        return output
