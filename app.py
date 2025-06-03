from flask import Flask, request, Response
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.route('/whitepages/phone', methods=['POST'])
def simulate_phone_api():
    data = request.json
    phone_number = data.get("phone_number", "")

    # Build XML
    root = ET.Element("WhitepagesPhoneResponse")
    ET.SubElement(root, "phone_number").text = phone_number
    ET.SubElement(root, "is_valid").text = "true"
    ET.SubElement(root, "line_type").text = "Mobile"
    ET.SubElement(root, "carrier").text = "Verizon Wireless"
    ET.SubElement(root, "is_prepaid").text = "false"
	ET.SubElement(root, "is_voip").text = "true"
    ET.SubElement(root, "is_commercial").text = "false"
    ET.SubElement(root, "country_calling_code").text = "1"
    ET.SubElement(root, "phone_risk_score").text = "77"

    xml_str = ET.tostring(root, encoding="utf-8")

    return Response(xml_str, mimetype='application/xml')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
