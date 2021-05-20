
import garmin_analysis.utils.visualize_data_utils as visualize_data_utils
import matplotlib.pyplot as plt



def run(df,output_path):
    """[Different functions that render different graphs for analysis]

    Args:
        df ([df]): [df contaiing all cleaned data]
        output_path ([df]): [path to output folder to save images and results]
    """

    # creates and saves a line graph
    visualize_data_utils.create_line_graph_month_distance(df,output_path)

    # combo chart all
    visualize_data_utils.create_combo_chart_all(df,output_path)

    # combo chart by distance
    visualize_data_utils.create_combo_chart_by_distance(df,output_path)

    # line chart HR_cadence
    visualize_data_utils.create_line_HR_cadence(df,output_path)

    # line chart HR_cadence
    visualize_data_utils.create_line_speed_distance(df,output_path)

