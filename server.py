''' Executing this function initiates the application of emotion detector
    to be executed over the Flask channel and deployed on localhost:5000.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask(__name__)
@app.route("/emotionDetector")
def emotion_detect():
    """
    Detects the emotion of a given text.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)
    if result is None:
        return " Invalid text! Please try again!."
    anger_score = result['anger']
    disgust_score = result ['disgust']
    fear_score = result['fear']
    joy_score = result['joy']
    sadness_score = result['sadness']
    dominant_emotion = result['dominant_emotion']
    response_text = (
    f"For the given statement, the system response is 'anger': {anger_score}, "
    f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score}, "
    f"and 'sadness': {sadness_score}. The dominant emotion is <b>{dominant_emotion}</b>"
    )
    return response_text
@app.route("/")
def render_index_page():
    """
    Renders the index page.
    """
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)
