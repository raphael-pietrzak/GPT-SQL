
from llm import Llm

class Main:
    def __init__(self):
        self.llm = Llm()

    def run(self):
        output = self.llm.generate()
        print(output)
        


if __name__ == '__main__':
    main = Main()
    main.run()