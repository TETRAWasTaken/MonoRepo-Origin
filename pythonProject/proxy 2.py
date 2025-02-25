import socket
hostname = socket.gethostname()
addresses = socket.getaddrinfo(hostname, None, socket.AF_INET6)
ipv6_address = addresses[1][4][0]

