
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
    
    result = ', '.join(f"'{key}': {value}" for key, value in response.items())
    return "For the given statement, the system response is {}. <br> The dominant emotion is {}.".format(result, max(response, key = response.get))
    # TODO


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')
    #TODO

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''#TODO
    app.run(host="0.0.0.0", port=5000)

# def sent_analyzer():
#     text_to_analyze = request.args.get('textToAnalyze')
#     response = sentiment_analyzer(text_to_analyze)
#     label = response['label']
#     score = response['score']
#     if label is None:
#         return "Invalid input ! Try again."
#     else:
#         return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)

