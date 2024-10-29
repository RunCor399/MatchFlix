

## TODO
- Use Github issues to manages tasks
- Investigate interaction between Spring app and CoTurn (how is the user allowed to authenticate to the TURN server? => backend returns credentials to the client, the CoTurn init key in this way is only known to backend and CoTurn itself)

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

### Credentials generation
- CoTurn server starts up with with a fixed secret key (can this be dynamic? can it be shared with the webapp backend?)
- CoTurn's startup secret key can be saved in "turn_secret" DB table, making it dynamic => instead of using a static secret, **populate the turn_secret table** so that the secret can be retrieved by the backend

Username and Password generation with python snippet:
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

- Once I have a username and generated HMAC, update **turnusers_lt** table to store the new user 
- Therefore Spring app has access to the same DB as the TURN server

## Problems
- Share CoTurn fixed key with the webapp backend


