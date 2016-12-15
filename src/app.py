from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/classify")
def predict():
    #return CNTK prediction
    return json.dumps([{'cat1': 0.5}, {'cat2': 0.2}, {'cat3': 0.1}])

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=80)