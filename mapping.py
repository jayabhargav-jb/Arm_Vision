import csv
import numpy as np

with open("btm.csv", "r") as btm:
    reader_obj = csv.reader(btm)
    btm_arr_0 = list()
    btm_arr_1 = list()
    j = 0
    for i in reader_obj:
        if j != 0:
            btm_arr_0.append(int(i[1]))
            btm_arr_1.append(int(i[2]))
        j = 1

best_fit_btm = np.polyfit(btm_arr_0, btm_arr_1, 5)

print(type(best_fit_btm))