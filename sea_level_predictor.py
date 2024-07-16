#STEP-1: Import the Data and Prepare Environment
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

#Import data using Pandas
df = pd.read_csv('epa-sea-level.csv')


#STEP-2: Create Scatter Plot with Linear Regression
#Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', marker='o', alpha=0.6)

#Perform linear regression to get slope and intercept
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

#Predict sea level change till 2050
years_future = range(1880, 2051)
plt.plot(years_future, intercept + slope * years_future, 'r-', label='Linear Fit Full Data')

#Plot new line of best fit from year 2000 onwards
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
plt.plot(years_future, intercept_recent + slope_recent * years_future, 'g-', label='Linear Fit Recent Data')

#Set labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

#Save and return the plot
plt.savefig('sea_level_plot.png')
plt.show()

