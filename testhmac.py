import hashlib

username = "testuser"
realm = "matchflix.it"
password = "pass"

# Create the input string
input_str = f"{username}:{realm}:{password}"

# Generate the MD5 hash
hmac = hashlib.md5(input_str.encode()).hexdigest()

print(hmac)
