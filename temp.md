4d3515912fb7fc8257da44df5bee77ce
4d3515912fb7fc8257da44df5bee77ce MATCH!  => use testhmac.py which computes hex(md5((b'username:realm:password'))) 
This works without a static secret or a turn_secret value

(MySQL reachable at 127.0.0.1 because coturn is running in 'host' network mode)
Turn admin command to add user in MySQL
turnadmin -a -M "host=127.0.0.1 dbname=coturn user=coturn password=" -u user -r matchflix -p pass



Troubleshoot:
- Why turnutilities are not working from the peer when using host.docker.internal? (netcat connects successfully)
- is there a difference between STUN/TURN credentials and TURN API credentials
- write coturn logs somewhere specific
