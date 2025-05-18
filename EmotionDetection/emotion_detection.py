import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyze):  # Define a function named emotion_detector that takes a string input (text_to_analyze)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the emotion predict service
    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers

    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotion = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion, key=emotion.get)
        return {
            'anger': emotion['anger'],
            'disgust': emotion['disgust'],
            'fear': emotion['fear'],
            'joy': emotion['joy'],
            'sadness': emotion['sadness'],
            'dominant_emotion': dominant_emotion
        }
    elif response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }