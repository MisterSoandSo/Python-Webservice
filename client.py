import json
import jwt
import requests

SECRET_KEY = 'your-secret-key'
file_loc = 'fake_data.json'
output_file = 'output_' + file_loc

with open(file_loc, 'r') as jf:
    payload = json.load(jf)
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    headers = {'Authorization': token, 'Compute': '0'}
    # print(headers)  # for debugging
    response = requests.get('http://127.0.0.1:5000/api/resource', headers=headers)

    if response.status_code == 200:
        print('Server Response:', response.json())
        with open(output_file, "w") as results:
            json.dump(response.json(), results)
    else:
        print('Server Response:', response.status_code, response.json())

