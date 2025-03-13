Overview
========
Welcome to Astronomer! This project was generated after you ran 'astro dev init' using the Astronomer CLI. This readme describes the contents of the project, as well as how to run Apache Airflow on your local machine.

# Airflow Projects - Astronomer

This repository contains three small projects demonstrating how to use Apache Airflow with Astronomer for workflow automation and data pipeline management.

## Project 1: Machine Learning Pipeline with Airflow  (mlpipeline.py)

### Description
This project defines an *ETL pipeline for Machine Learning* using Airflow. The pipeline consists of three tasks:
1. *Preprocess Data* - Simulates data preprocessing.
2. *Train Model* - Simulates the model training process.
3. *Evaluate Model* - Simulates model evaluation.

### Files
- ml_pipeline.py - The DAG file containing the ML pipeline.

### DAG Structure

Preprocess Data → Train Model → Evaluate Model


### How It Works
- Each step is implemented as a *PythonOperator* inside an Airflow DAG.
- The tasks execute in sequence, ensuring dependencies are followed.

---

## Project 2: Mathematical Operations Pipeline (mathematical_pipeline.py)

### Description
This project defines a *mathematical sequence* as a DAG. It starts with a number and performs the following transformations:
1. *Start Task* - Initialize with 10.
2. *Add 5* - Adds 5 to the number.
3. *Multiply by 2* - Multiplies the result by 2.
4. *Subtract 3* - Subtracts 3 from the result.
5. *Square the Result* - Computes the square of the final value.

### Files
- mathematical_pipeline.py - The DAG file for this project.

### DAG Structure

Start Task → Add 5 → Multiply by 2 → Subtract 3 → Square the Result


### How It Works
- Uses *XComs* to pass data between tasks.
- Each function retrieves the previous result using xcom_pull and updates the value using xcom_push.

---

## Project 3: TaskFlow API Implementation (mathpipeline_with_taskFlowApi.py)

### Description
This project showcases *Airflow's TaskFlow API* by implementing the same mathematical sequence from Project 2 but with a simplified syntax using @task decorators.

### Benefits of TaskFlow API
- Eliminates the need for *XCom push/pull*.
- Tasks automatically pass data between each other.
- Code is more readable and concise.

### Files
- math_sequence_taskflow.py - The DAG file using TaskFlow API.

### DAG Structure

Start Number → Add 5 → Multiply by 2 → Subtract 3 → Square the Result


### How It Works
- Uses the @task decorator instead of PythonOperator.
- Each function returns a value, which is automatically passed to the next task.



## list of essential Astronomer(Astro) Airflow commands

# 1. Install Astro CLI (if not installed)
curl -sSL install.astronomer.io | bash

# 2. Create a new Astro Airflow project
astro dev init

# 3. Start the Airflow project locally
astro dev start

# 4. Stop the running Airflow instance
astro dev stop

# 5. Restart Airflow after making changes
astro dev restart

# 6. List all running Airflow containers
astro dev ps

# 7. Open the Airflow UI in a browser
astro dev airflow

# 8. Run Airflow CLI commands inside the running instance
astro dev run airflow dags list

# 9. Deploy the project to Astronomer Cloud
astro deploy

# 10. View logs of running tasks
astro dev logs

# 11. Destroy the local Airflow environment (removes all containers & volumes)
astro dev kill

## Conclusion
These projects provide a foundational understanding of Apache Airflow with Astronomer. They demonstrate *task dependencies, XComs, and TaskFlow API*, which are essential for building real-world data pipelines.

