import numpy as np
import pandas as pd
from src.utility import make_connection, read_sql, push_data


def get_statistics_data():
    make_conn = make_connection()
    table_name = 'crop_predictor_weatherdata'
    frame = read_sql(table_name, make_conn)
    frame = frame.replace(-9999, np.nan)
    frame['date_time'] = pd.to_datetime(frame['date'], format='%Y%m%d')
    frame['year'] = pd.DatetimeIndex(frame['date_time']).year
    frame.drop('id', axis=1, inplace=True)
    frame.drop('date', axis=1, inplace=True)
    frame_average = frame.groupby(['weather_station', 'year']).mean().reset_index()
    frame_average['max_temp'] = frame_average['max_temp'].apply(lambda x: x/10)
    frame_average['min_temp'] = frame_average['min_temp'].apply(lambda x: x/10)
    frame_average['precipitation'] = frame_average['precipitation'].apply(lambda x: x/100)
    return frame_average


def push_statistics_data_to_sql():
    table_name = 'crop_predictor_statisticsdata'
    data_frame = get_statistics_data()
    make_conn = make_connection()
    push_data(data_frame, table_name, make_conn)