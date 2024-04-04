import os


LENGTH = 200


class Text:
    
    # INIT
    def __init__(self):

        self.path = None
        self.content = ""
        self.max_length = LENGTH # To be adjusted

    
    # Function to initialize a text file
    def initialize(self,path):
        self.set_path(path)
        self.set_content()
        return(True)



    # Function to set the path
    def set_path(self, path):
        if(self.verify_path(path) == True):
            self.path = str(path)
            print(f"[INFO] : selected path is {self.path}")
            return(True)
        else:
            return(False)


    # Function to verify path format
    def verify_path(self, path):

        # verify if extension is txt
        if(path == None or path == ""):
            print("[ERROR] : path is empty")
            return(False)
        
        # verify if path is a str
        if(type(path) != str):
            print("[ERROR] : specified path is not an str")
            return(False)
        
        # verify if path is an txt file
        if(path[len(path)-4:len(path)] != ".txt"):
            print(path[len(path)-4:len(path)])
            print("[ERROR] : specified document is not a txt file")
            return(False)
        
        # if path in correct format
        return(True)
    


    # Function to set a new max length to content
    def set_max_length(self, length):
        
        if(length >= 0):
            try:
                self.max_length = int(length)
            except:
                print("[ERROR] : specified length is not an int type")
                return(False)
        else:
            print("[ERROR] : length can't be a negative")
            return(False)
        
        return(True)
    


    # Function to extract text from specified file in path
    def set_content(self):
        
        try:
            print(self.path)
            file = open(os.path.expanduser(self.path), "r")
            content = file.read()
            file.close()
        except:
            print("[ERROR] : Cannot find specified file, please verify the path")
            return(False)
        
        if(self.verify_content(content) == True):
            self.content = content
            return(True)
        else:
            return(False)


    # Function to verify extracted text
    def verify_content(self, content):
        
        # verify if content is not empty
        if(content == None or content == ""):
            print("[ERROR] : specified content is empty")
            return(False)
        
        # verify if content is in the max_length limit
        if(len(content)>self.max_length):
            print("[ERROR] : specified content length is out of limit, please verify max_length")
            return(False)
        
        # if content is in the correct format  
        return(True)