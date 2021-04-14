from flask import Flask, render_template, jsonify
import random
import json

app = Flask(__name__)
PORT = 3500

@app.route("/", methods=["GET", "POST"])
def startpy():

    result = {

        "Greetings": "Tactlabs welcomes you"
    }

    return render_template("index.html")

@app.route("/data", methods=["GET"])
def read_json():

    


    result_dict = {
        
        
        'users': 'users:',
        'title': 'iPhone 12 pro price in different countries',
        'subtitle': 'source: https://www.statista.com/statistics/793628/worldwide-developer-survey-most-used-languages/',
    }


    return jsonify(result_dict)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
