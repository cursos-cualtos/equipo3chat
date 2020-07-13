from flask import Flask
import json

app = Flask(__name__)

@app.route('/auth/<user>')
def index(user):
    usuarios = ["Héctor", "Emmanuel"]

    if user in usuarios:
        message = {'status':'authorized'}
    else:
        message = {'status':'unauthorized'}

    return json.dumps(message)

if __name__ == "__main__":
    app.run(port=5000)
