
import pickle
import pandas as pd
import json
import xgboost as xgb

from flask import Flask
from flask import request
from flask import jsonify

model_file = 'churn-model.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

app = Flask('churn')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    
    # Convert JSON to Python dictionary
    data_dict = json.loads(customer)

    X_test_customer = pd.DataFrame.from_dict([data_dict])
    y_test_customer = pd.DataFrame({'Churn?':[0]})

    X_test_customer['State'] = X_test_customer['State'].astype('category')
    X_test_customer["Int'l Plan"] = X_test_customer["Int'l Plan"].astype('category')
    X_test_customer['VMail Plan'] = X_test_customer['VMail Plan'].astype('category')
 
    dtest = xgb.DMatrix(X_test_customer, label=y_test_customer, enable_categorical=True)

    y_pred_prob = model.predict(dtest)
    y_pred = (y_pred_prob >= 0.5).astype(int)
    
    # Create the response dictionary
    result = {
        'churn_probability': float(y_pred_prob[0]),
        'churn': bool(y_pred[0])
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)