from flask import Flask

import service_predict_via_heuristics

app = Flask(__name__)

@app.route('/')
def index():
  return 'data-type-predictor - Server Works!'

#adding variables
@app.route('/predict_type/<property_name>')
def predict_type(property_name):
    prediction = service_predict_via_heuristics.predict_type_from_name(property_name, True)
    return f'property_name: {property_name} -> predicted type={prediction}'
