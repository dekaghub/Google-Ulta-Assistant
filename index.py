 # /index.py

from flask import Flask, request, jsonify, render_template
#/from flask_pusher import Pusher
import os
import dialogflow
import requests
import json


GOOGLE_APPLICATION_CREDENTIALS=os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_movie_detail', methods=['POST'])
def get_movie_detail():
    data = request.get_json(silent=True)
    movie = data['queryResult']['parameters']['makeup']
    api_key = os.getenv('ULTA_API_KEY')

    movie_detail = requests.get('http://www.omdbapi.com/?t={0}&apikey={1}'.format(movie, api_key)).content
    movie_detail = json.loads(movie_detail)
    response =  """
        Title : {0}
        Released: {1}
        Actors: {2}
        Plot: {3}
        """.format(makeup_detail['Title'], makeup_detail['Released'], makeup_detail['Actors'], makeup_detail['Plot'])

    reply = {
            "fulfillmentText": response,
        }
    return jsonify(reply)

    def detect_intent_texts(project_id, session_id, text, language_code):
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(project_id, session_id)

        if text:
            text_input = dialogflow.types.TextInput(
                text=text, language_code=language_code)
            query_input = dialogflow.types.QueryInput(text=text_input)
            response = session_client.detect_intent(
                session=session, query_input=query_input)

            return response.query_result.fulfillment_text

    @app.route('/send_message', methods=['POST'])
    def send_message():
        message = request.form['message']
        project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
        fulfillment_text = detect_intent_texts(project_id, "unique", message, 'en')
        response_text = { "message":  fulfillment_text }
        pusher_client.trigger(
        'ulta-bot', 
        'new_message', 
        {
            'human_message': message, 
            'bot_message': fulfillment_text,
        },
        socketId
    )
        return jsonify(response_text)

    def audio_int(num_samples=50):
        """ Gets average audio intensity of your mic sound. You can use it to get
        average intensities while you're talking and/or silent. The average
        is the avg of the 20% largest intensities recorded.
        """
        
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    values = [math.sqrt(abs(audioop.avg(stream.read(CHUNK), 4))) 
              for x in range(num_samples)] 
    values = sorted(values, reverse=True)
    r = sum(values[:int(num_samples * 0.2)]) / int(num_samples * 0.2)
    print(" Average audio intensity is ", r)
    stream.close()
    p.terminate()
    
    if r > THRESHOLD:
        listen(0)
    
    threading.Timer(SILENCE_LIMIT, audio_int).start()  


    def listen(x):
        r=rs.Recognizer()
    if x == 0:
        system('say Hi. How can I help?')
    with rs.Microphone() as source:
        audio=r.listen(source)
    try:
        text = r.recognize_google(audio)
        y = process(text.lower())
        return(y)
    except:
        if x == 1:
            system('say Good Bye!')
        else:
            system('say I did not get that. Please say again.')
            listen(1) 

    def process(text):
        """ Gets average audio intensity of your mic sound. You can use it to get
        average intensities while you're talking and/or silent. The average
        is the avg of the 20% largest intensities recorded.
        """
    # run Flask app
if __name__ == "__main__":
    app.run()