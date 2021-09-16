import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy import stats
import numpy as np



def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']
    
     # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    plt.plot(x, y, 'o', label='original data')
    plt.plot(x, intercept + slope*x, 'y', label='fitted line')
    #plt.xlim(1880,2050)
    #plt.xlable("Year")
    #plt.ylable('Sea Level (inches)')
    plt.title('Rise in sea level')
    plt.legend()
    
      # Create second line of best fit
    x2=df["Year"][df["Year"] >= 2000]
    y2=df.loc[(df["Year"] >= 2000), "CSIRO Adjusted Sea Level"]
    xi=np.arange(x2.min(),2050,1)
    slope, intercept, r_value, p_value, std_err = linregress(x2,y2)
    plt.plot(xi, intercept + slope*xi, 'o')


    # Add labels and title
    ax = plt.gca()
    ax.set(xlabel = "Year", ylabel = "Sea Level (inches)", title = "Rise in Sea Level", xticks=[1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])


    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
