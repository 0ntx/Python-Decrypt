import hashlib
import string
import itertools

def brute_force_sha256(hash_to_crack, max_length=5):
    characters = string.ascii_letters + string.digits 
    for length in range(1, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            test_string = ''.join(combination)
            hashed_string = hashlib.sha256(test_string.encode()).hexdigest()
            if hashed_string == hash_to_crack:
                return test_string
    return None

hash_target = "185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969"  # enter your hash
result = brute_force_sha256(hash_target)

if result:
    print(f"Hash result : {result}")
else:
    print("Hash is not decryptable or can't be break.")
