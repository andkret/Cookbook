Data Engineering Course: Building A Data Platform
=================================================

## Contents

- [What We Want To Do](HandsOnCourse.md#what-we-want-to-do)
- [Thoughts On Choosing A Development Environment](HandsOnCourse.md#thoughts-on-choosing-a-development-environment)
- [A Look Into the Twitter API](HandsOnCourse.md#a-look-into-the-twiiter-api)
- [Ingesting Tweets with Apache Nifi](HandsOnCourse.md#ingesting-tweets-with-apache-nifi)
- [Writing from Nifi to Apache Kafka](HandsOnCourse.md#writing-from-nifi-to-kafka)
- [Apache Zeppelin](HandsOnCourse.md#apache-zeppelin)
  - [Install and Ingest Kafka Topic](HandsOnCourse.md#install-and-ingest-kafka-topic)
  - [Processing Messages with Spark & SparkSQL](HandsOnCourse.md#processing-messages-with-spark-and-sparksql)
  - [Visualizing Data](HandsOnCourse.md#visualizing-data)
- [Switch Processing from Zeppelin to Spark](HandsOnCourse.md#switch-processing-from-zeppelin-to-spark)

What We Want To Do
------------------

-   Twitter data to predict best time to post using the hashtag
    datascience or ai

-   Find top tweets for the day

-   Top users

-   Analyze sentiment and keywords

Thoughts On Choosing A Development Environment
----------------------------------------------

For a local environment you need a good PC. I thought a bit about a
budget build around 1.000 Dollars or Euros.

  -- ----------------------------------------------------------------------------------------------------------

     [Click here to watch](https://youtu.be/00NWR-II6ek)
     [Click here to listen](https://anchor.fm/andreaskayy/episodes/068-A-Budget-Data-Science-PC-Build-e45inh)
  -- ----------------------------------------------------------------------------------------------------------

A Look Into the Twitter API
---------------------------

  -- -----------------------------------------------------

     [Click here to watch](https://youtu.be/UnAXKxeIlyg)
  -- -----------------------------------------------------

Ingesting Tweets with Apache Nifi
---------------------------------

  -- -----------------------------------------------------

     [Click here to watch](https://youtu.be/pWuT4UAocUY)
  -- -----------------------------------------------------

  -- -----------------------------------------------------

     [Click here to watch](https://youtu.be/OLUwXr8-gAk)
  -- -----------------------------------------------------

Writing from Nifi to Apache Kafka
---------------------------------

  -- -----------------------------------------------------

     [Click here to watch](https://youtu.be/F7Y-ygnyJMg)
  -- -----------------------------------------------------

  -- -----------------------------------------------------

     [Click here to watch](https://youtu.be/pJbRnBQmoCs)
  -- -----------------------------------------------------

Apache Zeppelin
---------------

### Install and Ingest Kafka Topic

Start the container:


    docker run -d -p 8081:8080 --rm \
    -v /Users/xxxx/Documents/DockerFiles/logs:/logs \
    -v /Users/xxxx/Documents/DockerFiles/Notebooks:/notebook \
    -e ZEPPELIN_LOG_DIR='/logs' \
    -e ZEPPELIN_NOTEBOOK_DIR='/notebook' \
    --network app-tier --name zeppelin apache/zeppelin:0.7.3

### Processing Messages with Spark and SparkSQL

### Visualizing Data

Switch Processing from Zeppelin to Spark
----------------------------------------

### Install Spark

### Ingest Messages from Kafka

### Writing from Spark to Kafka

### Move Zeppelin Code to Spark
