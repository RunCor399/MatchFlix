# MatchFlix




# TURN Server API
- Shared secret generated by TURN Server
- The shared secret can be used by an application to generate access credentials for the TURN server [Reference](https://stackoverflow.com/questions/35766382/coturn-how-to-use-turn-rest-api)
- [TURN REST API](https://datatracker.ietf.org/doc/html/draft-uberti-behave-turn-rest-00) 
- Update MySQL DB data from coturn with turnadmin *turnadmin (operation) -r test -M "host=172.21.0.3 dbname=coturn user=coturn password=coturn_password"*






Your architecture for the video chat application sounds solid! Here's how you can manage the interaction between your Spring application and the Coturn server, particularly focusing on user authentication and connection.
Overview of Interaction

1. User Authentication: Users authenticate via your Spring application usingKeycloak.
2. Requesting TURN Credentials: Once authenticated, the Spring app generates TURNcredentials (username and password) for the users.
3. User Connection to Coturn: The Spring application provides the TURN credentialsto the client-side WebRTC application, which then uses them to connect to theCoturn server for peer-to-peer communications.
