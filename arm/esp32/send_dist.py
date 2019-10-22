
# this method is to send the mushroom distance to the pi
#
 
import socket
import struct
import sys
 
def send_dist(z, addr="172.20.10.3", port=5002):
    #
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
    sock.connect((addr, port))
    z_data = struct.pack("f", z)
    sock.send(z_data)
    sock.close()
    
    return 1
         