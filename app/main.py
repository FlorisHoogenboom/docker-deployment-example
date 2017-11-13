from flask import Flask
from flask import request, make_response, abort, session, json
from sklearn.externals import joblib
import pandas as pd


app = Flask(__name__)
model = joblib.load('/app/model/model')

@app.route("/")
def hello():
    return "Hello World from Flask"

@app.route("/predict", methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame.from_dict(data)
    data['target'] = list(model.predict(df))
    return make_response(json.jsonify(data), 200)