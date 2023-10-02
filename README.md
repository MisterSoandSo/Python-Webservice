# Python Webservice
 A python webservice that performs some dummy computations and returns a result. The project intends to simulate some computationally intensive python code that can be insert into the webservice.

The initial goal are as follow:
1. Take a json string as input and return a json string as output.
2. Needs to be secure with https and a username and password. Passwords hash required.
3. Needs to be able to handle multiple computations concurrently.
4. Database to store login cerdentials and keys.

### Server
***TBA***

### Client
***TBA***

### Rate Limit
```
"5 per second": This sets a rate limit of 5 requests per second.
"10 per minute": This sets a rate limit of 10 requests per minute.
"2 per hour": This sets a rate limit of 2 requests per hour.
"100 per day": This sets a rate limit of 100 requests per day.
```

## Setup Virtual Environment
In the console or terminal, type `python -m venv venv` to initialize the python virtual environment. In linux, you might have to run `sudo apt update && apt update -y` to install pip for later uses.
```
# Windows Users
.\venv\Scripts\activate

# Unix/ Mac Users
source venv/bin/activate

# Exit venv Command
deactivate

```

## Requirements
Using ``pip install -r requirements.txt`` should cover everything.

## License
This project is licensed under the GNU v3 License.