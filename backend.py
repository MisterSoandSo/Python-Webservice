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
