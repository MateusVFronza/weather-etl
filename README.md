# Weather Data ETL with Airflow

## Project Summary
This project is an Extract, Transform, Load (ETL) pipeline built with Apache Airflow to collect weather forecast data from the Visual-Crossing API for various cities, with a focus on Florianopolis. The data is then processed and loaded into a target destination for further analysis. This ETL process helps in obtaining up-to-date weather information for multiple locations, enabling various data-driven applications and insights.

## Project Details
### Data Source
The data source for this project is the Visual-Crossing API, which provides weather forecast information for different cities. Florianopolis is the primary city of interest.

### ETL Process
The ETL process is divided into the following steps:

→ Extract: Data is extracted from the Visual-Crossing API by making HTTP requests to retrieve weather forecast data for Florianopolis and other cities.

→ Transform: The extracted data is transformed to clean and structure it. This includes data validation, formatting, and any necessary calculations or data enrichment.

→ Load: The cleaned and transformed data is loaded into a target destination, which could be a database, data warehouse, or any other storage system for further analysis.

### Dependencies
→ Apache Airflow: The project uses Apache Airflow for task scheduling and orchestration. <br>
→ Python: The programming language used for scripting and data manipulation. <br>
→ Visual-Crossing API: The primary data source for weather forecast information. <br>
→ Docker: The project runs within a Docker container for portability and isolation. <br>
→ Docker Container Configuration <br>
→ The project is designed to run within a Docker container. To set up and run the container, follow these steps: <br>
&nbsp;&nbsp;&nbsp;&nbsp;    • Copy the docker-compose.yaml file from the official Apache Airflow documentation: Apache Airflow Docker Compose. <br>
&nbsp;&nbsp;&nbsp;&nbsp;    • Create a docker-compose.yaml file in the project's root directory. <br>
&nbsp;&nbsp;&nbsp;&nbsp;    • Create the following directories in your project's root directory to set up volumes for Airflow: <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    • dags/: This is where you can place your Airflow DAG files. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    • logs/: Airflow logs will be stored here. <br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    • plugins/: You can place custom Airflow plugins in this directory. <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    • data/: This volume will be used for storing data. <br>
&nbsp;&nbsp;&nbsp;&nbsp;    • Run the following command to initialize the Airflow infrastructure within the Docker container: <br>

```docker-compose up airflow-init```

Finally, start the Docker containers for Airflow and your project using:

```docker-compose up```

This will launch the Airflow web server, scheduler, and other necessary components, allowing you to manage and run your ETL pipeline within the Docker environment.

## Virtual Environment
To manage Python dependencies, it is recommended to use a virtual environment. You can create a virtual environment based on the requirements.txt file using the following steps:

Navigate to the project directory.

Create a virtual environment (e.g., .venv) using the following command:

```python -m venv .venv```

Activate the virtual environment:
```.venv\Scripts\activate.ps1``

Install the required Python packages within the virtual environment:
```pip install -r requirements.txt```

## Acknowledgments
This project is based on the knowledge and concepts acquired from one of the Alura Data Engineering courses, called Apache Airflow: orquestrando seu primeiro pipeline de dados. Special thanks to Alura for providing valuable insights and guidance in data engineering.
