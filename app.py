from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}"

@app.route('/set_score', methods=['POST'])
def set_score():
    data = request.json
    user_id = data.get("user_id")
    score = data.get("score")
    message_id = data.get("message_id")
    chat_id = data.get("chat_id")

    if not all([user_id, score, message_id, chat_id]):
        return jsonify({"error": "Missing data"}), 400

    payload = {
        "user_id": user_id,
        "score": score,
        "chat_id": chat_id,
        "message_id": message_id,
        "force": True
    }

    response = requests.post(f"{TELEGRAM_API}/setGameScore", json=payload)
    return jsonify(response.json())

@app.route('/get_scores', methods=['GET'])
def get_scores():
    chat_id = request.args.get("chat_id")
    message_id = request.args.get("message_id")
    if not chat_id or not message_id:
        return jsonify({"error": "Missing params"}), 400

    response = requests.get(f"{TELEGRAM_API}/getGameHighScores", params={
        "chat_id": chat_id,
        "message_id": message_id
    })
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
