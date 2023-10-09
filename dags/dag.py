from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash_operator import BashOperator

with DAG(dag_id='meu_primeiro_dag',start_date=days_ago(1),schedule_interval= '@daily') as dag: 
    tarefa1 = EmptyOperator(task_id='tarefa_1')
    tarefa2 = EmptyOperator(task_id='tarefa_2')
    tarefa3 = EmptyOperator(task_id='tarefa_3')
    tarefa4 = BashOperator(
        task_id='Cria_pasta',
        bash_command='mkdir -p "D:/MATEUS/Documentos/repos/alura-weather-api/pasta" ')

    tarefa1 >> tarefa2 >> tarefa3 >> tarefa4