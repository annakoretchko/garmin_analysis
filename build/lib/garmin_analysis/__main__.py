
import garmin_analysis.main_utils as main_utils
import garmin_analysis.get_data.get_data as get_data
import garmin_analysis.visualize_data.visualize_data as visualize_data
import os
import sys
from datetime import datetime as date


def main():
    
    args = main_utils.main_argparser()
    main_utils.set_env_variables(args)

    print("Initiate Program" , date.now())
    # gets the data and cleans it
    df = get_data.run(os.environ['data_path'])


    # visualizes the data
    visualize_data.run(df, os.environ['output_path'])

    print("Program Completed", date.now())






if __name__ == '__main__':
    main()