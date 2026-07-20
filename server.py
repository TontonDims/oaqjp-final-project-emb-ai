from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector") 
def emotion_detector(): 
# Récupérer le texte à analyser depuis les arguments de la requête 
text_to_analyze = request.args.get('textToAnalyze')

# Passer le texte à la fonction emotion_detector et stocker la réponse 
response = emotion_detector(text_to_analyze)

# Extraire l'étiquette et le score de la réponse 
emotion = response['emotion'] score = response['score']

# Retourner une chaîne formatée avec l'étiquette des émotions et les scores 
return "Pour l'énoncé donnée la réponse du système est  {} l'émotion dominante est {}.".format(emotion.split('_')[1], score)

@app.route("/")
def render_index_page():
     return render_template('index.html')


if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)