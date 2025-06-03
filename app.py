from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/whitepages/phone', methods=['POST'])
def simulate_phone_api():
    data = request.json
    phone_number = data.get("phone_number", "")

    response = {
        "phone_number": phone_number,
        "is_valid": True,
        "line_type": "Mobile",
        "carrier": "Verizon Wireless",
        "is_prepaid": False,
        "is_commercial": False,
        "country_calling_code": "1",
        "belongs_to": [
            {
                "name": "John Doe",
                "age_range": "35-44",
                "type": "Person",
                "gender": "Male",
                "location": {
                    "city": "San Francisco",
                    "state_code": "CA",
                    "postal_code": "94107",
                    "country_code": "US"
                }
            }
        ],
        "current_addresses": [
            {
                "location": {
                    "city": "San Francisco",
                    "state_code": "CA",
                    "postal_code": "94107",
                    "country_code": "US"
                },
                "delivery_point": "SingleUnit",
                "is_active": True
            }
        ],
        "associated_people": [],
        "alternate_phones": [],
        "warnings": [],
        "error": None,
        "metadata": {
            "request_id": "sim-req-001",
            "timestamp": "2025-06-03T15:00:00Z"
        }
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
