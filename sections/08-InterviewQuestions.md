1001 Data Engineering Interview Questions
=========================================

## Contents:

- [Python](10-InterviewQuestions.md#python)
- [SQL](10-InterviewQuestions.md#sql)
- [Integrate](10-InterviewQuestions.md#integrate)
    - [APIs](10-InterviewQuestions.md#apis)
- [Message Queues](10-InterviewQuestions.md#message-queues)
    - [Distributed Message Queues](10-InterviewQuestions.md#distributed-message-queues)
    - [Message Queues (Fifo)](10-InterviewQuestions.md#integrate)
    - [Caches](10-InterviewQuestions.md#caches)
- [Data Processing](10-InterviewQuestions.md#data-processing)
    - [ETL](10-InterviewQuestions.md#etl)
    - [Stream Processing](10-InterviewQuestions.md#stream-processing)
    - [Batch Processing](10-InterviewQuestions.md#batch-processing)
    - [Processing Frameworks](10-InterviewQuestions.md#processing-frameworks)
        - [Serverless](10-InterviewQuestions.md#serverless)
        - [Distributed Processing Frameworks](10-InterviewQuestions.md#distributed-processing-frameworks)
    - [Scheduling](10-InterviewQuestions.md#scheduling)
        - [Airflow](10-InterviewQuestions.md#airflow)
    - [CI-CD](10-InterviewQuestions.md#ci-cd)
    - [Docker](10-InterviewQuestions.md#docker)
    - [Kubernetes](10-InterviewQuestions.md#kubernetes)
- [Data Storage](10-InterviewQuestions.md#data-storage)
    - [Relational Databases](10-InterviewQuestions.md#relational-databases)
    - [NoSQL](10-InterviewQuestions.md#nosql)
    - [Analytical Stores](10-InterviewQuestions.md#analytical-stores)
    - [Relational Modeling](10-InterviewQuestions.md#relational-modeling)
    - [Dimensional Data Modeling](10-InterviewQuestions.md#dimensional-modeling)
    - [Data Lakes](10-InterviewQuestions.md#data-lakes)
- [Data Platforms](10-InterviewQuestions.md#data-platforms)
    - [AWS](10-InterviewQuestions.md#aws)
    - [Azure](10-InterviewQuestions.md#azure)
    - [GCP](10-InterviewQuestions.md#gcp)
    - [Snowflake](10-InterviewQuestions.md#snowflake)


### Python

1. **What is Apache Spark, and how can you use it with Python?**
   - **Answer**: Apache Spark is a distributed data processing framework that allows for big data processing with in-memory computing capabilities. You can use it with Python through PySpark, which provides a Python API for Spark. PySpark enables data engineers to write Spark applications in Python.

2. **How do you perform data cleaning in Python?**
   - **Answer**: Data cleaning in Python can be performed using the `pandas` library. Common tasks include handling missing values (`dropna`, `fillna`), removing duplicates (`drop_duplicates`), converting data types, normalizing data, and handling outliers. Example:
     ```python
     import pandas as pd
     df = pd.read_csv('data.csv')
     df.dropna(inplace=True)  # Remove rows with missing values
     df['column'] = df['column'].astype(int)  # Convert column to integer type
     ```

3. **Explain how you would optimize a slow-running SQL query within a Python ETL pipeline.**
   - **Answer**: To optimize a slow-running SQL query, you can:
     - Analyze the query execution plan.
     - Add appropriate indexes.
     - Optimize the query by reducing complexity, such as using JOINs efficiently and avoiding unnecessary subqueries.
     - Partition large tables if applicable.
     - Use caching and materialized views for frequently accessed data.
     - Ensure that statistics are up to date.
     Example with SQLAlchemy:
     ```python
     from sqlalchemy import create_engine
     engine = create_engine('postgresql://user:password@localhost/dbname')
     with engine.connect() as connection:
         result = connection.execute('SELECT * FROM table WHERE condition')
         data = result.fetchall()
     ```

4. **What is the role of a workflow scheduler in data engineering, and can you name some common ones?**
   - **Answer**: A workflow scheduler automates and manages the execution of ETL jobs and data pipelines. It ensures tasks are executed in the correct order and handles retries, dependencies, and monitoring. Common workflow schedulers include Apache Airflow, Luigi, Prefect, and Apache NiFi.

5. **How do you handle schema changes in a data pipeline?**
   - **Answer**: Handling schema changes in a data pipeline involves:
     - Implementing schema evolution techniques.
     - Using tools like Apache Avro, which supports schema evolution.
     - Versioning schemas and ensuring backward compatibility.
     - Monitoring and validating incoming data against the schema.
     - Applying transformations to adapt to new schemas.
     Example with Avro:
     ```python
     from avro.datafile import DataFileReader
     from avro.io import DatumReader

     reader = DataFileReader(open("data.avro", "rb"), DatumReader())
     for record in reader:
         print(record)
     reader.close()
     ```

6. **What is data partitioning, and why is it important in data engineering?**
   - **Answer**: Data partitioning is the process of dividing a large dataset into smaller, more manageable pieces, often based on a key such as date, user ID, or geographic location. Partitioning improves query performance by reducing the amount of data scanned and allows for parallel processing. It also helps in managing large datasets and reducing I/O costs.

7. **How do you ensure data quality in your pipelines?**
   - **Answer**: Ensuring data quality involves:
     - Implementing data validation checks (e.g., constraints, data type checks).
     - Monitoring for data anomalies and inconsistencies.
     - Using data profiling tools to understand the data.
     - Creating unit tests for data processing logic.
     - Automating data quality checks and alerting mechanisms.
     Example with `pandas` for data validation:
     ```python
     import pandas as pd

     df = pd.read_csv('data.csv')
     assert df['column'].notnull().all(), "Missing values found in column"
     assert (df['age'] >= 0).all(), "Negative ages found"
     ```

8. **What is the difference between batch processing and stream processing?**
   - **Answer**: Batch processing involves processing large volumes of data at once, usually at scheduled intervals. It is suitable for tasks that are not time-sensitive. Stream processing, on the other hand, involves processing data in real-time as it arrives, which is suitable for time-sensitive applications such as real-time analytics, monitoring, and alerts.

9. **How do you implement logging and monitoring in your data pipelines?**
   - **Answer**: Logging and monitoring can be implemented using:
     - Logging libraries like Python's `logging` module to capture and store logs.
     - Monitoring tools like Prometheus, Grafana, or ELK Stack (Elasticsearch, Logstash, Kibana) to visualize and monitor logs.
     - Setting up alerts for failures or anomalies.
     Example with Python's `logging` module:
     ```python
     import logging

     logging.basicConfig(filename='pipeline.log', level=logging.INFO)
     logging.info('This is an informational message')
     logging.error('This is an error message')
     ```

10. **What are some common challenges you face with distributed data processing, and how do you address them?**
    - **Answer**: Common challenges with distributed data processing include data consistency, fault tolerance, data shuffling, and latency. To address these:
      - Use distributed processing frameworks like Apache Spark, which handle many of these issues internally.
      - Implement robust error handling and retries.
      - Optimize data shuffling by partitioning data effectively.
      - Use caching mechanisms to reduce latency.
      - Ensure proper resource allocation and scaling to handle large data volumes.

## SQL

## Integrate
### APIs

These questions cover a range of topics related to APIs, including their concepts, security, best practices, and specific implementation details.

1. **What is an API and how does it work?**
   - **Answer**: An API (Application Programming Interface) is a set of rules and protocols for building and interacting with software applications. It allows different software systems to communicate with each other. APIs define the methods and data formats that applications can use to request and exchange data.

2. **What are the different types of APIs?**
   - **Answer**: The main types of APIs include:
     - **Open APIs (Public APIs)**: Available to developers and other users with minimal restrictions.
     - **Internal APIs (Private APIs)**: Used within an organization to connect systems and data internally.
     - **Partner APIs**: Shared with specific business partners and offer more control over how data is exposed.
     - **Composite APIs**: Combine multiple API requests into a single call, allowing multiple data or service requests in one API call.

3. **What is REST and how does it differ from SOAP?**
   - **Answer**: REST (Representational State Transfer) and SOAP (Simple Object Access Protocol) are two different approaches to building APIs. REST uses standard HTTP methods (GET, POST, PUT, DELETE) and is stateless, meaning each request from a client to a server must contain all the information needed to understand and process the request. SOAP, on the other hand, is a protocol that relies on XML-based messaging and includes built-in rules for security and transactions.

4. **Explain the concept of RESTful services.**
   - **Answer**: RESTful services are web services that follow the principles of REST. These principles include:
     - **Statelessness**: Each request from a client must contain all the information needed by the server to process the request.
     - **Client-Server Architecture**: The client and server are separate entities, and they communicate over a network via standard HTTP.
     - **Cacheability**: Responses from the server can be cached by the client or intermediate proxies to improve performance.
     - **Uniform Interface**: Resources are identified in the request (usually via URIs), and actions are performed using standard HTTP methods.

5. **What is an API gateway and why is it used?**
   - **Answer**: An API gateway is a server that acts as an intermediary for requests from clients seeking resources from backend services. It provides various functions such as request routing, composition, protocol translation, and handling of cross-cutting concerns like authentication, authorization, logging, monitoring, and rate limiting. It simplifies the client interface and improves security, scalability, and manageability of API services.

6. **How do you ensure the security of an API?**
   - **Answer**: Ensuring API security involves several practices, including:
     - **Authentication**: Verify the identity of the user or system making the request (e.g., using OAuth, JWT).
     - **Authorization**: Ensure the authenticated user or system has permission to perform the requested action.
     - **Encryption**: Use HTTPS to encrypt data in transit between the client and server.
     - **Rate Limiting**: Prevent abuse by limiting the number of requests a client can make in a given time period.
     - **Input Validation**: Validate and sanitize all inputs to prevent injection attacks.
     - **Logging and Monitoring**: Track API usage and monitor for unusual or suspicious activity.

7. **What is versioning in APIs and how is it typically managed?**
   - **Answer**: API versioning is the practice of managing changes to an API without disrupting existing clients. It can be managed in several ways, including:
     - **URI Versioning**: Including the version number in the URI path (e.g., `/v1/resource`).
     - **Query Parameter Versioning**: Including the version number as a query parameter (e.g., `/resource?version=1`).
     - **Header Versioning**: Including the version number in the HTTP headers (e.g., `Accept: application/vnd.example.v1+json`).

8. **What are HTTP status codes and why are they important in API responses?**
   - **Answer**: HTTP status codes are standardized codes returned by a server to indicate the result of a client's request. They are important because they provide meaningful feedback to the client about what happened with their request. Common status codes include:
     - **200 OK**: The request was successful.
     - **201 Created**: A resource was successfully created.
     - **400 Bad Request**: The request was invalid or cannot be processed.
     - **401 Unauthorized**: Authentication is required and has failed or has not yet been provided.
     - **404 Not Found**: The requested resource could not be found.
     - **500 Internal Server Error**: An error occurred on the server.

9. **Explain the concept of idempotency in RESTful APIs.**
   - **Answer**: Idempotency refers to the property of certain operations whereby performing the same operation multiple times results in the same outcome. In RESTful APIs, methods like GET, PUT, and DELETE are idempotent because making the same request multiple times has the same effect as making it once. POST is not idempotent because multiple requests could create multiple resources.

10. **How do you handle pagination in APIs?**
    - **Answer**: Pagination is used to split large sets of data into manageable chunks. Common methods for handling pagination include:
      - **Offset and Limit**: Using query parameters to specify the starting point and number of records to return (e.g., `?offset=0&limit=10`).
      - **Page Number and Size**: Using query parameters to specify the page number and the number of records per page (e.g., `?page=1&size=10`).
      - **Cursor-Based Pagination**: Using a cursor (a pointer to a specific record) to fetch the next set of results (e.g., `?cursor=abc123`).


These additional questions cover more advanced topics related to APIs, including security, design principles, best practices, and tooling.
11. **What is the difference between synchronous and asynchronous API calls?**
    - **Answer**: Synchronous API calls wait for the response before continuing, blocking the execution of code until the operation completes. Asynchronous API calls, on the other hand, do not block the execution; they allow the code to continue running and handle the response once it arrives, typically through callbacks, promises, or async/await patterns.

12. **What is a webhook, and how does it differ from an API endpoint?**
    - **Answer**: A webhook is a way for an application to provide other applications with real-time information. A webhook is a "callback" that allows the sending application to push data to the receiving application when an event occurs. Unlike traditional API endpoints, which require the client to periodically check for data (polling), webhooks enable the server to push data to the client when an event occurs.

13. **What is CORS, and why is it important in the context of APIs?**
    - **Answer**: CORS (Cross-Origin Resource Sharing) is a security feature implemented in web browsers that restricts web pages from making requests to a different domain than the one that served the web page. It is important in APIs to control how resources on a server are accessed by external domains. Proper CORS configuration ensures that only authorized domains can access API resources.

14. **What is the purpose of API documentation, and what should it include?**
    - **Answer**: API documentation provides developers with the information they need to use and integrate with an API effectively. It should include:
      - An overview of the API and its purpose.
      - Authentication and authorization methods.
      - Endpoint definitions and available methods (GET, POST, PUT, DELETE).
      - Request and response formats (including headers, query parameters, and body data).
      - Error codes and their meanings.
      - Examples of requests and responses.
      - Rate limits and usage policies.

15. **What are API gateways, and what role do they play in API management?**
    - **Answer**: API gateways act as intermediaries between clients and backend services. They provide various functions such as request routing, load balancing, security (authentication and authorization), rate limiting, logging, monitoring, and transforming requests and responses. API gateways simplify client interactions with microservices and help manage and secure APIs.

16. **How do you handle authentication and authorization in APIs?**
    - **Answer**: Authentication verifies the identity of a user or application, while authorization determines what resources and operations they have access to. Common methods for handling authentication and authorization in APIs include:
      - API keys: Simple tokens provided to access the API.
      - OAuth: An open standard for token-based authentication and authorization.
      - JWT (JSON Web Tokens): A compact, URL-safe means of representing claims to be transferred between two parties.
      - Basic Auth: A simple method using a username and password encoded in base64.

17. **What is the concept of rate limiting in APIs, and why is it important?**
    - **Answer**: Rate limiting controls the number of requests a client can make to an API within a specified time period. It is important for:
      - Preventing abuse and overuse of API resources.
      - Ensuring fair usage among clients.
      - Protecting the backend services from being overwhelmed.
      - Managing and maintaining service quality and performance.

18. **Explain the concept of API throttling.**
    - **Answer**: API throttling is the process of controlling the usage rate of an API by limiting the number of requests a client can make within a certain timeframe. Throttling helps prevent abuse, protects resources, and ensures that the service remains available and responsive to all users. It can be implemented using techniques such as rate limits, quotas, and burst control.

19. **What is HATEOAS and how does it relate to RESTful APIs?**
    - **Answer**: HATEOAS (Hypermedia As The Engine Of Application State) is a constraint of RESTful APIs where hypermedia links are included in the responses to guide clients through the API. It allows clients to dynamically discover available actions and navigate the API without hardcoding the structure. For example, a response to a GET request for a user resource might include links to update or delete the user.

20. **What are some common tools and platforms for testing and documenting APIs?**
    - **Answer**: Common tools and platforms for testing and documenting APIs include:
      - **Postman**: A popular tool for developing, testing, and documenting APIs.
      - **Swagger/OpenAPI**: A framework for designing, building, and documenting RESTful APIs, often used with tools like Swagger UI and Swagger Editor.
      - **Insomnia**: An API client for testing RESTful and GraphQL APIs.
      - **Apigee**: An API management platform providing tools for API design, security, analytics, and monitoring.
      - **Paw**: A macOS-based API client for testing and documenting APIs.
      - **RAML (RESTful API Modeling Language)**: A language for designing and documenting APIs.


## Message queues
### Distributed Message Queues
### Message Queues (Fifo)
### Caches

## Data Processing
### ETL
### Stream processing
### Batch processing
### Processing Frameworks
#### Serverless
#### Distributed Processing frameworks
### Scheduling
#### Airflow
### Docker and Kubernetes
### CI-CD

## Data Storage
### Relational Databases
### NoSQL
### Analytical Stores
### Relational Modeling
### Dimensional Data Modeling
### Data Lakes

## Data Platforms
### AWS
### GCP
### Azure
### Snowflake





Looking for a job or just want to know what people find important? In
this chapter you can find a lot of interview questions we collect on the
stream.

Ultimately this should reach at least one thousand and one questions.

**But Andreas, where are the answers??** Answers are for losers. I have
been thinking a lot about this and the best way for you to prepare and
learn is to look into these questions yourself.

This cookbook or Google will help you a long way. Some questions we
discuss directly on the live stream.

Live Streams
------------

First live stream where we started to collect these questions.

| Podcast Episode: #096 1001 Data Engineering Interview Questions
|------------------|
|First live stream where we collect and try to answer as many interview questions as possible. If this helps people and is fun we do this regularly until we reach 1000 and one.
| [Watch on YouTube](https://youtu.be/WbqRH2r3N40)

All Interview Questions
-----------------------

The interview questions are roughly structured like the sections in the
\"Basic data engineering skills\" part. This makes it easier to navigate
this document. I still need to sort them accordingly.

### SQL DBs

-   What are windowing functions?

-   What is a stored procedure?

-   Why would you use them?

-   What are atomic attributes?

-   Explain ACID props of a database

-   How to optimize queries?

-   What are the different types of JOIN (CROSS, INNER, OUTER)?

-   What is the difference between Clustered Index and Non-Clustered
    Index - with examples?

### The Cloud

-   What is serverless?

-   What is the difference between IaaS, PaaS and SaaS?

-   How do you move from the ingest layer to the Cosumption layer? (In
    Serverless)

-   What is edge computing?

-   What is the difference between cloud and edge and on-premise?

### Linux

-   What is crontab?

### Big Data

-   What are the 4 V's?

-   Which one is most important?

### Kafka

-   What is a topic?

-   How to ensure FIFO?

-   How do you know if all messages in a topic have been fully consumed?

-   What are brokers?

-   What are consumergroups?

-   What is a producer?

### Coding

-   What is the difference between an object and a class?

-   Explain immutability

-   What are AWS Lambda functions and why would you use them?

-   Difference between library, framework and package

-   How to reverse a linked list

-   Difference between args and kwargs

-   Difference between OOP and functional programming

### NoSQL DBs

-   What is a key-value (rowstore) store?

-   What is a columnstore?

-   Diff between Row and col.store

-   What is a document store?

-   Difference between Redshift and Snowflake

### Hadoop

-   What file formats can you use in Hadoop?

-   What is the difference between a namenode and a datanode?

-   What is HDFS?

-   What is the purpose of YARN?

### Lambda Architecture

-   What is streaming and batching?

-   What is the upside of streaming vs batching?

-   What is the difference between lambda and kappa architecture?

-   Can you sync the batch and streaming layer and if yes how?


### Data Warehouse & Data Lake

-   What is a data lake?

-   What is a data warehouse?

-   Are there data lake warehouses?

-   Two data lakes within single warehouse?

-   What is a data mart?

-   What is a slow changing dimension (types)?

-   What is a surrogate key and why use them?

### APIs (REST)

-   What does REST mean?

-   What is idempotency?

-   What are common REST API frameworks (Jersey and Spring)?

### Apache Spark

-   What is an RDD?

-   What is a dataframe?

-   What is a dataset?

-   How is a dataset typesafe?

-   What is Parquet?

-   What is Avro?

-   Difference between Parquet and Avro

-   Tumbling Windows vs. Sliding Windows

-   Difference between batch and stream processing

-   What are microbatches?

### MapReduce

-   What is a use case of mapreduce?

-   Write a pseudo code for wordcount

-   What is a combiner?

### Docker & Kubernetes

-   What is a container?

-   Difference between Docker Container and a Virtual PC

-   What is the easiest way to learn kubernetes fast?

### Data Pipelines

-   What is an example of a serverless pipeline?

-   What is the difference between at most once vs at least once vs
    exactly once?

-   What systems provide transactions?

-   What is a ETL pipeline?

### Airflow

-   What is a DAG (in context of airflow/luigi)?

-   What are hooks/is a hook?

-   What are operators?

-   How to branch?

### DataVisualization

-   What is a BI tool?

### Security/Privacy

-   What is Kerberos?

-   What is a firewall?

-   What is GDPR?

-   What is anonymization?

### Distributed Systems

-   How clusters reach consensus (the answer was using consensus
    protocols like Paxos or Raft). Good I didnt have to explain paxos

-   What is the cap theorem / explain it (What factors should be
    considered when choosing a DB?)

-   How to choose right storage for different data consumers? It's
    always a tricky question

### Apache Flink

-   What is Flink used for?

-   Flink vs Spark?

### GitHub

-   What are branches?

-   What are commits?

-   What's a pull request?

### Dev/Ops

-   What is continuous integration?

-   What is continuous deployment?

-   Difference CI/CD

### Development / Agile

-   What is Scrum?

-   What is OKR?

-   What is Jira and what is it used for?



