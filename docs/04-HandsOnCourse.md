Data Engineering Course: Building A Data Platform
=================================================

## Contents

- [GenAI Retrieval Augmented Generation with Ollama and ElasticSearch](04-HandsOnCourse.md#genai-retrieval-augmented-generation-with-ollama-and-elasticsearch)
- [Free Data Engineering Course with AWS, TDengine, Docker and Grafana](04-HandsOnCourse.md#free-data-engineering-course-with-aws-tdengine-docker-and-grafana)
- [Monitor your data in dbt & detect quality issues with Elementary](04-HandsOnCourse.md#monitor-your-data-in-dbt-and-detect-quality-issues-with-elementary)
- [Solving Engineers 4 Biggest Airflow Problems](04-HandsOnCourse.md#solving-engineers-4-biggest-airflow-problems)
- [The best alternative to Airlfow? Mage.ai](04-HandsOnCourse.md#the-best-alternative-to-airlfow?-mage.ai)

## GenAI Retrieval Augmented Generation with Ollama and ElasticSearch

- This how-to is based on this one from Elasticsearch: https://www.elastic.co/search-labs/blog/rag-with-llamaIndex-and-elasticsearch
- Instead of Elasticsearch cloud we're going to run everything locally
- The simplest way to get this done is to just clone this GitHub Repo for the code and docker setup
- I've tried this on a M1 Mac. Changes for Windows with WSL will come later.
- The biggest problems that I had were actually installing the dependencies rather than the code itself.

### Install Ollama
1. Download Ollama from here https://ollama.com/download/mac
2. Unzip, drag into applications and install
3. do `ollama run mistral` (It's going to download the Mistral 7b model, 4.1GB size)
4. Create a new folder in Documents "Elasticsearch-RAG"
5. Open that folder in VSCode

### Install Elasticsearch & Kibana (Docker)
1. Use the docker-compose file from this repo: https://github.com/andkret/Cookbook/blob/master/Code%20Examples/GenAI-RAG/docker-compose.yml
2. Download Docker Desktop from here: https://www.docker.com/products/docker-desktop/
3. Install docker desktop and sign in in the app/create a user -> sends you to the browser

**For Windows Users**
Configure WSL2 to use max only 4GB of ram:
```
wsl --shutdown
notepad "$env:USERPROFILE/.wslconfig"
```
.wslconfig file:
```
[wsl2]
memory=4GB   # Limits VM memory in WSL 2 up to 4GB
```
**Modify the Linux kernel map count in WSL**
Do this before the start because Elasticsearch requires a higher value to work
`sudo sysctl -w vm.max_map_count=262144`

4. go to the Elasticsearch-RAG folder and do `docker compose up`
5. make sure you have Elasticsearch 8.11 or later (we use 8.16 here in this project) if you want to use your own Elasticsearch image
6. if you get this error on a mac then just open the console in the docker app: *error getting credentials - err: exec: docker-credential-desktop: executable file not found in $PATH, out:*
7. Install xcode command line tools: `xcode-select --install`
8. make sure you're at python 3.8.1 or larger -> installed 3.13.0 from https://www.python.org/downloads/

### Setup the virtual Python environment

#### preparation on a Mac
##### install brew
which brew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
export PATH="/opt/homebrew/bin:$PATH"
brew --version
brew install pyenv
brew install pyenv-virtualenv

##### install pyenv
```
brew install pyenv
brew install pyenv-virtualenv
```

Modify the path so that pyenv is in the path variable
`nano ~/.zshrc`

```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

install dependencies for building python versions
`brew install openssl readline sqlite3 xz zlib`

Reload to apply changes
`source ~/.zshrc`

install python
```
pyenv install 3.11.6
pyenv version
```

Set Python version system wide
`pyenv global 3.11.6`

```
pyenv virtualenv <python-version> <new-virtualenv-name>
pyenv activate <your-virtualenv-name>
pyenv virtualenv-delete <your-virtualenv-name>
```

#### Windows without pyenv
setup virtual python environment - go to the Elasticsearch-RAG folder and do
`python3 -m venv .elkrag`
enable the environment
`source .elkrag/bin/activate`


### Install required libraries (do one at a time so you see errors):
```
pip install llama-index (optional python3 -m pip install package name)
pip install llama-index-embeddings-ollama
pip install llama-index-llms-ollama
pip install llama-index-vector-stores-elasticsearch
pip install python-dotenv
```

### Write the data to Elasticsearch
1. create / copy in the index.py file
2. download the conversations.json file from the folder code examples/GenAI-RAG
3. if you get an error with the execution then check if pedantic version is <2.0 `pip show pydantic` if not do this: `pip install "pydantic<2.0`
4. run the program index.py: https://github.com/andkret/Cookbook/blob/master/Code%20Examples/GenAI-RAG/index.py

### Check the data in Elasticsearch
1. go to kibana http://localhost:5601/app/management/data/index_management/indices and see the new index called calls
2. go to dev tools and try out this query `GET calls/_search?size=1 http://localhost:5601/app/dev_tools#/console/shell`

### Query data from elasticsearch and create an output with Mistral
1. if everything is good then run the query.py file https://github.com/andkret/Cookbook/blob/master/Code%20Examples/GenAI-RAG/query.py
2. try a few queries :)

### Install libraries to extract text from pdfs


### Extract data from CV and put it into Elasticsearch
I created a CV with ChatGPT https://github.com/andkret/Cookbook/blob/master/Code%20Examples/GenAI-RAG/Liam_McGivney_CV.pdf

Install the library to extract text from the pdf
`pip install PyMuPDF`
I had to Shift+Command+p then python clear workspace cache and reload window. Then it saw it :/

The file cvpipeline.py has the python code for the indexing. It's not working right now though!
https://github.com/andkret/Cookbook/blob/master/Code%20Examples/GenAI-RAG/cvpipeline.py


I'll keep developing this and update it once it's working.


## Free Data Engineering Course with AWS TDengine Docker and Grafana

**Free hands-on course:** [Watch on YouTube](https://youtu.be/eoj-CnrR9jA)

In this detailed tutorial video, Andreas guides viewers through creating an end-to-end data pipeline using time series data. The project focuses on fetching weather data from a Weather API, processing it on AWS, storing it in TDengine (a time series database), and visualizing the data with Grafana. Here's a concise summary of what the video covers:

1. **Introduction and Setup:**
  - The project is introduced along with a GitHub repository containing all necessary resources and a step-by-step guide.
  - The pipeline architecture includes an IoT weather station, a Weather API, AWS for processing, TDengine for data storage, and Grafana for visualization.
2. **Project Components:**
  - **Weather API:** Utilizes weatherapi.com to fetch weather data.
  - **AWS Lambda:** Processes the data fetched from the Weather API.
  - **TDengine:** Serves as the time series database to store processed data. It's highlighted for its performance and simplicity, especially for time series data.
  - **Grafana:** Used for creating dashboards to visualize the time series data.
3. **Development and Deployment:**
  - The local development environment setup includes Python, Docker, and VS Code.
  - The tutorial covers the creation of a Docker image for the project and deploying it to AWS Elastic Container Registry (ECR).
  - AWS Lambda is then configured to use the Docker image from ECR.
  - AWS EventBridge is used to schedule the Lambda function to run at specified intervals.
4. **Time Series Data:**
  - The importance of time series data and the benefits of using a time series database like TDengine over traditional relational databases are discussed.
  - TDengine's features such as speed, scaling, data retention, and built-in functions for time series data are highlighted.
5. **Building the Pipeline:**
  - Detailed instructions are provided for setting up each component of the pipeline:
    - Fetching weather data from the Weather API.
    - Processing and sending the data to TDengine using an AWS Lambda function.
    - Visualizing the data with Grafana.
  - Each step includes code snippets and configurations needed to implement the pipeline.
6. **Conclusion:**
  - The video concludes with a demonstration of the completed pipeline, showing weather data visualizations in Grafana.
  - Viewers are encouraged to replicate the project using the resources provided in the GitHub repository linked in the video description.

This video provides a comprehensive guide to building a data pipeline with a focus on time series data, demonstrating the integration of various technologies and platforms to achieve an end-to-end solution.

## Monitor your data in dbt and detect quality issues with Elementary

**Free hands-on tutorial:** [Watch on YouTube](https://youtu.be/6fnU91Q2gq0)

In this comprehensive tutorial, Andreas delves into the integration of dbt (data build tool) with Elementary to enhance data monitoring and quality detection within Snowflake databases. The tutorial is structured to guide viewers through a hands-on experience, starting with an introduction to a sample project setup and the common challenges faced in monitoring dbt jobs. It then transitions into how Elementary can be utilized to address these challenges effectively.

Key learning points and tutorial structure include:

1. **Introduction to the Sample Project:** Andreas showcases a project setup involving Snowflake as the data warehouse, dbt for data modeling and testing, and a visualization tool for data analysis. This setup serves as the basis for the tutorial.
2. **Challenges in Monitoring dbt Jobs:** Common issues in monitoring dbt jobs are discussed, highlighting the limitations of the dbt interface in providing comprehensive monitoring capabilities.
3. **Introduction to Elementary:** Elementary is introduced as a dbt-native data observability tool designed to enhance the monitoring and analysis of dbt jobs. It offers both open-source and cloud versions, with the tutorial focusing on the cloud version.
4. **Setup Requirements:** The tutorial covers the necessary setup on both the Snowflake and dbt sides, including schema creation, user and role configuration in Snowflake, and modifications to the dbt project for integrating with Elementary.
5. **Elementary's User Interface and Features:** A thorough walkthrough of Elementary's interface is provided, showcasing its dashboard, test results, model runs, data catalog, and data lineage features. The tool's ability to automatically run additional tests, like anomaly detection and schema change detection, is also highlighted.
6. **Advantages of Using Elementary:** The presenter outlines several benefits of using Elementary, such as easy implementation, native test integration, clean and straightforward UI, and enhanced privacy due to data being stored within the user's data warehouse.
7. **Potential Drawbacks:** Some potential drawbacks are discussed, including the additional load on dbt job execution due to more models being run and limitations in dashboard customization.
8. **Summary and Verdict:** The tutorial concludes with a summary of the key features and benefits of using Elementary with dbt, emphasizing its value in improving data quality monitoring and detection.

Overall, viewers are guided through setting up and utilizing Elementary for dbt data monitoring, gaining insights into its capabilities, setup process, and the practical benefits it offers for data quality assurance.


## Solving Engineers 4 Biggest Airflow Problems

**Free hands-on tutorial:** [Watch on YouTube](https://youtu.be/b9bMNEh8bes)

In this informative video, Andreas discusses the four major challenges engineers face when working with Apache Airflow and introduces Astronomer, a managed Airflow service that addresses these issues effectively. Astronomer is highlighted as a solution that simplifies Airflow deployment and management, making it easier for engineers to develop, deploy, and monitor their data pipelines. Here's a summary of the key points discussed for each challenge and how Astronomer provides solutions:

1. Managing Airflow Deployments:
  - **Challenge:** Setting up and maintaining Airflow deployments is complex and time-consuming, involving configuring cloud instances, managing resources, scaling, and updating the Airflow system.
  - **Solution with Astronomer:** Offers a straightforward deployment process where users can easily configure their deployments, choose cloud providers (GCP, AWS, Azure), and set up scaling with just a few clicks. Astronomer handles the complexity, making it easier to manage production and quality environments.
2. Development Environment and Deployment:
  - **Challenge:** Local installation of Airflow is complicated due to its dependency on multiple Docker containers and the need for extensive configuration.
  - **Solution with Astronomer:** Provides a CLI tool for setting up a local development environment with a single command, simplifying the process of developing, testing, and deploying pipelines. The Astronomer CLI also helps in initializing project templates and deploying Dags to the cloud effortlessly.
3. Source Code Management and CI/CD Pipelines:
  - **Challenge:** Collaborative development and continuous integration/deployment (CI/CD) are essential but challenging to implement effectively with Airflow alone.
  - **Solution with Astronomer:** Facilitates easy integration with GitHub for source code management and GitHub Actions for CI/CD. This allows automatic testing and deployment of pipeline code, ensuring a smooth workflow for teams working on pipeline development.
4. Observing Pipelines and Alarms:
  - **Challenge:** Monitoring data pipelines and getting timely alerts when issues occur is crucial but often difficult to achieve.
  - **Solution with Astronomer:** The Astronomer platform provides a user-friendly interface for monitoring pipeline status and performance. It also offers customizable alerts for failures or prolonged task durations, with notifications via email, PagerDuty, or Slack, ensuring immediate awareness and response to issues.

Overall, the video shows Astronomer as a powerful and user-friendly platform that addresses the common challenges of using Airflow, from deployment and development to collaboration, CI/CD, and monitoring. It suggests that Astronomer can significantly improve the experience of engineers working with Airflow, making it easier to manage, develop, and monitor data pipelines.


## The best alternative to Airlfow? Mage.ai

**Free hands-on tutorial:** [Watch on YouTube](https://youtu.be/3gXsFEC3aYA)

In this insightful video, Andreas introduces Mage, a promising alternative to Apache Airflow, focusing on its simplicity, user-friendliness, and scalability. The video provides a comprehensive walkthrough of Mage, highlighting its key features and advantages over Airflow. Here's a breakdown of what viewers can learn and expect from the video:

1. **Deployment Ease:** Mage offers a stark contrast to Airflow's complex setup process. It simplifies deployment to a single Docker image, making it straightforward to install and start on any machine, whether it's local or cloud-based on AWS, GCP, or Azure. This simplicity extends to scaling, which Mage handles horizontally, particularly beneficial in Kubernetes environments where performance scales with the number of pipelines.
2. **User Interface (UI):** Mage shines with its UI, presenting a dark mode interface that's not only visually appealing but also simplifies navigation and pipeline management. The UI facilitates easy access to pipelines, scheduling, and monitoring of pipeline runs, offering a more intuitive experience compared to Airflow.
3. **Pipeline Creation and Modification:** Mage streamlines the creation of ETL pipelines, allowing users to easily add data loaders, transformers, and exporters through its UI. It supports direct interaction with APIs for data loading and provides a visual representation of the data flow, enhancing the overall pipeline design experience.
4. **Data Visualization and Exploration:** Beyond simple pipeline creation, Mage enables in-depth data exploration within the UI. Users can generate various charts, such as histograms and bar charts, to analyze the data directly, a feature that greatly enhances the tool's utility.
5. **Testing and Scheduling:** Testing pipelines in Mage is straightforward, allowing for quick integration of tests to ensure data quality and pipeline reliability. Scheduling is also versatile, supporting standard time-based triggers, event-based triggers for real-time data ingestion, and API calls for on-demand pipeline execution.
6. **Support for Streaming and ELT Processes:** Mage is not limited to ETL workflows but also supports streaming and ELT processes. It integrates seamlessly with DBT models for in-warehouse transformations and Spark for big data processing, showcasing its versatility and scalability.
7. **Conclusion and Call to Action:** Andreas concludes by praising the direction in which the industry is moving, with tools like Mage simplifying data engineering processes. He encourages viewers to try Mage and engage with the content by liking, subscribing, and commenting on their current tools and the potential impact of Mage.

Overall, the video shows Mage as a highly user-friendly, scalable, and versatile tool for data pipeline creation and management, offering a compelling alternative to traditional tools like Airflow.
