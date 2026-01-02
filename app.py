import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from google import genai

app = Flask(__name__)
# CORS ni barcha uchun ruxsat berilgan holatda sozlaymiz
CORS(app, resources={r"/*": {"origins": "*"}})

# API kalitini tekshirish
API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyDT1c3VPNBG--Su05uyZqo6oWOG58Xs-lI")

client = genai.Client(api_key=API_KEY)

@app.route('/chat', methods=['POST', 'OPTIONS'])
def chat():
    # OPTIONS so'rovi (Preflight) uchun javob berish
    if request.method == 'OPTIONS':
        return '', 204
        
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({"reply": "Xabar yozilmadi"}), 400
        
        # Model nomini tekshiring: sizda "gemini-2.0-flash" ishlagan
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=user_message
        )
        
        # Javobni qaytarishda aniq .text maydonidan foydalanamiz
        return jsonify({"reply": response.text})
        
    except Exception as e:
        print(f"Server xatosi: {str(e)}")
        return jsonify({"error": str(e), "reply": "Serverda xatolik yuz berdi"}), 500

if name == '__main__':
    app.run(host='0.0.0.0', port=5000)
