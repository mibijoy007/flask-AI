
from flask import Flask,render_template,request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app 
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the label and its dominant emotion 
         for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    return '''For the given statement, the system response is {response} 
    The dominant emotion is {max(response, key=response.get)}'''
    # return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)
    # TODO

# def sent_analyzer():
#     text_to_analyze = request.args.get('textToAnalyze')
#     response = sentiment_analyzer(text_to_analyze)
#     label = response['label']
#     score = response['score']
#     if label is None:
#         return "Invalid input ! Try again."
#     else:
#         return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)

