from flask import Flask
from markupsafe import escape
from flask import request
from data import messages
from db_utils import add_message
import json
import db_utils

app = Flask(__name__)

@app.route('/messages')
def index():
    # result = 
    return json.dumps(db_utils.get_all_messages(), default=str)

@app.route('/messages/<int:message_id>', methods=["GET"])
def greeting(message_id):
    message = {'message': 'Hello user'}
    print(message_id)
    return json.dumps(messages[message_id])

@app.route('/messages/add', methods=["POST"])
def messages_add():
    print(request.json)
    add_message(request.json)
    return json.dumps({})

if __name__ == "__main__":
    app.run(port=5002)
