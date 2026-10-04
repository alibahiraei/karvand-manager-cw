import numpy as np
import random

a=np.array([[1,2],
            [3,4]])

sum_asis_0=np.sum(a,axis=0)

sum_asis_1=np.sum(a,axis=1)

print(f"sum_axis_0 {sum_asis_0}")
print(f"sum_axis_1 {sum_asis_1}")

"""x=np.array([[12,20,85,66],
            [55,33,100,77],
            [88,23,45,41],
            [140,180,99,400]])

print("even row",x[0:5:2,:])
print("even row",x[0:5:2])
print("last cloum",x[:,-1])
print(" odd clo",x[:,1:5:2])
print("daraye row 3 cloum 2",x[3,2])"""




