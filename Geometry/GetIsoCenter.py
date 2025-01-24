from typing import List, Tuple
import numpy as np
def get_iso_center(cst, ct, visBool=False):
    V = []
    no_obj_or_const = None
    if cst.shape[1] >= 6:
        no_obj_or_const = all(elem is None or elem is '' for elem in cst[:,5])
    else:
        no_ob_or_const = True

    for i in range(0,cst.shape[0]):
        if cst[i, 2] == "TARGET" and (no_obj_or_const or cst[i, 5] is not None):
            V.append(V, cst[i, 3][0])

    V = np.unique(V)

    if V.size == 0:
        #The code for this will be added in later versions
        pass






