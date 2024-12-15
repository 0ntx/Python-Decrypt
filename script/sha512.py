import hashlib
import string
import itertools

def brute_force_hash(hash_to_crack, hash_type='sha512', max_length=5):
    characters = string.ascii_letters + string.digits
    hash_function = getattr(hashlib, hash_type)
    
    for length in range(1, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            test_string = ''.join(combination)
            hashed_string = hash_function(test_string.encode()).hexdigest()
            if hashed_string == hash_to_crack:
                return test_string
    return None

hash_target_sha512 = "ee26b0dd4af7e749aa1a8ee3c10ae9923f618980772e473f8819a5d4940e0db27ac185f8a0e1d5f8a9d5ac64470d93f437f4e37a804bcf3ac43e73272f5b3c1d"
result_sha512 = brute_force_hash(hash_target_sha512, hash_type='sha512', max_length=6)
if result_sha512:
    print(f"Hash result : {result_sha512}")
else:
    print("Hash is not decryptable or can't be break.")