#Microservice para hospedaje
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

listOfHospedajes = [{"hotel-name":"disneyland hotel", "check-in":"04/07/2022", "check-out":"06/07/2022"}]

@app.route('/list', methods=["GET"])
def getHospedajes():
    return jsonify(eqtls=listOfHospedajes).get_data()

@app.route('/create', methods=["POST"])
def postHospedajes():
    val = request.get_data(as_text=True)
    try:
        x = json.loads(val)
        listOfHospedajes.append(x)
    except:
        listOfHospedajes.append(val)
    return val

if __name__ == "__main__":
    app.run()
