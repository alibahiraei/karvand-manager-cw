import numpy as np


"""scores=[72,85,90,66,78]
scores=np.array(scores)
print("dtype:", scores.dtype)
print("size:", scores.size)
print("shape:", scores.shape)
print("ndim:", scores.ndim)"""

"""grad=[
    [12,25,13,14],
    [20,14,18,19],
    [15,16,17,19]
]
"""
"""a=np.array([3,6,9])
b=np.array([1,2,3])
c=np.array([.5,.5,.5])

print("sum:", a + b)
print("difference:", a - b)
print("elementwise multiplication:", a * b)
print("a * 0.5:", a * 0.5)
print(a*c)
print(a.shape)"""
m=np.array([
    [80,70,90],
    [60,85,75],
    [95,60,80],
    [70,70,70]

])

weights=np.array([.5,.3,.2])

result=np.dot(m,weights)
result_a=np.sum(m*weights, axis=1)
print(result_a)

print(result)
"""print(result.shape)
print(type(result))"""