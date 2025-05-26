
from flask import Flask, request, jsonify
from collections import defaultdict

app = Flask(__name__)
scores = defaultdict(int)

@app.route('/submit', methods=['POST'])
def submit_score():
    data = request.json
    user = data.get('user')
    score = data.get('score', 0)
    scores[user] = max(scores[user], score)
    return jsonify(success=True)

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return jsonify(leaderboard=sorted_scores[:10])

if __name__ == '__main__':
    app.run(debug=True)
