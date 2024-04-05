LENGTH_NAME = 25

POSSIBLE_VALUES = [str, int, list, range, bool]

class RelationScheme :


    def __init__(self):
        self.name = ""
        self.attributes = {}
        self.max_length_name = LENGTH_NAME #To be adjusted
    

           
    # Function to set name if it's in correct format
    def set_name(self, name):
    
        if(self.verify_name(name) == True):
            self.name = str(name)
            return True
        else:
            return False



    # Function to verify name format
    def verify_name(self, name):
    
        # verify if the name is not out of length
        if(len(name)>self.max_length_name):
            print(f"[ERROR] : name {name} out of limit, please check max_length_name")
            return False
    
        # verify if the name is compatible with str casting
        try:
            str(name)
        except:
            print(f"[ERROR] : name {name} is not in an accepted format")
            return False

        return True
    


    # Function to set max length of a name
    def set_max_length_name(self, max_length_name):
        try:
            self.max_length_name = int(max_length_name)
            return True
        except:
            print(f"[ERROR] : provided max_length_name {max_length_name} isn't a int type")
            return False
    


    # Function to insert attribute in dictionnary
    def insert_attribute(self, name, dom):

        if(self.verify_name(name) == True):
            
            # Inserting domain value(s) in dictionnary by selecting the type
            if(type(dom) in POSSIBLE_VALUES or dom == None):
                if not(name in self.attributes):
                    self.attributes[name] = dom
                    return True
                else:
                    print(f"[ERROR] : specified attribute {name} is already existing")
                    return False
            else:
                print(f"[ERROR] : specified dom {dom} is not in an accepted type")
                return False
        
        #if name not valided
        return False



    # Function to erase attribute
    def erase_attribute(self, key):

        if(key in self.attributes):
            del self.attributes[key]
            return True
        else:
            print(f"[INFO] : specified key {key} is not an attribute of {self.name}")
            return False
    
