import json
import time
import random

# Server Processing Functions
def dummy_computation_func(packet):
    packet = json.loads(packet)
    reply = '{0} {1} is {2} years old and lives in {3}.'.format(packet['first_name'], packet['last_name'], str(packet['age']), packet['city']) 
    return reply

def dummy_computation_func_with_delay(packet):
    reply = dummy_computation_func(packet)
    time_list = [6, 15, 25, 30, 80]
    time.sleep(random.choice(time_list))  # Simulate Long Computation Process
    return reply


# Database Management
import sqlite3
import hashlib

class UserManagement():
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT NOT NULL UNIQUE,
                            password TEXT NOT NULL
                        )''')

        self.conn.commit()

    def register_user(self,username,password) -> bool:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            # Username already exists
            return False

    def login_user(self,username,password) -> bool:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
        self.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
        user = self.cursor.fetchone()
        return True if user else False
    
    def list_users(self) -> list:
        query = "SELECT * FROM users"
        self.cursor.execute(query)

        users = []
        for row in self.cursor.fetchall():
            user_dict = {
                "id": row[0],
                "username": row[1],
            }
            users.append(user_dict)
        return users