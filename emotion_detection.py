import requests,json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    return emotions

    # return response.text
    # return formatted_response
    # dominant_emotion = max(emotions, key=emotions.get)
    # return dominant_emotion
    # # return f'Donimant Emotion: {dominant_emotion}'


# '{"emotionPredictions":
# [{"emotion":
#         {"anger":0.01364663, "disgust":0.0017160787, "fear":0.008986978, "joy":0.9719017, "sadness":0.055187024}, 
#         "target":"", 
#         "emotionMentions":[{"span":{"begin":0, "end":27, "text":"I love this new technology."}, 
# "emotion":{"anger":0.01364663, "disgust":0.0017160787, "fear":0.008986978, "joy":0.9719017, "sadness":0.055187024}}]}], 
#         "producerId":{"name":"Ensemble Aggregated Emotion Workflow", "version":"0.0.1"}}'



# URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
# Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
# Input json: { "raw_document": { "text": text_to_analyse } }

# def sentiment_analyzer(text_to_analyse):
#     url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
#     myobj = { "raw_document": { "text": text_to_analyse } }
#     header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
#     response = requests.post(url, json = myobj, headers=header)

#     return response.text
