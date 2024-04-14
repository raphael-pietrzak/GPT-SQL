import json
from jsonschema import validate, Draft7Validator

# Function to generate a dynamic JSON schema
def generate_schema(prompt_attributes):
    # If no attributes are specified, return an empty schema
    if not prompt_attributes:
        return {}
    
    # Create properties for each attribute with their respective domains
    properties = {}
    for attribute, domain in prompt_attributes.items():
        if domain == "str":
            properties[attribute] = {"type": "string"}
        elif domain == "int":
            properties[attribute] = {"type": "integer"}
        elif domain == "list":
            properties[attribute] = {"type": "array"}
        elif domain == "range":
            properties[attribute] = {"type": "object", "properties": {"start": {"type": "integer"}, "end": {"type": "integer"}}}
        elif domain == "bool":
            properties[attribute] = {"type": "boolean"}
    
    # Construct the schema
    schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": properties
        }
    }
    
    return schema

# Function to verify JSON format and attributes using jsonschema
def verify_json(json_data, prompt_attributes):
    try:
        schema = generate_schema(prompt_attributes)
        print("Generated JSON Schema:")
        print(json.dumps(schema, indent=4))  # Print the schema with indentation for better readability
        print("\nVerifying JSON format and attributes...")
        validate(instance=json.loads(json_data), schema=schema, cls=Draft7Validator)
        print("JSON format and attributes are as expected.")
        return True
    except Exception as e:
        print(f"JSON verification error: {e}")
        return False

# Example usage
json_data = '''
[
    {"nom": "John", "age": 30, "liste": [1, 2, 3], "plage": {"start": 1, "end": 5}, "est_majeur": true},
    {"nom": "Alice", "age": 25, "liste": [4, 5, 6], "plage": {"start": 2, "end": 7}, "est_majeur": false}
]
'''
# Attributes specified by the user (example)
prompt_attributes = {
    "nom": "str",
    "age": "int",
    "liste": "list",
    "plage": "range",
    "est_majeur": "bool"
}

# Verify JSON format and attributes
verify_json(json_data, prompt_attributes)

#if verify_json(json_data, prompt_attributes):
      # If the verification is successful, converts the Json into Db with the JsonToDb class
    
#else:
    # If the verification fails, re-run the llm with the Llm class
   