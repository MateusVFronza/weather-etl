from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.decorators import dag, task
from airflow.models import Variable
import pendulum
import os
from datetime import datetime, timedelta
import pandas as pd
from utils.classes import weather
import json

key = Variable.get("key") # The token obtained by the application website
city = Variable.get("city") # Target city: Florianopolis 
 # 
# '0 8 * * *' → daily at 8am
with DAG(
    dag_id='weather_forecast',
    start_date=pendulum.datetime(2023,9,28, tz = 'UTC'),
    schedule_interval= '0 8 * * *') as dag: 
 
    forecast = weather(city,key)

    forecast_dates = PythonOperator(
        task_id= 'get_dates',
        python_callable= forecast.dates
    )

    forecast_requests = PythonOperator(
        task_id = 'requests',
        python_callable=forecast.request
    )
    forecast_turn_into_dataframe = PythonOperator(
        task_id= 'turn_into_a_df',
        python_callable= forecast.turn_into_df
    )

    preview_df = PythonOperator(
        task_id= 'preview',
        python_callable= forecast.df_preview
    )
    forecast_export_the_df = PythonOperator(
        task_id= 'export',
        python_callable= forecast.export_df
    )

    forecast_dates >> forecast_requests >> forecast_turn_into_dataframe >> preview_df >> forecast_export_the_df


#
