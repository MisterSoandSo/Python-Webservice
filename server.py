from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import os

from backend import dummy_computation_func, dummy_computation_func_with_delay

app = Flask(__name__)

PORT = 5000
cert_file = 'ssl/example.crt'
key_file = 'ssl/example.key'

# Check if the certificate and key files exist
if not os.path.isfile(cert_file) or not os.path.isfile(key_file):
    raise Exception("SSL/TLS certificate and key files are missing.")

app.config['JWT_SECRET_KEY'] = 'your-secret-key'
app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config['JWT_HEADER_TYPE'] = 'Bearer'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False 

# Create a JWT manager
jwt = JWTManager(app)

limiter = Limiter(
    app=app,
    storage_uri="memory://",
    key_func=get_remote_address,
)

dummy_comp = [dummy_computation_func, dummy_computation_func_with_delay]

#User Database
users = {}

# Routes
@app.route('/status', methods=['GET'])
@limiter.limit("10 per minute")  # Allow 10 requests per minute
def status():
    return "Online!"

@app.route('/login', methods=['POST'])
@limiter.limit("2 per minute")  # Prevent Brute Force Logins
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = users.get('user_id')

    if user and password == user['password']:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    data = request.headers.get('Payload')
    compute = int(request.headers.get('Compute'))

    if not data:
        return jsonify({'error': 'Data is missing'}), 401
    if compute >= len(dummy_comp):
        return jsonify({'error': 'Algorithm not implemented'}), 501
    return jsonify({'message': dummy_comp[compute](data)})

if __name__ == '__main__':
    app.run(debug=True, port=PORT, ssl_context=(cert_file, key_file))
