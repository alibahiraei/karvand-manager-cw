import numpy as np
import csv
import json

rows=[]

with open("citiy.csv","r",encoding="utf-8") as file:   #city,avg_temp,humidity,popularity,cost_index
    reader=csv.DictReader(file)
    for row in reader:
        try:
            member=[float(row["avg_temp"]),
                     float(row["humidity"]),
                     float(row["popularity"]),
                     float(row["cost_index"])]
            
            rows.append({"citiy":row["city"],"featur":member})
        except ValueError :
             print(f"ignoring {row['city']}")
#print(rows)
city_list=[i["citiy"] for i in rows]
data=np.array([i["featur"] for i in rows])
featurs=data.T
"""print(featurs)
print(city_list)
print(data)"""
################################################## 
#سوال یک از بخش کاوش و مقایسه بندی
"""print(f"mean featur -->{np.mean(featurs,axis=1)}")
print(f"max featur -->{np.max(featurs,axis=1)}")
print(f"min featur -->{np.min(featurs,axis=1)}")
print(f"standaed devaitoin featur -->{np.std(featurs,axis=1)}")"""
###############################################
#سوال دوم از بخش کاوش و مقایسه بندی
min_val=np.min(featurs,axis=1,keepdims=True)
max_val=np.max(featurs,axis=1,keepdims=True)
scaled_data=(featurs-min_val)/(max_val-min_val)
"""print("min scaled--->",(min_val))
print("max scaled--->",(max_val))
print("data scaled--->",(scaled_data)"""
###################################################
#اسکالن کردن دیتا با داده جدید
new_data=np.array([26,40,8,4])
scal_new = (new_data.reshape(-1, 1) - min_val) / (max_val - min_val)
#print("scal_new_ data",(scal_new))
###################################################
"""best_euclidean_idx = np.argmin(min_val)
print(city_list[best_euclidean_idx])"""
###################################################

"""temps=np.array([
    [19,21,24,22],    #دوشنبه
    [24,23,27,25,],   #سه شنبه
    [17,18,19,20]     #چهارشنبه
])
maen_day_1=np.mean(temps,axis=1)
print(maen_day_1)
maen_temps=np.mean(temps,axis=0)
print(maen_temps)

avrag_ditanc=temps-maen_day_1
print(avrag_ditanc)"""
##########################################
image = np.array([
[10, 20, 30, 40, 50],
[15, 25, 35, 45, 55],
[20, 30, 40, 50, 60],
[25, 35, 45, 55, 65],
[30, 40, 50, 60, 70]
])
center=image[1:4,1:4]
##################################################
"""quiz_scores = np.array([45, 78, 92, 60, 55, 88, 30])

c=np.where()"""
#################################################
prices = np.array([100, 102, 98, 105, 110, 107, 115])

daily_returns = (prices[1:] - prices[:-1]) / prices[:-1] * 100
print(daily_returns.std())

print(prices[1:])
print(prices[:-1])
max_maen=np.argmax(prices)+1
print(max_maen)








