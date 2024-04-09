import torch 
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

# Hugging Face Model Selection
model_name = "deepset/roberta-base-squad2"  # Example model - Choose wisely!

# Download the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)


file_to_read = "scraped_text.txt"


# Read the text file
with open(file_to_read, 'r') as file:
    text = file.read()

# Ask a question (Replace with your own question)
question = "What is the main topic discussed in the text?"  

# Get the answer 
answer = model(question, text)  

print(answer) 