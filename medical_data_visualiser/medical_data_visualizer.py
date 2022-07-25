import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv(r'./medical_data_visualiser/medical_examination.csv')





# # Draw Categorical Plot
def draw_cat_plot():
    # df = data
        # Add 'overweight' column
    BMI = df['weight'] / (df['height'] * df['height']) * 10000
    df['overweight'] = BMI.apply(lambda x : 1 if x > 25 else 0)

    # print(df.head())
    # Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
    if len(list(df['cholesterol'].unique())) > 2:
        df['cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0 )
        df['gluc'] = df['gluc'].apply(lambda x: 1 if x > 1 else 0 )
    # data = df
    # # df1 = df.query('cardio == 0')
    # # df2 = df.query('cardio == 1')
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.

    df_cat = pd.melt(df, value_vars = ['gluc', 'smoke', 'active', 'alco', 'cholesterol', 'overweight'], id_vars = ['cardio'])

    g = sns.catplot(data = df_cat, x = 'variable', kind = 'count', hue = 'value', col = 'cardio', order = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])
    g.set_ylabels('total')
    print(dir(g))
    g = g.figure

    
     

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    # df_cat = None

    # Draw the catplot with 'sns.catplot()'



    # Do not modify the next two lines
    g.savefig('catplot.png')
    return g


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    global df

   
    df_heat = df[ (df['ap_lo'] <= df['ap_hi']) &
                  (df['height'] >= df['height'].quantile(0.025)) &
                  (df['height'] <= df['height'].quantile(0.975)) &
                  (df['weight'] >= df['weight'].quantile(0.025)) &
                  (df['weight'] <= df['weight'].quantile(0.975))]

    
    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones(corr.shape)).astype(bool)

    # Set up the matplotlib figure
    plt.figure(figsize=(15, 15))

     # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(corr, mask=mask, annot=True, fmt = '.1f', cbar_kws = {'ticks': [-0.08, 0.00, 0.08, 0.16, 0.24]}, center = 0.0, vmin= -0.16, vmax = 0.32, linewidth = 0.75)
    fig = ax.get_figure()


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig


if __name__=="__main__":
    draw_cat_plot()
    draw_heat_map()