# emotion_detector.py
import json
from ibm_watson import Natural LanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions

authenticator = IAMAuthenticator("YOUR_API_KEY")
nlu = Natural LanguageUnderstandingV1(
    version='2021-08-01',
    authenticator=authenticator
)
nlu.set_service_url("YOUR_SERVICE_URL")

def emotion_predictor(text_to_analyze):
    try:
        response = nlu.analyze(
            text=text_to_analyze,
            features=Features(emotion=EmotionOptions())
        ).get_result()

        emotions = response['emotion']['document']['emotion']
        dominant_emotion = max(emotions, key=emotions.get)

        return {
            "emotion": emotions,
            "dominant_emotion": dominant_emotion
        }
    except:
        return None

