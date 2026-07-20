import requests # Importer la bibliothèque requests pour gérer les requêtes HTTP
import json

# Définir une fonction nommée emotion_detector qui prend une chaîne en entrée (text_to_analyse)
def emotion_detector(text_to_analyze):  
    # URL du service d'analyse de sentiment
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    
    # Créer un dictionnaire avec le texte à analyser
    myobj = { "raw_document": { "text": text_to_analyze } } 
    
    # Définir les en-têtes requis pour la requête API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} 
    
    # Envoyer une requête POST à l'API avec le texte et les en-têtes
    response = requests.post(url, json = myobj, headers=header)  
    
    # If the response status code is 200, extract the emotion and score from the response
    if response.status_code == 200:
        # Parsing the JSON response from the API 
        formatted_response = json.loads(response.text)
        emotion = formatted_response['emotionPredictions']
        score = formatted_response['emotionPredictions'][0]
    # If the response status code is 500, set emotion and score to None
    elif response.status_code == 500:
        # Extracting emotion and score from the response 
        emotion = None
        score = None
    # For any other unexpected status codes, set emotion and score to None
    else:
        emotion = None
        score = None
    
    # Return the response text from the API
    return {'emotion': emotion, 'score': score} 