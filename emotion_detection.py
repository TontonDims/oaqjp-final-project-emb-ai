import requests # Importer la bibliothèque requests pour gérer les requêtes HTTP
            
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
    
    # Retourner le texte de la réponse de l'API
    return response.text 