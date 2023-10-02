from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    storage_uri="memory://",
)

@app.route('/status', methods=['GET'])
def a_msg():
    return "Alive!"

@app.route('/predict', methods=['GET'])
@limiter.limit("5/minute")  # Allow 5 requests per minute
def b_msg():
    return "Predictionroute is rate-limited!"


if __name__ == '__main__':
    app.run(debug=True, port = 5000)