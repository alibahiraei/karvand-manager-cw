import numpy as np

"""
song = np.array([0.7, 0.9, 0.6])
user_taste = np.array([0.6, 0.8, 0.5])
elemenwise=song*user_taste
print(f" elementwise {elemenwise}")
dotproduct=song@user_taste
print(f"docproduct {dotproduct}")
b=.3
y=(song@user_taste)+b
print(y)"""
######################################################
"""song1 = np.array([0.9, 0.1])
song2 = np.array([0.85, 0.15])
song3 = np.array([-0.9, -0.1])

cosin_similarty_1_2=(song1@song2)/np.linalg.norm(song1)*np.linalg.norm(song2)
cosin_similarty_1_3=(song1@song3)/np.linalg.norm(song1)*np.linalg.norm(song3)
cosin_similarty_2_3=(song2@song3)/np.linalg.norm(song2)*np.linalg.norm(song3)
print(f"song1_2-->{cosin_similarty_1_2}")
print(f"song1_3->{cosin_similarty_1_3}")
print(f"song2_3->{cosin_similarty_2_3}")"""
###########################################################
# سوال 4 بخش یکم
"""songs=np.array([
    [.9, .1,.8],
    [.85, .15,.7],
    [-.9, -.1,-.3],
    [.25,.14,.89],
    [.45,.32,.36]
])
user_taste = np.array([0.6, 0.8, 0.5])

y=songs@user_taste
print(y)"""
##############################################################
stats = np.random.rand(4, 3)
print(stats)
print("-------------------------------------------")
skill_matrix = np.random.rand(3, 5)
print(skill_matrix)
print("------------------------------------------")
y=stats@skill_matrix
print(y)
######################################################
X_chars = np.array([
[80, 40, 60],
[30, 90, 50],
[70, 70, 70],
[95, 20, 40]
])

W_skills = np.random.randn(3, 3)
b_skills = np.array([1.0, -0.5, 0.2])
Z = X_chars @ W_skills + b_skills

