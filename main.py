import csv 
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics
import random

df=pd.read_csv("articles.csv")
data=df["reading_time"].tolist()
population_mean=statistics.mean(data)
population_stdev=statistics.stdev(data)

print("Population mean:",population_mean )
print("Population stdev",population_stdev)


def random_set_mean(counter):
    dataset=[]
    for i in range(1,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df=mean_list 
    mean=statistics.mean(mean_list)
    stdev=statistics.stdev(mean_list)
    print("Sample mean:", mean)
    print("Sample stdev:", stdev)   
    fig=ff.create_distplot([df],['reading_time'],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1], mode="lines", name="MEAN"))
    fig.show()

def setup():
    mean_list=[]
    for i in range(100):
        set_of_means=random_set_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)

setup()
