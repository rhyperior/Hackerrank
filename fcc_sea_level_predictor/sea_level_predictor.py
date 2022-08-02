import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv(r'./fcc_sea_level_predictor/epa-sea-level.csv')
    
    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], c='blue', s=3)
    
    # Create first line of best fit
    line = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    for year in range(2014, 2051):
        df.loc[len(df.index)] = [year,0,0,0,0]

    plt.plot(df['Year'], line.intercept + line.slope*df['Year'], color='red', label='Best Fit')
    # plt.legend()
    # Create second line of best fit
    line_2 = linregress(df.iloc[120:134]['Year'], df.iloc[120:134]['CSIRO Adjusted Sea Level'])

    plt.plot(df.iloc[120:]['Year'], line_2.intercept + line_2.slope*df.iloc[120:]['Year'], color='orange', label='Second Best Fit')
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png', dpi=500)

    return plt.gca()

# if __name__=="__main__":
#     draw_plot()