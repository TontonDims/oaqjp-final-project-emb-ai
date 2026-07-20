from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Cas de test pour emotion joy
        self.assertEqual(result_1['emotion'], 'joy')  
        result_1 = emotion_detector('I am glad this happened') 

        # Cas de test pour emotion anger
        self.assertEqual(result_2['emotion'], 'anger')  
        result_2 = emotion_detector('I am really mad about this') 

        # Cas de test pour emotion disgust
        self.assertEqual(result_2['emotion'], 'disgust') 
        result_3 = emotion_detector('I feel disgusted just hearing about this')  

        # Cas de test pour emotion sadness
        self.assertEqual(result_4['emotion'], 'sadness')
        result_4 = emotion_detector('I am so sad about this')  

        # Cas de test pour emotion fear
        self.assertEqual(result_5['emotion'], 'fear')  
        result_5 = emotion_detector('I am really afraid that this will happen') 

    unittest.main() 