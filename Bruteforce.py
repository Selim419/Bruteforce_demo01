import time
import itertools
import random

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def bruteforce(charset, min_length, max_length):
    start_time = time.time()
    print(f"Brute force in progress...")
    
    for length in range(min_length, max_length + 1):
        for combination in itertools.product(charset, repeat=length):
            password = ''.join(combination)
            elapsed_time = time.time() - start_time
            print(f"Attempted password: {password}. Time elapsed: {elapsed_time} seconds.")
