import numpy as np


og_arr = np.array([
    [0,1,2,3,4,5],
    [10,11,12,13,14,15],
    [20,21,22,23,24,25],
    [30,31,32,33,34,35],
    [40,41,42,43,44,45],
    [50,51,52,53,54,55]
])


pink_subarray = og_arr[1, 2:4]


green_subarray = og_arr[2:4, 4:6]


blue_subarray = og_arr[:, 1:2]


orange_subarray = og_arr[[2, 4], :5:2]

print("Pink sub-array:\n", pink_subarray)
print("Green sub-array:\n", green_subarray)
print("Blue sub-array:\n", blue_subarray)
print("Orange sub-array:\n", orange_subarray)
