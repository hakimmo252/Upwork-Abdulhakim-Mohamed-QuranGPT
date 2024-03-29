from flask import Flask, request

from quran_chatgpt.helper.conversation import create_conversation
from quran_chatgpt.helper.twilio_api import send_message

qa = create_conversation()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return 'OK', 200

@app.route('/twilio', methods=['POST'])
def twilio():
    query = request.form['Body']
    sender_id = request.form['From']
    # TODO
    # get the user
    # if not create
    # create chat_history from the previous conversations

    res = qa(
        {
        'question': f'If outside of the given book please refer to the Quran in your answe. {query}',
        'chat_history': {}
        }
    )
    
    send_message(sender_id, res['answer'])

    return 'OK', 200

@app.route('/api/qa', methods=['POST'])
def api_qa():

    body = request.get_json()
    question = body['query']

    res = qa(
        {
        'question': question,
        'chat_history': {}
        }
    )

    return res, 200
