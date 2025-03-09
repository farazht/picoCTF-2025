## Chronohack

Pretty straight forwards python code. Basically, the exploit lies in the fact that the token is generated *when* we connect. We as the attacker also know the time (though not exactly), so we can take guesses around when we connect.

Referenced [this stackoverflow post](https://stackoverflow.com/questions/21233340/sending-string-via-socket-python) and this [guide](https://www.geeksforgeeks.org/socket-programming-python/) to learn how to use sockets.
