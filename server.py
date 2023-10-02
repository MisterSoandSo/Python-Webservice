from flask import Flask

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def a_msg():
    return "Alive!"

@app.route('/predict', methods=['GET'])
def b_msg():
    return "Prediction!"


app.run(debug=True, port = 5000)