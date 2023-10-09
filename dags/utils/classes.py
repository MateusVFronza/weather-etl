from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.decorators import dag, task
from airflow.models import Variable
import os
from os.path import join
from datetime import datetime, timedelta
import pandas as pd
import json


class weather():
    def __init__(self,city,key):
        self.city = city
        self.key = key
        self.first_date = None
        self.last_date = None
        self.first_date_str = None
        self.last_date_str = None
        self.url = None
        # self.df = None

    
    def dates(self,ti):
        self.first_date = datetime.today()
        self.last_date = self.first_date + timedelta(days = 7)
        self.first_date_str = self.first_date.strftime('%Y-%m-%d') 
        self.last_date_str = self.last_date.strftime('%Y-%m-%d') 
        
        
        ti.xcom_push(key='extract_date', value= self.first_date)
        ti.xcom_push(key='first_date', value= self.first_date_str)
        ti.xcom_push(key='last_date', value=self.last_date_str)
    
    def request(self,ti):
        self.first_date_str = ti.xcom_pull(key='first_date', task_ids='get_dates')
        self.last_date_str = ti.xcom_pull(key='last_date', task_ids='get_dates')

        self.url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{self.city}/{self.first_date_str}/{self.last_date_str}?key={self.key}&contentType=csv&include=days'
        
        ti.xcom_push(key='url', value=self.url)

        print(self.url,'\nDone!')

    def turn_into_df(self,ti):
        self.df = pd.read_csv(ti.xcom_pull(key='url', task_ids='requests'))
        
        self.df['extract_date'] = ti.xcom_pull(key='extract_date', task_ids='get_dates') 

        return self.df

    def df_preview(self,ti):
        df = ti.xcom_pull(task_ids = 'turn_into_a_df')
        return df.head(3)

    def export_df(self,ti):
        df = ti.xcom_pull(task_ids = 'turn_into_a_df')
        df.to_csv(f'/opt/airflow/data/forecast-{ti.xcom_pull(key="first_date", task_ids="get_dates")}')
        print('Done')
