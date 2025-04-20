from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detection  # Make sure this import works

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():
    # Get text from the query parameter
    text_to_analyze = request.args.get("textToAnalyze")

    # If no text is provided, return a helpful message
    if not text_to_analyze:
        return "Please provide text using the 'textToAnalyze' query parameter.", 400

    # Run the emotion detection
    result = emotion_detection(text_to_analyze)

    # Return the result as a string
    return f"The detected dominant emotion is: {result['dominant_emotion']}"

if __name__ == "__main__":
    app.run(debug=True)