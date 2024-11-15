from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Hugging Face API endpoint for the BART model
HF_API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
HF_API_KEY = "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"  # Replace with your Hugging Face API key

def query_huggingface_api(text):
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": text}
    response = requests.post(HF_API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()[0]['summary_text']
    else:
        return "Error: Unable to summarize text."

@app.route('/summarize', methods=['POST'])
def summarize():
    text = request.json.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    summary = query_huggingface_api(text)
    return jsonify({"summary": summary})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
