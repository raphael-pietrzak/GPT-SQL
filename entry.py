import json
import os

CONTENT_LENGTH = 200
NAME_LENGTH = 25
PATH = "user_inputs.json"

class Entry:

    def __init__(self):
        self.content = ""
        self.relation_scheme_name = ""
        self.relation_scheme_content = {}
        if(os.path.getsize(PATH) > 1):
            self.loads()
    
    def saves(self):
        inputs = {
            "entries" : [
                {
                "entry_content" : str(self.content),
                "entry_relation_scheme_name" : str(self.relation_scheme_name)
                },
                {}
            ]}
        inputs["entries"][1].update(self.relation_scheme_content)
        inputs_string = json.dumps(inputs, indent=1)
        with open(PATH, 'w') as file:
            file.write(inputs_string)

    def loads(self):
        with open(PATH, "r") as file:
            json_content = json.loads(file.read())
        if("entry_content" in json_content["entries"][0]):
            self.content = json_content["entries"][0]["entry_content"]
        if("entry_relation_scheme_name" in json_content["entries"][0]):
            self.relation_scheme_name = json_content["entries"][0]["entry_relation_scheme_name"]
        if(json_content["entries"][1] != {}):
            self.relation_scheme_content = json_content["entries"][1]


    def set_content(self, content):
        if(self.check_content(content)):
            self.content = content
            return True
        return False

    def check_content(self, content):
        if(len(content) > CONTENT_LENGTH):
            return False
        return True
    
    def set_relation_scheme_name(self, name):
        if(self.check_name(name)):
            self.relation_scheme_name = name
            return True
        return False

    def check_name(self, name):
        if(len(name)>NAME_LENGTH):
            return False
        if(name == "entry_content"):
            return False
        if(name == "entry_relation_scheme_name"):
            return False
        if(name == "entry_relation_scheme_content"):
            return False
        return True
    
    def check_type_att(self, type_att):
        if(type_att == "str"):
            return True
        if(type_att == "int"):
            return True
        if(type_att == "list"):
            return True
        if(type_att == "range"):
            return True
        if(type == "None"):
            return True
        return False

    def add_attribute(self, name, type_att):
        if(name in self.relation_scheme_content):
            return False
        if(self.check_name(name) and self.check_type_add):
            self.relation_scheme_content[name] = type_att
            return True
        return False
       
    def delete_attribute(self, name):
        if(name in self.relation_scheme_content):
            del self.relation_scheme_content[name]
            return True
        return False

entry = Entry()
