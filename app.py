from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

model = joblib.load('place.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    iq = float(request.form['iq'])
    cgpa = float(request.form['cgpa'])
    prediction = model.predict([[iq, cgpa]])
    result = 'Placed' if prediction[0] == 1 else 'Not Placed'
    return render_template('index.html', prediction_text=f'Prediction: {result}')

if __name__ == '__main__':
    app.run(debug=True)
