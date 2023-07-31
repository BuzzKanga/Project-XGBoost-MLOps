import requests
import json

url = 'http://localhost:9696/predict'

customer = {
    "State":"FL",
    "Account Length":131,
    "Area Code":707,
    "Int'l Plan":"no",
    "VMail Plan":"yes",
    "VMail Message":400,
    "Day Mins":4.6298486156,
    "Day Calls":4,
    "Eve Mins":3.5019160814,
    "Eve Calls":1,
    "Night Mins":4.0989253823,
    "Night Calls":150,
    "Intl Mins":4.3284419486,
    "Intl Calls":4,
    "CustServ Calls":6
}

customer_json = json.dumps(customer)

response = requests.post(url, json=customer_json).json()
print(response)

if response['churn'] == True:
    print('Customer will churn')
else:
    print('Customer will not churn')