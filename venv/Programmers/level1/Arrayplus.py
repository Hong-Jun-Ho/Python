import numpy as np
def solution(priorities, location):
    return (np.array(priorities)+np.array(location)).tolist()