#STEP-1: Importing and Cleaning Data

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Step 1: Import data and set index to date column
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Step 2: Clean the data by filtering out days with page views in the top 2.5% or bottom 2.5%
df_clean = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

#STEP-2: Draw Line Plot Function
def draw_line_plot():
    # Copy and modify data for plotting
    df_plot = df_clean.copy()

    # Create a new column for year and month
    df_plot['year'] = df_plot.index.year
    df_plot['month'] = df_plot.index.month
    df_plot['month_name'] = df_plot.index.strftime('%B')  # Convert month number to month name

    # Group by year and month to get average page views
    df_plot = df_plot.groupby(['year', 'month', 'month_name']).mean()
    df_plot.reset_index(inplace=True)

    # Set up the matplotlib figure and plot
    fig, ax = plt.subplots(figsize=(14, 6))
    sns.lineplot(x='year', y='value', hue='month_name', data=df_plot, ax=ax, linewidth=2.5)

    # Add labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save the plot image
    fig.savefig('line_plot.png')

    # Return the figure
    return fig

#STEP-3: Draw Bar Plot Function
def draw_bar_plot():
    # Copy and modify data for plotting
    df_plot = df_clean.copy()

    # Create a new column for year and month
    df_plot['year'] = df_plot.index.year
    df_plot['month'] = df_plot.index.month
    df_plot['month_name'] = df_plot.index.strftime('%B')  # Convert month number to month name

    # Group by year and month to get average page views
    df_plot = df_plot.groupby(['year', 'month', 'month_name']).mean()
    df_plot.reset_index(inplace=True)

    # Pivot the dataframe for plotting
    df_pivot = df_plot.pivot(index='year', columns='month_name', values='value')
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    df_pivot = df_pivot.reindex(columns=month_order)

    # Set up the matplotlib figure and plot
    fig, ax = plt.subplots(figsize=(14, 6))
    df_pivot.plot(kind='bar', ax=ax)

    # Add labels and title
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_title('Average Page Views per Month (Year-wise)')

    # Add legend with month labels
    ax.legend(title='Months', labels=month_order)

    # Save the plot image
    fig.savefig('bar_plot.png')

    # Return the figure
    return fig

#STEP-4: Draw Box Plot Function
def draw_box_plot():
    # Prepare data for plotting
    df_box = df_clean.copy()

    # Extract year and month
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box['date']]
    df_box['month'] = [d.strftime('%b') for d in df_box['date']]

    # Sort by month order
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box = df_box.sort_values(by='date')
    df_box['month'] = pd.Categorical(df_box['month'], categories=month_order, ordered=True)

    # Initialize matplotlib figure
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 6))

    # Plot Year-wise Box Plot
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[0].set_title('Year-wise Box Plot (Trend)')

    # Plot Month-wise Box Plot
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=month_order)
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save the plot image
    fig.savefig('box_plot.png')

    # Return the figure
    return fig
