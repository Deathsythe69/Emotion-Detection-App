from flask import Flask, request, jsonify
from emotion_package import emotion_detector

app = Flask(__name__)

@app.route('/emotion', methods=['POST'])
def detect_emotion():
    text = request.json.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    result = emotion_detector(text)
    if result is None:
        return jsonify({"error": "Failed to analyze emotion"}), 500
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
