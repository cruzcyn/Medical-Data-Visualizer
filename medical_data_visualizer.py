import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# TODO Clean the data. Filter out the following patient segments that represent incorrect data:
# where diastolic pressure > systolic pressure
df = df[df["ap_lo"] <= df["ap_hi"]]

# height > 97.5th percentile
height_percentile = np.percentile(df.height, 97.5)
df = df[df.height < height_percentile]

# weight < 2.5th percentile and  weight > 97.5th percentile
weight_low_percentile = np.percentile(df.weight, 2.5)
weight_high_percentile = np.percentile(df.weight, 97.5)
df = df[(df.weight > weight_low_percentile) & (df.weight < weight_high_percentile)]


# TODO Add 'overweight' column. Calculate BMI (weight/height**2 in meters)
# If BMI > 25, then overweight = 1 (so, yes), else overweight = 0
df['overweight'] = None

# TODO Normalize data by making 0 always good and 1 always bad. 
# If the value of 'cholesterol' or 'gluc' is 1, make the value 0. 
# If the value is more than 1, make the value 1.


# Draw Categorical Plot
# TODO Convert data into long format and create a chart that shows the value counts
# of the categorical features (so, what's written in the next comment) using seaborn's
# catplot().
# The dataset should be split by "Cardio" so there is one chart for each "cardio" value.
# This chart should look like the one in examples/Figure_1.png

def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 
    #'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = None


    # Group and reformat the data to split it by 'cardio'. Show the counts of each 
    # feature. You will have to rename one of the columns for the catplot to work 
    # correctly.
    df_cat = None
    

    # Draw the catplot with 'sns.catplot()'



    # Get the figure for the output
    fig = None


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
# TODO Create a correlation matrix using the dataset. Plot it using seaborn's "heatmap()"
# Mask the upper triangle. The chart should look like Fig_2 in the examples.

def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
