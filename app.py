from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app) # Web-saytdan murojaat qilishga ruxsat beradi

# API Kalitni bu yerga yozing
genai.configure(api_key="SIZNING_YANGI_API_KALITINGIZ")

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        # Sizda ishlagan model nomini yozamiz
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(user_message)
        
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if name == '__main__':
    app.run(host='0.0.0.0', port=5000)
