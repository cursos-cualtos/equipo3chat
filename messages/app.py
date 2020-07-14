from flask import Flask
from markupsafe import escape
from data import messages
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

if __name__ == "__main__":
    app.run(port=5002)
