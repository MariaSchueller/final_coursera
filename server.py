from flask import Flask, request, render_template
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
    response = emotion_detection(text_to_analyze)

    # Return the result as a string
    string_res = "".join([f"{k}: {v}, " for k,v in response.items() if k!= "dominant_emotion"])
    result = f"For the given statement, the system response is {string_res}"
    return result

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5000, debug=True)

