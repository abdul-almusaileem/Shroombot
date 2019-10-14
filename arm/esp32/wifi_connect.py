
import network
# this method is for the esp to connect to wi-fi change config to change SSID
#
def connect(ssid, password):
    # create the station to make esp connect to wifi
    # TODO: understand more
    #
    station = network.WLAN(network.STA_IF)
    
    # check if the esp connected to a network already
    # 
    if station.isconnected() == True:
        
        print("Already connected")
        print("addr = {}".format(station.ifconfig()[0]))
        return

    # connect to a the network
    #
    if (~station.active()):
        station.active(True)
    
    station.connect(ssid, password)
    
    # wait till it connects to the network
    #
    while station.isconnected() == False:
        pass
 
    print("Connection successful")
    print(station.ifconfig())
    addr = station.ifconfig()[0]
    
    return addr