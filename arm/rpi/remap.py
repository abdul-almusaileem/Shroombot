
import math

# this function is to remap the coordinates using Brandon's lOgIc
#
def remap(id=0, angles=[]):#, scan_flag=1):

    # reference angles for Brandon's LoGic
    # TODO: CLEAN OR FIND A WAY TO EXPLAIN
    #
    REF_ANGLES = [55, 120, 36, 120, 120, 120]

    # remap by id
    #    
    if(id == 0):
        angles[id] = REF_ANGLES[id] + angles[id]
    elif (id == 4):
        angles[id] = REF_ANGLES[id] - (90 + -1 * (angles[1] + angles[2]+ angles[3]))
    elif(angles[id] >= 0):
        angles[id] = REF_ANGLES[id] - abs(angles[id])
    elif(angles[id] < 0):
            angles[id] = REF_ANGLES[id] + abs(angles[id])

    return abs(angles[id])