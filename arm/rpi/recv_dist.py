
# this method receives the z from the esp
#

import socket
import struct
import sys

def recv_z(host="172.20.10.3", port=5002):
    #
    #
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

        sock.bind((host, port))
        sock.listen(1)
        sock.settimeout(30)

        #
        while True:
            #accept connection
            #
            try:
                conn, addr = sock.accept()
                

                # verify connection
                #
                print("{} is connected".format(addr))
                
                # receive data
                #
                while True:
                    data = conn.recv(1024)
                    #print("data: {}".format(data))
                    # check if no data was sent and exit
                    #
                    if (data == b''):
                        conn.close()
                        sock.close()
                        break
                    
                    # convert data from bytes to float
                    #
                    dist_z = struct.unpack("f", data)[0]
                    
                    # if no data break
                    # 
                    if not data:
                        conn.close()
                        sock.close()
                        break
                    
            except OSError as err:
                print("time out!!!")
                sock.close()
                break
                
    return dist_z 