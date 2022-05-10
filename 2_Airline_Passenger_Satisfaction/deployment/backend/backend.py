from flask import Flask, jsonify, request
import pickle
import pandas as pd

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

columns = [
 'Customer Type',
 'Age',
 'Type of Travel',
 'Class',
 'Flight Distance',
 'Inflight wifi service',
 'Departure/Arrival time convenient',
 'Ease of Online booking',
 'Gate location',
 'Food and drink',
 'Online boarding',
 'Seat comfort',
 'Inflight entertainment',
 'On-board service',
 'Leg room service',
 'Baggage handling',
 'Checkin service',
 'Inflight service',
 'Cleanliness',]

classes = ['neutral or dissatisfied', 'satisfied']

@app.route("/")
def home():
    return "<h1>It Works!</h1>"

@app.route("/predict", methods=['GET','POST'])
def model_prediction():
    if request.method == "POST":
        content = request.json
        try:
            data=[content['Customer Type'],
            content['Age'],
            content['Type of Travel'],
            content['Class'],
            content['Flight Distance'],
            content['Inflight wifi service'],
            content['Departure/Arrival time convenient'],
            content['Ease of Online booking'],
            content['Gate location'],
            content['Food and drink'],
            content['Online boarding'],
            content['Seat comfort'],
            content['Inflight entertainment'],
            content['On-board service'],
            content['Leg room service'],
            content['Baggage handling'],
            content['Checkin service'],
            content['Inflight service'],
            content['Cleanliness'],
            ]

            data = pd.DataFrame([data], columns=columns)
            res = model.predict(data)
            response = {"code": 200, "status":"OK", 
                        "result":{"prediction":str(res[0]),
                                   "description":classes[res[0]]}}
            return jsonify(response)
        except Exception as e:
            response = {"code":500, "status":"ERROR", 
                        "result":{"error_msg":str(e)}}
            return jsonify(response)
    return "<p>Silahkan gunakan method POST untuk mengakses hasil prediksi dari model</p>"

# app.run(debug=True)