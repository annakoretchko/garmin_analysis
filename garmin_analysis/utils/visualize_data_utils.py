
import matplotlib.pyplot as plt
import os
import sys

def create_line_graph_month_distance(df,output_path, show = False):
    """[Creates a line graph from the df and saves to outputs folder]

    Args:
        df ([df]): [df containing all cleaned data]
        output_path ([str]): [path to output folder to save images and results]
        show (bool, optional): [Flag, if set to true will render image]. Defaults to False.
    """
    
    # created graph
    df.plot.line(x ='Month',y = 'Average_Distance',title='Mean Distance Over Time', ylabel='Distance (mi)',
         xlabel='Month', figsize=(6, 5))

    # displays if true
    if show:
        plt.show()
    
    # saves to output folder
    fname = "line_graph_month_distance.png"
    pout = os.path.join(output_path,fname)
    plt.savefig(pout)


def create_combo_chart_all(df, output_path, show = False):
    """[Creates a combo chart  from the df and saves to outputs folder]

    Args:
        df ([df]): [df containing all cleaned data]
        output_path ([str]): [path to output folder to save images and results]
        show (bool, optional): [Flag, if set to true will render image]. Defaults to False.
    """
    
    # groups data
    df = df.groupby(['Year']).mean()

    df.plot(kind='bar', title='Average Metric Values by Year', ylabel='Mean Values',
         xlabel='Year', figsize=(6, 5))

    # shows if true
    if show:
        plt.show()
    
    # saves image to output folder
    fname = "combo_chart_all.png"
    pout = os.path.join(output_path,fname)
    plt.savefig(pout)


def create_line_HR_cadence(df, output_path, show = False):
    """[Creates a line graph of HR and cadence from the df and saves to outputs folder]

    Args:
        df ([df]): [df containing all cleaned data]
        output_path ([str]): [path to output folder to save images and results]
        show (bool, optional): [Flag, if set to true will render image]. Defaults to False.
    """

    # subsets data and groups it
    df = df[['Year','Average_Heart_Rate','Average_Run_Cadence']]
    df.groupby(['Year']).mean().plot(legend=True, title='Average HR and Cadence Over Years', ylabel='Mean Metric',
         xlabel='Year', figsize=(6, 5))
    

 
    # show image if true
    if show:
        plt.show()
    
    # saves image to output folder
    fname = "line_HR_cadence.png"
    pout = os.path.join(output_path,fname)
    plt.savefig(pout)


def create_line_speed_distance(df, output_path, show = False):
    """[Creates a line graph of speed and distance from the df and saves to outputs folder]

    Args:
        df ([df]): [df containing all cleaned data]
        output_path ([str]): [path to output folder to save images and results]
        show (bool, optional): [Flag, if set to true will render image]. Defaults to False.
    """

    # subsets data and groups it
    df = df[['Year','Average_Speed','Average_Distance']]
    df.groupby(['Year']).mean().plot(legend=True, title='Average Speed and Distance Over Years', ylabel='Mean Values',
         xlabel='Year', figsize=(6, 5))
    
    # show image if true
    if show:
        plt.show()

    # saves image to output folder
    fname = "line_speed_distance.png"
    pout = os.path.join(output_path,fname)
    plt.savefig(pout)


def create_combo_chart_by_distance(df, output_path, show = False):
    """[Creates a line graph from the df and saves to outputs folder]

    Args:
        df ([df]): [df containing all cleaned data]
        output_path ([str]): [path to output folder to save images and results]
        show (bool, optional): [Flag, if set to true will render image]. Defaults to False.
    """
    
    # subsets data and groups it
    df = df.round(0)
    df = df.groupby(['Average_Distance']).mean()
    df = df.round(1)

    # plots it
    df.plot(kind='bar', title='Average Metrics By Distance Ran', ylabel='Mean Values',
         xlabel='Distance Ran (mi)', figsize=(6, 5))
    
 
    # show image if true
    if show:
        plt.show()
    
    # saves image to output folder
    fname = "combo_chart_by_distance.png"
    pout = os.path.join(output_path,fname)
    plt.savefig(pout)