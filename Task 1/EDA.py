import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 
import plotly.express as px
import seaborn as sns
import plotly.graph_objects as go
import math
from plotly.subplots import make_subplots
from numpy import linalg as LA


def multiple_histogram(data):
    
    num_row = math.ceil(len(data.columns) / 3)
    fig = make_subplots(rows=num_row, cols=3,subplot_titles=(data.columns))

    place_col = 1
    place_row = 1
    for i in data.columns:

        fig.add_trace(go.Histogram(x=data[i]),row=place_row, col=place_col)

        place_col += 1
        if place_col == 4:
            place_col = 1
            place_row += 1
    return fig.update_layout(height=1600, width=1100,title_text="Multiple Histogram for all featrues")



def multiple_boxplot(data):
    
    num_row = math.ceil(len(data.columns) / 3)
    fig = make_subplots(rows=num_row, cols=3,subplot_titles=(data.columns))

    place_col = 1
    place_row = 1
    for i in data.columns:

        fig.add_trace(go.Box(y=data[i]),row=place_row, col=place_col)

        place_col += 1
        if place_col == 4:
            place_col = 1
            place_row += 1
    return fig.update_layout(height=1600, width=1100,
                          title_text="Multiple Histogram for all featrues")

def split_name(X_data, separator):
    
    for i in range(len(X_data.columns)):

        if  separator in X_data.columns[i]:

            new_name = X_data.columns[i].split(separator)[1]
            X_data.rename(columns={X_data.columns[i]:new_name}, inplace=True)
            
def check_nulls(X_data):
    
    unusual_nulls = X_data[X_data.isin(['{}','[]', "?", ".", "-", "_", "", " ", "  "])].sum()

    nulls_df = pd.concat([X_data.isna().sum(), unusual_nulls], axis=1)
    nulls_df.columns = ["usual_nulls", "strange_nulls"]
    nulls_df = nulls_df.sort_values('usual_nulls', ascending = False)
    return nulls_df
