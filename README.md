# MatchFlix




# TURN Server API
- Shared secret generated by TURN Server
- The shared secret can be used by an application to generate access credentials for the TURN server [Reference](https://stackoverflow.com/questions/35766382/coturn-how-to-use-turn-rest-api)
- [TURN REST API](https://datatracker.ietf.org/doc/html/draft-uberti-behave-turn-rest-00) 
- Update MySQL DB data from coturn with turnadmin *turnadmin (operation) -r test -M "host=172.21.0.3 dbname=coturn user=coturn password=coturn_password"*