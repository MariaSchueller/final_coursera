import requests
import json

def emotion_detection(text_to_analyse):
    # Set up API endpoint and headers
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Prepare the request payload
    my_obj = {"raw_document": {"text": text_to_analyse}}

    # Send POST request to the Watson NLP API
    response = requests.post(url, json=my_obj, headers=headers)

    # Parse the response JSON
    formatted_response = json.loads(response.text)

    # Extract emotion scores
    emo = formatted_response["emotionPredictions"][0]["emotion"]

    # Find and add the dominant emotion
    dominant_emotion = max(emo, key=emo.get)
    emo["dominant_emotion"] = dominant_emotion

    return emo  # Return full emotion dictionary with dominant emotion added
