
# this function is to remap the coordinates using Brandon's lOgIc
#
def remap(id=0, angles=[], negX_flag=0):
        
    # reference angles for Brandon's LoGic
    # TODO: CLEAN OR FIND A WAY TO EXPLAIN
    #
    REF_ANGLES = [235, 120, 36, 120, 120]

    if (id == 0):  
        
        # FIXME: not negative but very large number becomes negative when flipping 
        # FIXME: not sure if that the right fix but this fixed the high too
        # FIXME: this works for X = 0 but X = 1 works but technically shouldn't ?
        #
        print("base: {}".format(angles[id]))      
        if(angles[id] > 240):
            angles[id] = 100
        
        angles[id] = angles[id] + 45
        
        # check if the negative flag was set
        #
        if(negX_flag):
            print("it was negative")
            angles[id] = angles[id] + 90
        
        # FIXME: the angles changes here before that it's not negative
        #    
        if angles[id] > 270:
            angles[id] = 360 - angles[id]
            
            
    elif (id == 1): 
        angles[id] = abs(REF_ANGLES[id] - angles[id])
        
    elif (id == 2):
        angles[id] = abs(REF_ANGLES[id] - angles[id])
      
    elif (id == 3):
        angles[id] = abs(REF_ANGLES[id] - angles[id])
    
    return angles[id]