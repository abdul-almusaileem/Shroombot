
# this function is to remap the coordinates using Brandon's lOgIc
#
def remap(id=0, angles=[], negX_flag=0):
        
    # reference angles for Brandon's LoGic
    # TODO: CLEAN OR FIND A WAY TO EXPLAIN
    #
    REF_ANGLES = [55, 120, 36, 120, 120, 120]

    if(id == 0):
        angles[id] = REF_ANGLES[id] + angles[id]
    # angles[id] = angles[id] + REF_ANGLES[id]
    if(id != 0 and angles[id] >= 0):
        angles[id] = REF_ANGLES[id] - abs(angles[id])
    elif(id != 0 and angles[id] < 0):
        angles[id] = REF_ANGLES[id] + abs(angles[id])
        
        
    # if (angles[id] < 0):
    #     angles[id] = 0
    
    return abs(angles[id])