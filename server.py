from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import jwt
import time
import random

app = Flask(__name__)

# Secret key for signing and verifying tokens
SECRET_KEY = 'your-secret-key'

limiter = Limiter(
    app=app,
    storage_uri="memory://",
    key_func=get_remote_address,
)

# Server Processing Functions
def dummy_computation_func(packet):
    reply = '{0} {1} is {2} years old and lives in {3}.'.format(packet['first_name'], packet['last_name'], packet['age'], packet['city']) 
    return reply

def dummy_computation_func_with_delay(packet):
    reply = dummy_computation_func(packet)
    time_list = [6, 15, 25, 30, 80]
    time.sleep(random.choice(time_list))  # Simulate Long Computation Process
    return reply

dummy_comp = [dummy_computation_func, dummy_computation_func_with_delay]

# Routes
@app.route('/status', methods=['GET'])
def status():
    return "Online!"

@app.route('/predict', methods=['GET'])
@limiter.limit("5 per minute")  # Allow 5 requests per minute
def rate_limited_route():
    return "Route is rate-limited!"

@app.route('/api/resource', methods=['GET'])
def protected_resource():
    token = request.headers.get('Authorization')
    compute = int(request.headers.get('Compute'))

    if not token:
        return jsonify({'error': 'Token is missing'}), 401
    if compute >= len(dummy_comp):
        return jsonify({'error': 'Algorithm not implemented'}), 501

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return jsonify({'message': dummy_comp[compute](payload)})
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 401

if __name__ == '__main__':
    app.run(debug=True, port=5000)
