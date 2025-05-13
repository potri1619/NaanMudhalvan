from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array([[data['temperature'], data['pressure'], data['vibration'], data['speed']]])
    prediction = model.predict(features)[0]
    return jsonify({'status': prediction})

if __name__ == '__main__':
    app.run(debug=True)
