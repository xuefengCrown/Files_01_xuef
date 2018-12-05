
##Different computers are independent in the sense that they do not directly share memory.
##Instead, they communicate with each other using messages, information transferred from
##one computer to another over a network.

#4.6.1   Messages
##Messages sent between computers are sequences of bytes. The purpose of a message varies;
##messages can request data, send data, or instruct another computer to evaluate a procedure call.
##In all cases, the sending computer must encode information in a way that the receiving computer
##can decode and correctly interpret. To do so, computers adopt a message protocol that endows
##meaning to sequences of bytes.


# TCP 三次握手
##Establishing a connection between two computers A and B proceeds in three steps:
##1. A sends a request to a port of B to establish a TCP connection, providing a port number
##to which to send the response.
##2. B sends a response to the port specified by A and waits for its response to be acknowledged.
##3. A sends an acknowledgment response, verifying that data can be transferred in both directions.
##
##After this three-step "handshake", the TCP connection is established, and A and B can send data
##to each other. Terminating a TCP connection proceeds as a sequence of steps in which both the
##client and server request and acknowledge the end of the connection.

from socket import gethostbyname
##print(gethostbyname('www.baidu.com'))

from urllib.request import urlopen
response = urlopen('https://www.baidu.com').read()
print(response[:15])

##Upon receiving this response, the browser issues additional requests for images,
##videos, and other auxiliary components of the page. These requests are initiated
##because the original HTML document contains addresses of additional content and
##a description of how they embed into the page.


#Modularity.
##The concepts of client and server are powerful abstractions.
##A server provides a service, possibly to multiple clients simultaneously,
##and a client consumes that service. The clients do not need to know the details of
##how the service is provided, or how the data they are receiving is stored or calculated,
##and the server does not need to know how its responses are going to be used.



# P2P
##In a peer-to-peer system, all components of the system contribute some processing power
##and memory to a distributed computation.

##Division of labor among all participants is the identifying characteristic of a
##peer-to-peer system. This means that peers need to be able to communicate with each
##other reliably. In order to make sure that messages reach their intended destinations,
##peer-to-peer systems need to have an organized network structure. The components in
##these systems cooperate to maintain enough information about the locations of other
##components to send messages to intended destinations.



