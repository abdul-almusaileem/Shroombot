import struct
import machine
from time import sleep


#
#
def main():
    motor = conn()

    set_id(motor)

    while True:
        move(motor, 1000, 2000)
        sleep(2)
        move(motor, 0, 2000)
        sleep(2)


#
#
def conn():
    return machine.UART(2, baudrate=115200, rx=16, tx=17, timeout=10)

#
#
def ones_comp(num):
   mm = struct.pack('<H', num)
   return (mm[0]^0xFF)



def highlowbyte(num):
   mm = struct.pack('<H', num)
   return (hex(mm[1]), hex(mm[0]))

#
#
def checksum(ibuf, maxindx):
    sum = 0

    # sum the bytes except the fries two
    #
    for i in range(2, maxindx):
        byte = struct.unpack('>H', bytearray(b'\x00'+ibuf[i]))[0]
        sum += byte

    # take the one's comp of the sum and assign it to the last byte
    #
    ibuf[maxindx] = ones_comp(sum)

    #print(sum, ibuf[maxindx])

    return ibuf[maxindx]

#
#
def set_id(motor):

    # buffer!!!
    #
    buf = [0] * 7
    buf[0] = b'\x55'
    buf[1] = b'\x55'
    buf[2] = b'\xFE'
    buf[3] = b'\x04'
    buf[4] = b'\x0D'
    buf[5] = b'\x03' # ID

    #
    #
    checksum_num = [checksum(buf, len(buf)-1)]
    checksum_byte = bytes(checksum_num)
    buf[6] = checksum_byte

    print(buf)

    for i in range(0, len(buf)):
        motor.write(buf[i])


def move(motor, position, time):
    # move
    # TODO: make the ID
    #
    buf = [0] * 10

    #
    #
    (pos_high, pos_low) = highlowbyte(position)
    (time_high, time_low) = highlowbyte(time)

    buf[0] = b'\x55'
    buf[1] = b'\x55'
    buf[2] = b'\x03' # ID
    buf[3] = b'\x07'
    buf[4] = b'\x01'

    buf[5] = bytes([int(pos_low)])
    buf[6] = bytes([int(pos_high)])

    buf[7] = bytes([int(time_low)])
    buf[8] = bytes([int(time_high)])
    #buf[7] = b'\xE8' # time_low
    #buf[8] = b'\x03' # time_high

    checksum_num = [checksum(buf, len(buf)-1)]
    checksum_byte = bytes(checksum_num)
    buf[9] = checksum_byte

    print(buf)

    for i in range(0, len(buf)):
        motor.write(buf[i])

if __name__ == '__main__':
    main()
