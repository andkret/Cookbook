Best Practices Cloud Platforms
=============================

This section is a collection of best practices on how you can arrange the tools together to a platform.  
It's here especially to help you start your own project in the cloud on AWS, Azure and GCP.

Like the advanced skills section this section also follows my [My Data Science Platform Blueprint](sections/01-Introduction.md#my-big-data-platform-blueprint).
In the blueprint I divided the platform into sections: Connect, Buffer, Processing, Store and Visualize.

This order will help you learn how to connect the right tools together.
Take your time and research the tools and learn how they work.

Right now the Azure section has a lot of links to platform examples.
They are also useful for AWS and GCP, just try to change out the tools.

As always, I am going to add more stuff to this over time.

Have fun!

## Contents

- [Amazon Web Services (AWS)](06-BestPracticesCloud.md#aws)
  - [Connect](06-BestPracticesCloud.md#Connect)
  - [Buffer](06-BestPracticesCloud.md#Buffer)
  - [Processing](06-BestPracticesCloud.md#Processing)
  - [Store](06-BestPracticesCloud.md#Store)
  - [Visualize](06-BestPracticesCloud.md#Visualize)
  - [Containerization](06-BestPracticesCloud.md#Containerization)
  - [Best Practices](06-BestPracticesCloud.md#Best-Practices)
  - [More Details](06-BestPracticesCloud.md#More-Details)
- [Microsoft Azure](06-BestPracticesCloud.md#azure)
  - [Connect](06-BestPracticesCloud.md#Connect-1)
  - [Buffer](06-BestPracticesCloud.md#Buffer-1)
  - [Processing](06-BestPracticesCloud.md#Processing-1)
  - [Store](06-BestPracticesCloud.md#Store-1)
  - [Visualize](06-BestPracticesCloud.md#Visualize-1)
  - [Containerization](06-BestPracticesCloud.md#Containerization-1)
  - [Best Practices](06-BestPracticesCloud.md#Best-Practices-1)
- [Google Cloud Platform (GCP)](06-BestPracticesCloud.md#gcp)
  - [Connect](06-BestPracticesCloud.md#Connect-2)
  - [Buffer](06-BestPracticesCloud.md#Buffer-2)
  - [Processing](06-BestPracticesCloud.md#Processing-2)
  - [Store](06-BestPracticesCloud.md#Store-2)
  - [Visualize](06-BestPracticesCloud.md#Visualize-2)
  - [Containerization](06-BestPracticesCloud.md#Containerization-2)
  - [Best Practices](06-BestPracticesCloud.md#Best-Practices-2)

# AWS
## Connect
- Elastic Beanstalk (very old)
- SES Simple Email Service
- API Gateway
## Buffer
- Kinesis
- Kinesis Data Firehose
- Managed Streaming for Kafka (MSK)
- MQ
- Simple Queue Service (SQS)
- Simple Notification Service (SNS)
## Processing
- EC2
- Athena
- EMR
- Elasticsearch
- Kinesis Data Analytics
- Glue
- Step Functions
- Fargate
- Lambda
- SageMaker
## Store
- Simple Storage Service (S3)
- Redshift
- Aurora
- RDS
- DynamoDB
- ElastiCache
- Neptune Graph DB
- Timestream
- DocumentDB (MongoDB compatible)
## Visualize
- Quicksight

## Containerization
- Elastic Container Service (ECS)
- Elastic Container Registry (ECR)
- Elastic Kubernetes Service (EKS)

## Best Practices
Deploying a Spring Boot Application on AWS Using AWS Elastic Beanstalk:

[https://aws.amazon.com/de/blogs/devops/deploying-a-spring-boot-application-on-aws-using-aws-elastic-beanstalk/](https://aws.amazon.com/de/blogs/devops/deploying-a-spring-boot-application-on-aws-using-aws-elastic-beanstalk/)

How to deploy a Docker Container on AWS:

[https://towardsdatascience.com/how-to-deploy-a-docker-container-python-on-amazon-ecs-using-amazon-ecr-9c52922b738f](https://towardsdatascience.com/how-to-deploy-a-docker-container-python-on-amazon-ecs-using-amazon-ecr-9c52922b738f)


## More Details
AWS Whitepapers:

[https://d1.awsstatic.com/whitepapers/aws-overview.pdf](https://d1.awsstatic.com/whitepapers/aws-overview.pdf)


# Azure
## Connect
- Event Hub
- IoT Hub
## Buffer
- Data Factory
- Event Hub
- RedisCache (also Store)
## Processing
- Stream Analytics Service
- Azure Databricks
- Machine Learning
- Azure Functions
- Azure HDInsight (Hadoop PaaS)
## Store
- Blob
- CosmosDB
- MariaDB
- MySQL
- PostgreSQL
- SQL
- Azure Data lake
- Azure Storage (SQL Table?)
- Azure Synapse Analytics
## Visualize
- PowerBI
## Containerization
- Virtual Machines
- Virtual Machine Scale Sets
- Azure Container Service (AKS)
- Container Instances
- Azure Kubernetes Service
## Best Practices

Advanced Analytics Architecture:

[https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/advanced-analytics-on-big-data](https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/advanced-analytics-on-big-data)

Anomaly Detection in Real-time Data Streams:

[https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/anomaly-detection-in-real-time-data-streams](https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/anomaly-detection-in-real-time-data-streams)

Modern Data Warehouse Architecture:

[https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/modern-data-warehouse](https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/modern-data-warehouse)

CI/CD for Containers:

[https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/cicd-for-containers](https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/cicd-for-containers)

Real Time Analytics on Big Data Architecture:

[https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/real-time-analytics](https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/real-time-analytics)

Anomaly Detection in Real-time Data Streams:

[https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/anomaly-detection-in-real-time-data-streams](https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/anomaly-detection-in-real-time-data-streams)

IoT Architecture – Azure IoT Subsystems:

[https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/azure-iot-subsystems](https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/azure-iot-subsystems)

Tier Applications & Data for Analytics:

[https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/tiered-data-for-analytics](https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/tiered-data-for-analytics)

Extract, transform, and load (ETL) using HDInsight:

[https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/extract-transform-and-load-using-hdinsight](https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/extract-transform-and-load-using-hdinsight)

IoT using Cosmos DB:

[https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/iot-using-cosmos-db](https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/iot-using-cosmos-db)

Streaming using HDInsight:

[https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/streaming-using-hdinsight](https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/streaming-using-hdinsight)

# GCP
## Connect
- Cloud IoT Core
- App Engine
- Cloud Dataflow
## Buffer
- Pub/Sub
## Processing
- Compute Engine
- Cloud Functions
- Specialized tools:
  - Cloud Dataflow
  - Cloud Dataproc
  - Cloud Datalab
  - Cloud Dataprep
  - Cloud Composer
- App Engine
## Store
- Cloud Storage
- Cloud SQL
- Cloud Spanner
- Cloud Datastore
- Cloud BigTable
- Cloud Storage
- Cloud Memorystore
- BigQuery
## Visualize

## Containerization
- Kubernetes Engine
- Container Security
## Best Practices

Thanks to Ismail Holoubi for the following GCP links

Best practices for migrating virtual machines to Compute Engine:

https://cloud.google.com/solutions/best-practices-migrating-vm-to-compute-engine

Best practices for Cloud Storage:

https://cloud.google.com/storage/docs/best-practices

Moving a publishing workflow to BigQuery for new data insights:

https://cloud.google.com/blog/products/data-analytics/moving-a-publishing-workflow-to-bigquery-for-new-data-insights

Architecture: Optimizing large-scale ingestion of analytics events and logs:

https://cloud.google.com/solutions/architecture/optimized-large-scale-analytics-ingestion

Choosing the right architecture for global data distribution:

https://cloud.google.com/solutions/architecture/global-data-distribution

Best Practices for Operating Containers:

https://cloud.google.com/solutions/best-practices-for-operating-containers

Preparing a Google Kubernetes Engine Environment for Production:

https://cloud.google.com/solutions/prep-kubernetes-engine-for-prod

Automating IoT Machine Learning: Bridging Cloud and Device Benefits with AI Platform:

https://cloud.google.com/solutions/automating-iot-machine-learning
