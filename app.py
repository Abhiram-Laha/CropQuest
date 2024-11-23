from flask import Flask, request, render_template, redirect, url_for, session
import numpy as np
import pickle
from flask_session import Session  

# Load model (Crop Recommendation)
model_crop = pickle.load(open('RandomForest.pkl', 'rb'))

# Load model (Fertilizer Recommendation)
model_ferti = pickle.load(open('classifier.pkl', 'rb'))
ferti = pickle.load(open('fertilizer.pkl', 'rb'))


app = Flask(__name__)


app.config['SESSION_TYPE'] = 'filesystem'  
Session(app)  

@app.route('/')
def home():
    return render_template('index.html')




# Render crop recommendation form page (1)

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




# Render Fertilizer recommendation form page (3)

@app.route('/fert-recommend')
def fertilizer_recommendation():
    result = session.get('result')  
    session.pop('result', None)  
    return render_template("Fertilizer_Rec.html", x=result)

@app.route('/predict-ferti', methods=['POST'])
def predict_fertilizer():
    try:
        temp = request.form.get('temp')
        humi = request.form.get('humid')
        mois = request.form.get('mois')
        soil = request.form.get('soil')
        crop = request.form.get('crop')
        nitro = request.form.get('nitro')
        pota = request.form.get('pota')
        phosp = request.form.get('phos')

        inputs = [temp, humi, mois, soil, crop, nitro, pota, phosp]
        if None in inputs or not all(val.isdigit() for val in inputs):
            session['result'] = 'Invalid input. Please provide numeric values for all fields.'
            return redirect(url_for('home'))

        input_values = [int(val) for val in inputs]
        prediction = model_ferti.predict([input_values])
        res = str(ferti.classes_[prediction[0]])
        session['result'] = res
        return redirect(url_for('fertilizer_recommendation'))

    except Exception as e:
        session['result'] = f"Error: {str(e)}"
        return redirect(url_for('fertilizer_recommendation'))
    
    
    
    
    
    

if __name__ == '__main__':
    app.run(debug=True, port=8000)
