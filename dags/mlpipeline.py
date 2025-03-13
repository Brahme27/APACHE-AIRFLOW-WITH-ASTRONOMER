from airflow import DAG 
from airflow.operators.python import PythonOperator
from datetime import datetime

#define the task 1 
def preprocess_data():
    print("Data preprocessing is done.....")

##define the task 2
def train_model():
    print("Model training is done.....")

## define our task 3 
def evaluate_model():
    print("Model evaluation is done.....")

# define the DAG
with DAG(dag_id='ml_pipeline',start_date=datetime(2025, 3, 13),schedule_interval='@weekly') as dag:
    
    # define the task
    preprocess=PythonOperator(
        task_id='preprocess_data',
        python_callable=preprocess_data
    )

    train=PythonOperator(
        task_id='train_model',
        python_callable=train_model
    )

    evaluate=PythonOperator(
        task_id='evaluate_model',
        python_callable=evaluate_model
    )

    ## set dependencies(in which order they should run)
    preprocess >> train >> evaluate