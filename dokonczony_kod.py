import hashlib
import sys


def zlam_hash(hash_format, wordlist, hash_1):
    with open(wordlist, 'r', encoding='utf-8') as file:
        for line in file:
            password = line.strip()
            if hash_format == 'md5':
                hashed_password = hashlib.md5(password.encode()).hexdigest()
            elif hash_format == 'sha3-512':
                hashed_password = hashlib.sha3_512(password.encode()).hexdigest()
            elif hash_format == 'sha256':
                hashed_password = hashlib.sha256(password.encode()).hexdigest()

            if hashed_password == hash_1:
                print(f"Hasło znalezione: {password}")
                return

    print("Hasło nie znalezione w wordliście.")


if len(sys.argv) == 4:
    hash_format = sys.argv[1]
    wordlist = sys.argv[2]
    hash_1 = sys.argv[3]
    zlam_hash(hash_format, wordlist, hash_1)
else:
    print("Za mało argumentów.")
