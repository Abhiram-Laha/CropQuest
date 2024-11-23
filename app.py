from flask import Flask, request, render_template, redirect, url_for, session
import numpy as np
import pickle
from flask_session import Session  

model_crop = pickle.load(open('RandomForest.pkl', 'rb'))




app = Flask(__name__)


app.config['SESSION_TYPE'] = 'filesystem'  
Session(app)  

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/crop-recommend')
def crop_recommendation():
    return render_template('crop_rec.html')

@app.route("/predict-crop", methods=['POST'])
def predict_crop():
    N = float(request.form['Nitrogen'])
    P = float(request.form['Phosporus'])
    K = float(request.form['Potassium'])
    temp = float(request.form['Temperature'])
    humidity = float(request.form['Humidity'])
    ph = float(request.form['Ph'])
    rainfall = float(request.form['Rainfall'])

    feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)

    prediction = model_crop.predict(single_pred)[0]

    crop_dict = {
        'rice': 'rice.jpg',
        'maize': 'maize.jpg',
        'chickpea': 'chickpea.jpg',
        'kidneybeans': 'kidneybeans.jpg',
        'pigeonpeas': 'pigeonpeas.jpg',
        'mothbeans': 'mothbeans.jpg',
        'mungbean': 'mungbean.jpg',
        'blackgram': 'blackgram.jpg',
        'lentil': 'lentil.jpg',
        'pomegranate': 'pomegranate.jpg',
        'banana': 'banana.jpg',
        'mango': 'mango.jpg',
        'grapes': 'grapes.jpg',
        'watermelon': 'watermelon.jpg',
        'muskmelon': 'muskmelon.jpg',
        'apple': 'apple.jpg',
        'orange': 'orange.jpg',
        'papaya': 'papaya.jpg',
        'coconut': 'coconut.jpg',
        'cotton': 'cotton.jpg',
        'jute': 'jute.jpg',
        'coffee': 'coffee.jpg'
    }

    if prediction in crop_dict:
        image_filename = crop_dict[prediction]
        result = prediction.capitalize()
    else:
        image_filename = 'img.jpg'
        result = "Error occurred, please check the input values."

    return render_template('crop_rec.html', result=result, image_filename=image_filename)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
