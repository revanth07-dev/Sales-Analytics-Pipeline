# Sales-Analytics-Pipeline

This project demonstrates the fundamental concepts and practical application of building a modern data engineering pipeline. It extracts raw sales data, cleans and transforms it into a structured analytical data model, and orchestrates the entire process using industry-standard tools.

Table of Contents
Project Overview

Goals

Architecture

Technologies Used

Setup Instructions (Local Environment)

Prerequisites

Step 1: Project Setup

Step 2: PostgreSQL Database Setup (Sales Data)

Step 3: Apache Airflow Setup

Step 4: dbt Core Setup

Pipeline Details

Data Ingestion (Python)

Data Transformation (dbt)

Orchestration (Airflow)

Running the Pipeline

Verifying the Data & Performance

Future Enhancements

1. Project Overview
This project implements an Extract, Load, Transform (ELT) data pipeline for sales data. The primary objective is to take raw sales transaction records from a CSV file, load them into a staging area, and then transform them into a Kimball-style dimensional model (Fact and Dimension tables) ready for business intelligence and analytics. The entire workflow is automated using Apache Airflow.

2. Goals
Ingest Raw Data: Load sales_data.csv into a PostgreSQL staging table.

Initial Data Cleaning: Perform basic data type conversions and handle missing values during ingestion.

Transform Data: Build a dimensional data model (fact and dimension tables) from the staging data using dbt.

Orchestrate Workflow: Automate the entire ELT process using Apache Airflow, scheduling data ingestion and transformation.

Demonstrate Core DE Skills: Showcase proficiency in Python, SQL, PostgreSQL, Docker, Airflow, and dbt.

3. Architecture
The pipeline follows an ELT (Extract, Load, Transform) pattern:

Okay, here's a comprehensive documentation for your data engineering project, suitable for a GitHub repository. It covers everything from setup to the completed pipeline, highlighting the tools and concepts you've mastered.

Data Engineering Sales Analytics Pipeline
This project demonstrates the fundamental concepts and practical application of building a modern data engineering pipeline. It extracts raw sales data, cleans and transforms it into a structured analytical data model, and orchestrates the entire process using industry-standard tools.

Table of Contents
Project Overview

Goals

Architecture

Technologies Used

Setup Instructions (Local Environment)

Prerequisites

Step 1: Project Setup

Step 2: PostgreSQL Database Setup (Sales Data)

Step 3: Apache Airflow Setup

Step 4: dbt Core Setup

Pipeline Details

Data Ingestion (Python)

Data Transformation (dbt)

Orchestration (Airflow)

Running the Pipeline

Verifying the Data & Performance

Future Enhancements

1. Project Overview
This project implements an Extract, Load, Transform (ELT) data pipeline for sales data. The primary objective is to take raw sales transaction records from a CSV file, load them into a staging area, and then transform them into a Kimball-style dimensional model (Fact and Dimension tables) ready for business intelligence and analytics. The entire workflow is automated using Apache Airflow.

2. Goals
Ingest Raw Data: Load sales_data.csv into a PostgreSQL staging table.

Initial Data Cleaning: Perform basic data type conversions and handle missing values during ingestion.

Transform Data: Build a dimensional data model (fact and dimension tables) from the staging data using dbt.

Orchestrate Workflow: Automate the entire ELT process using Apache Airflow, scheduling data ingestion and transformation.

Demonstrate Core DE Skills: Showcase proficiency in Python, SQL, PostgreSQL, Docker, Airflow, and dbt.

3. Architecture
The pipeline follows an ELT (Extract, Load, Transform) pattern:

Extract & Load (EL): A Python script reads the sales_data.csv, performs initial cleaning, and loads the data into a staging.sales table in PostgreSQL. This script is triggered by Airflow.

Transform (T): dbt models define transformations that read from staging.sales and create cleaned, structured dim_dates, dim_products, and fact_sales tables in the analytics schema of the same PostgreSQL database. This dbt process is also triggered by Airflow.

Orchestration: Apache Airflow schedules and monitors the sequential execution of the Python ingestion script and the dbt transformation process.

4. Technologies Used

Language: Python 

pandas: For data manipulation and CSV reading.

sqlalchemy: For database connectivity.

psycopg2-binary: PostgreSQL adapter for Python.


Database: PostgreSQL 

Persistent storage for raw and transformed data.


Orchestration: Apache Airflow 

For scheduling and monitoring the data pipeline.

Running via Docker Compose for local development.


Transformation: dbt (data build tool) 

For defining and executing SQL-based data transformations.

dbt-postgres: PostgreSQL adapter for dbt.

dbt-utils: dbt package for common SQL macros (e.g., generate_surrogate_key).

Containerization: Docker & Docker Compose

Used to containerize PostgreSQL and Airflow services for isolated and consistent environments.

Data Visualization (Future): Power BI (or similar BI tool)

To connect to the transformed analytical tables for dashboarding.



