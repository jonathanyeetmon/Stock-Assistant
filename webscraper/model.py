from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from torch.nn.functional import softmax

# Check if CUDA (GPU support) is available
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

# Print out the selected device
print("Using device:", device)

tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")

# Load the model and send it to the device (GPU or CPU)
model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert").to(device)

model.eval()

def get_financial_sentiment(text):
    # Encode the text using the tokenizer and move the tensor to the GPU
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512).to(device)
    
    # Perform the forward pass of the model and calculate probabilities
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        probabilities = softmax(logits, dim=1).flatten()
    
    # Since we are moving the data back to CPU for interpretation, we need to call `prob.item()`
    sentiment_mapping = {0: "positive", 1: "negative", 2: "neutral"}
    sentiment_probabilities = {sentiment_mapping[i]: prob.item() for i, prob in enumerate(probabilities.cpu())}
    
    return sentiment_probabilities

# Example usage
'''
text = "The company's revenue exceeded expectations for the last quarter."
sentiment_probabilities = get_financial_sentiment(text)
for sentiment, probability in sentiment_probabilities.items():
    print(f"Sentiment: {sentiment}, Probability: {probability:.4f}")
print(torch.cuda.is_available())
print(torch.cuda.device_count())
print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU found")
'''
