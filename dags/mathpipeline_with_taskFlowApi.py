'''
TaskFlow API in Apache Airflow
The TaskFlow API in Airflow is a simplified way to define tasks using Python functions and decorators (@task). 
It automatically handles XComs for data passing between tasks, removing the need for xcom_push() and xcom_pull().
'''
from airflow import DAG
from airflow.decorators import task 
from datetime import datetime

## Define the DAG
with DAG(
    dag_id="Math_sequence_DAG_with_TASK_FLOW_API",
    start_date=datetime(2025,3,13),
    schedule_interval="@once",
    catchup=False 
) as dag:
    
    @task 
    def start_number():
        initial_number=10
        print(f"Strating number: {initial_number}")
        return initial_number
    
    @task 
    def add_5(number):
        new_value=number+5
        print(f"Add 5: {number} + 5 ={new_value}")
        return new_value
    
    @task 
    def multiply_by_two(number):
        new_value= number*2 
        print(f"Multiply by 2 :{number} *2 ={new_value}")
        return new_value
    
    @task
    def subtract_three(number):
        new_value=number-3
        print(f"Subtracht 3: {number} -3 ={new_value}")
        return new_value
    
    @task 
    def square_number(number):
        new_value=number **2
        print(f"Square the result :{number}^2 ={new_value}")
        return new_value

    ##set the dependencies
    start_value=start_number()
    added_value=add_5(start_value)
    multiply_value=multiply_by_two(added_value)
    subtracted_value=subtract_three(multiply_value)
    square_value=square_number(subtracted_value)