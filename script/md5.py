import hashlib
import string
import itertools

def brute_force_hash(hash_to_crack, hash_type='MD5', max_length=5):
    characters = string.ascii_letters + string.digits
    hash_function = getattr(hashlib, hash_type)


    for length in range(1, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            test_string = ''.join(combination)
            hashed_string = hash_function(test_string.encode()).hexdigest()
            if hashed_string == hash_to_crack:
                return test_string
    return None

hash_target_md5 = "5d41402abc4b2a76b9719d911017c592"
result_md5 = brute_force_hash(hash_target_md5, hash_type='md5')
if result_md5:
    print(f"Hash result : {result_md5}")
else:
    print("Hash is not decryptable or can't be break.")
