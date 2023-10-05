import json
import requests

# Set the mode to either 'DEV' or 'PROD'
MODE = 'DEV'  # Change this to 'PROD' for production mode

file_loc = 'fake_data.json'
output_file = 'output_' + file_loc

if MODE == 'DEV':
    import warnings
    from urllib3.exceptions import InsecureRequestWarning

    # Mute the InsecureRequestWarning in development mode
    warnings.filterwarnings("ignore", category=InsecureRequestWarning)
    verify_ssl = False
else:
    verify_ssl = True

# Define login data
login_data = {
    'username': 'username',
    'password': 'password_hash'
}

url = 'https://127.0.0.1:5000/'

# Attempt to log in
login_response = requests.post(url + 'login', json=login_data, verify=verify_ssl)

if login_response.status_code == 200:
    try:
        with open(file_loc, 'r') as jf:
            payload = json.load(jf)
            access_token = login_response.json().get('access_token')
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Payload': json.dumps(payload),
                'Compute': '1'
            }
    except FileNotFoundError:
        print(f"File not found: {file_loc}")
    except Exception as e:
        print(f"An error occurred while opening the file: {e}")

    # Access a protected resource
    protected_response = requests.get(url + 'protected', headers=headers, verify=verify_ssl)

    if protected_response.status_code == 200:
        print(protected_response.json())
    else:
        print('Error Code:', protected_response.status_code)
else:
    print('Login failed. Invalid credentials.')
