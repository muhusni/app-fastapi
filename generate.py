import secrets

def generate_secret_key(length=32):
    """
    Generate a secret key for JWT signing.
    
    :param length: Length of the generated key (in bytes). Default is 32 bytes (256 bits).
    :return: A secret key as a hexadecimal string.
    """
    secret_key = secrets.token_hex(length)
    return secret_key

# Generate a secret key
key = generate_secret_key()
print("Generated Secret Key:", key)