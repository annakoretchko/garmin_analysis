import pandas as pd

import garmin_analysis.utils.get_data_utils as get_data_utils


def run(data_path):
    """[This takes int he argument for the data path and transforms it into
    a df. It also cleans and parses the data for analysis]

    Args:
        data_path ([str]): [path to location of csv data file]

    Returns:
        [df]: [returns a df that has been parsed, cleaned and ready for visua]ization
    """


    # reads in data path of csv to dataframe 
    df = pd.read_csv(data_path)

    # subset and rename cols
    df = get_data_utils.rename_cols(df)

    # remove units from df
    df = get_data_utils.remove_units(df)

    # convert astype for each column to appropriate type
    df = get_data_utils.convert_type(df)


    return df
   