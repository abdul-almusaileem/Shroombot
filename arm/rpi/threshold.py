
def threshold(real=[], computed=[], window=0.5):
    flag = 0
    THRESHOLD_BOOLS = []
    
    THRESHOLD_BOOLS.append(abs(real[0]) -  window < (abs(computed[0]))
                           and abs(real[0]) + window > abs(computed[0]))

    THRESHOLD_BOOLS.append(abs(real[1]) - window < (abs(computed[1]))
                          and abs(real[1]) + window > abs(computed[1]))
    
    THRESHOLD_BOOLS.append(abs(real[2]) - window < (abs(computed[2]))
                           and abs(real[2]) + window > abs(computed[2]))
    
    
    flag = THRESHOLD_BOOLS[0] and THRESHOLD_BOOLS[1] and THRESHOLD_BOOLS[2]
    print(THRESHOLD_BOOLS)
    return flag
    