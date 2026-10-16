import requests

API_URL = "https://huggingface.co"
HEADERS = {"Authorization": "Bearer YOUR_HUGGING_FACE_API_KEY"}

def analyze_sentiment(text):
    payload = {"inputs": text}
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    
    if response.status_code == 200:
        predictions = response.json()[0]
        highest_prediction = max(predictions, key=lambda x: x['score'])
        
        label_mapping = {
            "LABEL_0": "negative",
            "LABEL_1": "neutral",
            "LABEL_2": "positive",
            "positive": "positive",
            "neutral": "neutral",
            "negative": "negative"
        }
        
        sentiment = label_mapping.get(highest_prediction['label'], highest_prediction['label'])
        confidence = highest_prediction['score']
        
        return sentiment, confidence
    else:
        return "error", 0.0

if __name__ == "__main__":
    sample_text = "I absolutely love learning how to use new AI tools!"
    sentiment, confidence = analyze_sentiment(sample_text)
    
    print(f"Text: {sample_text}")
    print(f"Sentiment: {sentiment}")
    print(f"Confidence: {confidence:.2f}")
