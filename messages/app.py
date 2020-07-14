from flask import Flask
from markupsafe import escape
from data import messages
from db_utils import add_message
import json

app = Flask(__name__)

@app.route('/messages')
def index():
    return json.dumps(messages)

@app.route('/messages/<int:message_id>', methods=["GET"])
def greeting(message_id):
    message = {'message': 'Hello user'}
    print(message_id)
    return json.dumps(messages[message_id])

@app.route('/messages/add')
def messages_add():
    add_message()

if __name__ == "__main__":
    app.run(port=5002)
