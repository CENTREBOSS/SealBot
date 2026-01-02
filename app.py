import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai

app = Flask(__name__)
CORS(app)

# API kalitini xavfsizlik uchun Render Environment Variables-dan oladi
# Agar u yerga qo'ymagan bo'lsangiz, vaqtincha qo'shtirnoq ichiga yozing
API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyDT1c3VPNBG--Su05uyZqo6oWOG58Xs-lI")

client = genai.Client(api_key=API_KEY)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        # Sizda ishlagan model nomini yozamiz
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=user_message
        )
        
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DIQQAT: Pastdagi qatorga e'tibor bering, ikkita pastki chiziq bo'lishi shart!
if name == '__main__':
    app.run(host='0.0.0.0', port=5000)
