import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# IMPORT DATA
df = pd.read_csv("medical_examination.csv")

# CLEAN THE DATA
df = df[(df["ap_lo"] <= df["ap_hi"]) & 
        (df["height"] >= (df["height"].quantile(0.025))) &
        (df["height"] <= (df["height"].quantile(0.975))) &
        (df["weight"] >= (df["weight"].quantile(0.025))) &
        (df["weight"] <= (df["weight"].quantile(0.975)))]

# ADD OVERWEIGHT COLUMN
# The height in the df is given in cm amd the formula for the bmi calculation requires for it to be in m.
bmi_calc = df.weight/((df.height/100)**2)
df['overweight'] = np.where(bmi_calc > 25, 1, 0)

# NORMALIZE DATA by making 0 always good and 1 always bad.
bad_categories = ["cholesterol", "gluc"]
for cat in bad_categories:
    df[cat] = np.where(df[cat] == 1, 0, 1)


# Draw Categorical Plot

def draw_cat_plot():
    # Convert the data into long format
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"])

    # Get the figure for the output
    fig = sns.catplot(data=df_cat, kind="count",  x="variable", hue="value", col="cardio")
    fig.set_axis_labels("variable", "total")

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig.figure


# Draw Heat Map
# TODO Create a correlation matrix using the dataset. Plot it using seaborn's "heatmap()"
# Mask the upper triangle. The chart should look like Fig_2 in the examples.

def draw_heat_map():
    # Clean the data
    # Setting df_heat as df as I had already cleaned the data with the filters requested
    df_heat = df

    # Calculate the correlation matrix
    corr = df_heat.corr(method="pearson")

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 12))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, cmap="icefire", annot=True, fmt='0.1f', linewidths=1, 
                mask=mask, square=True)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
