# Python Webservice
 A python webservice that performs some dummy computations and returns a result. The project intends to simulate some computationally intensive python code that can be insert into the webservice.

## Project Status: Ongoing (as of 10/15/2023)

### Initial Goals:

- [x] Take a JSON string as input and return a JSON string as output.
- [x] Ensure secure HTTPS communication with username and password authentication. Passwords should be hashed.
- [x] Set up a database to store login credentials and keys.
- [x] Create a user management system that includes a database for storing login credentials and keys, and handles both login and registration processes.
- [ ] Implement the ability to handle multiple computations concurrently.

Additional goals
1. Stricter Access Control
2. Input validation and sanitzation
3. Better Rate Limit Control
4. Login Monitor
5. Admin Management Panel

### Server
***(To be announced)***

### Client
***(To be announced)***

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