import itertools
import hashlib
import sys
import time

def password_cracker(target, charset, max_length):
    target = hashlib.sha256(target.encode()).hexdigest()

    for length in range(1, max_length + 1):
        for combination in itertools.product(charset, repeat=length):
            attempt = ''.join(combination)
            attempt_hash = hashlib.sha256(attempt.encode()).hexdigest()
            if attempt_hash == target:
                return f"Cracked! Password is: {attempt}"
            print(f"Attempt: {attempt}", end="\r")
            time.sleep(0.01)
    return "Failed to crack the password"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <hash>")
        sys.exit(1)

    hash_to_crack = sys.argv[1]

    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789[]{}()*;/,._-"
    max_length = 16

    start_time = time.time()
    result = password_cracker(hash_to_crack, charset, max_length)
    print("\n")
    print(result)
    end_time = time.time()

    print(f"Time taken: {end_time - start_time} seconds")