from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/message', methods=['GET'])
def hello_world():
    return {"message": "Hello, World!"}
