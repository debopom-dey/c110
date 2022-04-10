import plotly.figure_factory as ff
import statistics as st
import random
import pandas as pd

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean=st.mean(data)
print("population mean:- ",population_mean)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean

def show_fig(mean_list):
    fig = ff.create_distplot([mean_list], ["reading_time"], show_hist=False)
    fig.show()
    mean=st.mean(mean_list)
    print("Mean of sampling distribution = ",mean)

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
setup()