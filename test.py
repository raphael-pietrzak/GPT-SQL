from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Chargement du modèle et du tokenizer
model_path = "/models/ggml-model-q4_0.bin" 
tokenizer = GPT2Tokenizer.from_pretrained(model_path)
model = GPT2LMHeadModel.from_pretrained(model_path)

# Définition du prompt
prompt = "Votre prompt ici."

# Encodage du prompt
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# Génération de la réponse
output = model.generate(input_ids, max_length=50, num_return_sequences=1, temperature=0.7)

# Décodage de la réponse
response = tokenizer.decode(output[0], skip_special_tokens=True)

print("Réponse générée:", response)
