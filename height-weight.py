import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import csv
import pandas as pd

data = pd.read_csv(r"C:\Users\bhuvi\Google Drive\Code\Python\Class 108 - Bell Curve\data.csv")
height = data["Height(Inches)"].tolist()
weight = data["Weight(Pounds)"].tolist()

mean_h = sum(height) / len(height)
mean_w = sum(weight) / len(weight)
print("Mean of Height is {} and Weight is {}".format(mean_h,mean_w))

std_h = statistics.stdev(height)
std_w = statistics.stdev(weight)
print("Standard Deviation of Height is {} and Weight is {}".format(std_h,std_w))

first_start_h = mean_h - std_h
first_end_h = mean_h + std_h
second_start_h = mean_h - (2*std_h)
second_end_h = mean_h + (2*std_h)
third_start_h = mean_h - (3*std_h)
third_end_h = mean_h + (3*std_h)

first_start_w = mean_w - std_w
first_end_w = mean_w + std_w
second_start_w = mean_w - (2*std_w)
second_end_w = mean_w + (2*std_w)
third_start_w = mean_w - (3*std_w)
third_end_w = mean_w + (3*std_w)

first_h = [h for h in height if h > first_start_h and h < first_end_h]
second_h = [h for h in height if h > second_start_h and h < second_end_h]
third_h = [h for h in height if h > third_start_h and h < third_end_h]

first_w = [w for w in weight if w > first_start_w and w < first_end_w]
second_w = [w for w in weight if w > second_start_w and w < second_end_w]
third_w = [w for w in weight if w > third_start_w and w < third_end_w]

print(" ")
print("Height that lies in the first standard deviation = {} %".format((len(first_h)*100)/len(height)))
print("Height that lies in the second standard deviation = {} %".format((len(second_h)*100)/len(height)))
print("Height that lies in the third standard deviation = {} %".format((len(third_h)*100)/len(height)))
print(" ")
print("Weight that lies in the first standard deviation = {} %".format((len(first_w)*100)/len(weight)))
print("Weight that lies in the second standard deviation = {} %".format((len(second_w)*100)/len(weight)))
print("Weight that lies in the third standard deviation = {} %".format((len(third_w)*100)/len(weight)))