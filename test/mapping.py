import csv
import numpy as np
import numpy.polynomial.polynomial as poly # Maybe need to use the newer package: https://stackoverflow.com/questions/18767523/fitting-data-with-numpy
from matplotlib import pyplot as plt

with open("btm.csv", "r") as btm:
    reader_obj = csv.reader(btm)
    btm_arr_0 = list()
    btm_arr_1 = list()
    j = 0
    for i in reader_obj:
        if j != 0:
            print(i[1], i[2])
            btm_arr_0.append(int(i[1]))
            btm_arr_1.append(float(i[2]))
        j = 1

best_fit_btm = poly.polyfit(btm_arr_0, btm_arr_1, 100)
plt.plot(btm_arr_1, btm_arr_0, 'o')

trend_poly = np.poly1d(best_fit_btm)
plt.plot(btm_arr_1, trend_poly(btm_arr_1))


def interpolate_btm(a):
    best_fit_btm = poly.polyfit(btm_arr_0, btm_arr_1, 100)
    return poly.polyval(a, best_fit_btm)

# print(interpolate_btm(85))

# print(best_fit_btm)
# print(type(best_fit_btm))