from django.http import HttpResponse
from psycopg2 import IntegrityError
from src.utility import prepare_data_weather_files, make_connection, push_data, prepare_data_crop_file


def ingest_weather_data():
    path = r'/Users/vamshi/Desktop/vamshi exercise/code-challenge-template/wx_data'  # use your path
    data_frame = prepare_data_weather_files(path)
    makr_connection = make_connection()
    try:
        push_data(data_frame, 'crop_predictor_weatherdata', makr_connection)
    except IntegrityError:
        return HttpResponse("Duplicate Entries found")


def ingest_yield_data():
    path = r'/Users/vamshi/Desktop/vamshi exercise/code-challenge-template/yld_data/US_corn_grain_yield.txt'
    data_frame = prepare_data_crop_file(path)
    makr_connection = make_connection()
    try:
        push_data(data_frame, 'crop_predictor_yielddata', makr_connection)
    except IntegrityError:
        return HttpResponse("Duplicate Entries found")
