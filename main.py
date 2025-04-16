
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    prompt = data.get("prompt", "")
    response = f"You said: {prompt} [Simulated AI response]"
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
