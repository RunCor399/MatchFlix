

## TODO

## STUN Server/Protocol (Session Traversal Utilities for NAT)
- Used for self discovery of public network IP address (behind NAT)
- STUN protocol uses UDP
- STUN server listens on 3478 by default


## TURN Server (Traversal Using Relay around NAT)
- Provide STUN capability and more
- When direct connection between two endpoints it's not possible, TURN is a protocol for relaying media traffic through a service
- Basic Authentication mechanism



## ICE (Interactive Connectivity Establishment)
- Standard for using STUN and TURN to establish connection between two endpoints
- Coordinates management of STUN, TURN and TURNS to optimize connection establishment and precedence between the preferred method





## CoTurn

### Authentication Flow
1. User creates an account
2. Backend persists the user in Keycloak backed by MySQL DB
3. Backend generates and returns to the user ephemeral TURN credentials
4. User authenticates to CoTurn using the ephemeral credentials

### Credentials generation
- CoTurn server starts up with with a fixed secret key. Instead of hardcoding the secret I can store it in the turn_secret table of the same DB used by the Backend
- Username and fixed secret are used to generate the ephemeral credentials

Username and fixed secret generation with python snippet:
```py
import hashlib
import hmac
import base64
from time import time

user = 'your-arbitrary-username'
secret = 'this-is-the-secret-configured-for-coturn-server'

ttl = 24 * 3600 # Time to live
timestamp = int(time()) + ttl
username = str(timestamp) + ':' + user
dig = hmac.new(secret.encode(), username.encode(), hashlib.sha1).digest()
password = base64.b64encode(dig).decode()

print('username: %s' % username)
print('password: %s' % password)
```



## Problems
- Share CoTurn fixed key with the webapp backend (k8s secret)


