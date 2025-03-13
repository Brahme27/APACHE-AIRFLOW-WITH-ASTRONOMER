'''
we are going to define a DAG with the tasks following below:

task_1: start with an initial number 
task_2: add 5 to the initial number
task_3: multiply the result by 2
task_4: subtract 3 from the result
task_5: compute the square of the result
'''

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


## define function for each and every task

def start_number(**context):
    context["ti"].xcom_push(key="current_value",value=10)
    print("starting number 10")

def add_5(**context):
    current_value=context["ti"].xcom_pull(key="current_value",task_ids="start_task")
    new_value=current_value+5
    context["ti"].xcom_push(key="current_value",value=new_value)
    print(f"Add 5: {current_value}+5= {new_value}")

def multiply_by_2(**context):
    current_value=context["ti"].xcom_pull(key="current_value",task_ids="add_5")
    new_value=current_value*2
    context["ti"].xcom_push(key="current_value",value=new_value)
    print(f"Multiply by 2: {current_value}*2= {new_value}")

def subtract_3(**context):
    current_value=context["ti"].xcom_pull(key="current_value",task_ids="multiply_by_2")
    new_value=current_value-3
    context["ti"].xcom_push(key="current_value",value=new_value)
    print(f"Subtract 3: {current_value}-3= {new_value}")

def square_number(**context):
    current_value=context["ti"].xcom_pull(key="current_value",task_ids="subtract_3")
    new_value=current_value**2
    context["ti"].xcom_push(key="current_value",value=new_value)
    print(f"Square: {current_value}^2= {new_value}")


## Define the DAG
with DAG(dag_id="mathematical_pipeline",start_date=datetime(2025,3,13),schedule_interval="@once",catchup=False) as dag:
    
    ## Define the tasks
    start_task=PythonOperator(
        task_id="start_task",
        python_callable=start_number,
        provide_context=True
    )
    
    add_5_task=PythonOperator(
        task_id="add_5",
        python_callable=add_5,
        provide_context=True
    )

    multiply_by_2_task=PythonOperator(
        task_id="multiply_by_2",
        python_callable=multiply_by_2,
        provide_context=True
    )

    subtract_3_task=PythonOperator(
        task_id="subtract_3",
        python_callable=subtract_3,
        provide_context=True
    )

    square_number_task=PythonOperator(
        task_id="square_number",
        python_callable=square_number,
        provide_context=True
    )

    ## Define the task dependencies
    start_task >> add_5_task >> multiply_by_2_task >> subtract_3_task >> square_number_task 