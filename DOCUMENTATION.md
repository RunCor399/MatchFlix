

## TODO
1. Automate Keycloak Realm import when installing the chart   
2. Create basic Spring Application that integrates with Keycloak and Postgres   (db name: matchflix_app)
    1. Study Kotlin Again
    2. Install IntelliJ
    3. Code
3. Add Spring app to Helm Chart
4. Setup CI to build Spring app code and deploy new image
5. Setup CI to build and deploy Helm Chart
6. Create basic React Web App that invokes Spring App APIs
7. Add React Web App to Helm Chart
8. Setup CI to build React app code and deploy new image
9. Modify CoTurn server configuration with a static secret stored in DB or config file (DB would be better)
10. Share secret between CoTurn and Spring App, and implement endpoint to return TURN credentials to REACT WebApp
11. Test the ability of the React App to authenticate with the CoTurn Server using the credentials returned by the Spring App
12. Connect the CIs so that when Spring or React code is built, a new deployment pipeline is started. Deployment pipeline should also be started when the code of the Helm chart is updated itself

X. Switch Coturn DB from MySQL to the Postgres (db name: matchflix_coturn)

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


