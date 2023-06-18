import os
from flask import request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
from app import app

load_dotenv()

client = MongoClient(os.getenv('MONGODB_CONNECTION_STRING'))
db = client[os.getenv('DB_NAME')]
collection = db[os.getenv('COLLECTION_NAME')]

@app.route('/calculate_premium', methods=['POST'])
def calculate_premium():
    request_data = request.json
    ages = request_data['ages']
    sum_insured = int(request_data['sum_insured'])
    city_tier = int(request_data['city_tier'])
    tenure = int(request_data['tenure'])

    rate_card = collection.aggregate([
        {
            '$match': {
                'Age': {
                    '$in': ages
                    },
                'SumInsured': sum_insured, 
                'TierID': city_tier, 
                'Tenure': tenure
            }
        }, {                    
            '$project': {
                '_id': 0, 
                'Age': 1, 
                'Rate': 1
            }
        }, {
            '$sort': {
                'Age': -1
            }
        }
    ])
    
    if rate_card:
        dataFetchAll = list(rate_card)
        premium = calculate_premium_from_rate_card(dataFetchAll)
        return jsonify({'premium': premium})
    else:
        return jsonify({'error': 'Rate card not found for the provided inputs.'}), 404


def calculate_premium_from_rate_card(rate_card):
    rateArray = []
    for index, entry in enumerate(rate_card):
        if index == 0:
            rateArray.append(entry['Rate'])
        else:
            rateArray.append(entry['Rate'] / 2)
    print(rateArray)
    return sum(rateArray)
    
 