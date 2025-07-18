import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
# import Ridge Regressor and standard scaler
ridge_model=pickle.load(open('models/ridge.pkl','rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))

application =Flask(__name__)
app= application

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def predict_api():
    data = request.get_json()
    Temperature = float(data.get('Temperature'))
    RH = float(data.get('RH'))
    Ws = float(data.get('Ws'))
    Rain = float(data.get('Rain'))
    FFMC = float(data.get('FFMC'))
    DMC = float(data.get('DMC'))
    ISI = float(data.get('ISI'))
    Classes = 1
    Region = 0

    new_data_scaled = standard_scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
    result = ridge_model.predict(new_data_scaled)
    return jsonify({'prediction': float(f"{result[0]:.2f}")})


if __name__=="__main__":
    app.run(host="0.0.0.0")