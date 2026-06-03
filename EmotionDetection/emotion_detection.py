# Import the requests library to handle HTTP requests
import requests
import json

# Define a function named emotion_detector that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyze):

    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)

    # Parsing the JSON response from the API 
    formatted_response = json.loads(response.text)

    # Extracting emotions and score from the response
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    # Extracting the score for each emotion
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Finding the dominant emmotion
    dominant_emotion = max(emotions, key=emotions.get)
    dominant_score = emotions[dominant_emotion]

    #Return the output of the emotion_detecor function
    output = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear':fear_score,
        'joy':joy_score,
        'sadness':sadness_score,
        'dominant_emotion':dominant_emotion
    }

    return output
    