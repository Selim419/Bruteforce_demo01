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
            sys.stdout.write(f"Attempt: {attempt}\r")
            sys.stdout.flush()
            time.sleep(0.01)
    return "Failed to crack the password"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <hash> <charset>")
        sys.exit(1)

    hash_to_crack = sys.argv[1]
    charset = sys.argv[2]
    max_length = 16

    start_time = time.time()
    result = password_cracker(hash_to_crack, charset, max_length)
    end_time = time.time()

    print("\n")
    print(result)
    print(f"Time taken: {end_time - start_time} seconds")
