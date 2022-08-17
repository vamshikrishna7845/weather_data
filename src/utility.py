import pandas as pd
import glob
import os
from django.conf import settings
from sqlalchemy import create_engine
from datetime import datetime


def execution_time(main_func):
    def timer_func(frame, table, engine):
        strt_time = datetime.now()
        print("starting time is ", strt_time)
        entries = main_func(frame, table, engine)
        end_time = datetime.now()
        print("end time is ", end_time)
        print("total number of enrties ingested ", entries)
    return timer_func


def prepare_data_weather_files(path):
    all_files = glob.glob(os.path.join(path, "*.txt"))
    li = []

    for filename in all_files:
        base_file = os.path.basename(filename)
        file_name = os.path.splitext(base_file)[0]
        df = pd.read_csv(filename, sep='\t', header=None)
        df.columns = ["date", "max_temp", "min_temp", "precipitation"]
        df['weather_station'] = file_name
        li.append(df)
    frame = pd.concat(li)
    return frame


def prepare_data_crop_file(path):
    filename = path
    df = pd.read_csv(filename, sep='\t', header=None)
    df.columns = ["year", "qty_harvested"]
    return df


def make_connection():
    user = settings.DATABASES['default']['USER']
    password = settings.DATABASES['default']['PASSWORD']
    database_name = settings.DATABASES['default']['NAME']
    # host = settings.DATABASES['default']['HOST']
    # port = settings.DATABASES['default']['PORT']

    database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(
        user=user,
        password=password,
        database_name=database_name,
    )

    engine = create_engine(database_url, echo=False)

    return engine


@execution_time
def push_data(frame, table, engine):
    entires = frame.to_sql(table, engine, if_exists='append', index=False)
    return entires


def read_sql(table_name, engine):
    df = pd.read_sql_table(table_name, engine)
    return df
