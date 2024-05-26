"""
Map the joint space to the actuator space
"""

import numpy as np
import numpy.polynomial.polynomial as poly


def map_top(top):
    """Map the top arm joint space to the actuator space"""
    top_function = np.array(
        [
            3.35529148e06,
            8.84410306e05,
            1.04328896e05,
            7.27541210e03,
            3.33457682e02,
            1.05531503e01,
            2.35430936e-01,
            3.70394212e-03,
            4.02870939e-05,
            2.88614537e-07,
            1.22600360e-09,
            2.34010917e-12,
        ]
    )
    return poly.polyval(top, top_function)


def map_mid(mid):
    """Map the mid arm joint space to the actuator space"""
    mid_function = np.array(
        [
            -2.31885589e03,
            -1.29855133e03,
            -2.87799053e02,
            -3.59886151e01,
            -2.84267136e00,
            -1.49601283e-01,
            -5.37399856e-03,
            -1.32283879e-04,
            -2.19520825e-06,
            -2.34769509e-08,
            -1.46135153e-10,
            -4.02335473e-13,
        ]
    )
    return poly.polyval(mid, mid_function)


def map_btm(btm):
    """Map the btm arm joint space to the actuator space"""
    btm_function = np.array(
        [1.35976942e02, -4.51701069e00, 1.09257558e-01, -2.00390181e-03, 1.38400627e-05]
    )
    return poly.polyval(btm, btm_function)
