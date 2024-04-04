from text import Text

class Main:
    def __init__(self):
        self.text = Text()

    def run(self):

        # Text extraction & verification testing
        path = ""
        self.text.initialize(path)
        print(self.text.content)


if __name__ == '__main__':
    main = Main()
    main.run()
