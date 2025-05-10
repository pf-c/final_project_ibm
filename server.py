from flask import Flask, jsonify, request, render_template
from emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector", methods=['POST'])
def emotion_detector_api():
    text_to_analyze = request.json.get('textToAnalyze', '')
    if not text_to_analyze:
        return jsonify({
            'status': 'error',
            'message': 'Invalid input. Please provide text for analysis.'
        }), 400

    response = emotion_detector(text_to_analyze)
    if response and 'dominant_emotion' in response:
        anger_score = response.get('anger', 0)
        disgust_score = response.get('disgust', 0)
        fear_score = response.get('fear', 0)
        joy_score = response.get('joy', 0)
        sadness_score = response.get('sadness', 0)
        dominant_emotion = response.get('dominant_emotion', '')

        response_data = {
              f"For the given statement, the system response is "
            f"'anger': {anger_score}, 'disgust': {disgust_score}, "
            f"'fear': {fear_score}, 'joy': {joy_score} and "
            f"'sadness': {sadness_score}. The dominant emotion is "
            f"**{dominant_emotion}**."
        }
        return jsonify(response_data), 200
    else:
        return jsonify({
           'status': 'error',
           'message': 'Failed to analyze emotions.'
        }), 500

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=False)