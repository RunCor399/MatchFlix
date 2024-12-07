import hashlib

username = "testuser1"
realm = "matchflix"
password = "testpass1"

# Create the input string
input_str = f"{username}:{realm}:{password}"

# Generate the MD5 hash
hmac = hashlib.md5(input_str.encode()).hexdigest()

print(hmac)
<<<<<<< HEAD




# import hmac
# import hashlib
# import base64
# import time

# def get_turn_credentials(name, secret):
#     # Calculate UNIX timestamp for 24 hours from now
#     unix_timestamp = int(time.time()) + 24 * 3600
#     username = f"{unix_timestamp}:{name}"
    
#     # Create HMAC using SHA1
#     hmac_obj = hmac.new(secret.encode('utf-8'), username.encode('utf-8'), hashlib.sha1)
#     password = base64.b64encode(hmac_obj.digest()).decode('utf-8')
    
#     return {
#         "username": username,
#         "password": password
#     }

# # Example usage
# name = "testuser2"
# secret = "secretkey"
# credentials = get_turn_credentials(name, secret)
# print(credentials)
=======
>>>>>>> cbf5f8905d326da358a2cabf1f3c35e18b2868f4
