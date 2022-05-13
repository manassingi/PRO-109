import random

import plotly.figure_factory as ff
import plotly.express as px
import statistics
import pandas as pd
import plotly.graph_objects as go
import csv
result=[]
df = pd.read_csv("data.csv")
data = df["reading score"].tolist()
result.append(data)

mean = statistics.mean(data)
median =statistics.median(data)
mode = statistics.mode(data)
sd = statistics.stdev(data)

print(mean)

print(median)
print(mode)
print(sd)
first_std_deviation_start, first_std_deviation_end = mean-sd, mean+sd
second_std_deviation_start, second_std_deviation_end = mean-(2*sd), mean+(2*sd)
third_std_deviation_start, third_std_deviation_end = mean-(3*sd), mean+(3*sd)
list1=[result for result1 in data if result1 > first_std_deviation_start and result1 < first_std_deviation_end]
list2=[result for result1 in data if result1 > second_std_deviation_start and result1 < second_std_deviation_end]
list3=[result for result1 in data if result1 > third_std_deviation_start and result1 < third_std_deviation_end]
print(result)
print("{}% of data lies within 1 standard deviation".format(len(list1)*100.0/len(result)))
print("{}% of data lies within 1 standard deviation".format(len(list2)*100.0/len(result)))
print("{}% of data lies within 1 standard deviation".format(len(list3)*100.0/len(result)))

fig= ff.create_distplot([data],["Score"])

fig.add_trace(go.Scatter(x=[first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1")) 
fig.add_trace(go.Scatter(x=[first_std_deviation_end ], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1")) 
fig.add_trace(go.Scatter(x=[second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2")) 
fig.add_trace(go.Scatter(x=[second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))

fig.show()
