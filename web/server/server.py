from flask import Flask, request, jsonify
import utils
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/hello')
def helloworld():
    return "hello world"

@app.route('/get-location-names')
def get_location_names():
    response = jsonify({
        'locations': utils.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict-home-price', methods = ['POST'])
def predict_home_price():
    total_sqft = request.form['total_sqft']
    location = request.form['location']
    bath = request.form['bath']
    balcony = request.form['balcony']
    bhk = request.form['bhk']

    response = jsonify({
        'house_price': utils.get_estimated_price(total_sqft, bath, balcony, bhk, location)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("server staring")
    app.run()