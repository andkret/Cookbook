Data Engineering Course: Building A Data Platform
=================================================

## Contents

- [What We Want To Do](04-HandsOnCourse.md#what-we-want-to-do)
- [Thoughts On Choosing A Development Environment](04-HandsOnCourse.md#thoughts-on-choosing-a-development-environment)
- [A Look Into the Twitter API](04-HandsOnCourse.md#a-look-into-the-twiiter-api)
- [Ingesting Tweets with Apache Nifi](04-HandsOnCourse.md#ingesting-tweets-with-apache-nifi)
- [Writing from Nifi to Apache Kafka](04-HandsOnCourse.md#writing-from-nifi-to-kafka)
- [Apache Zeppelin](04-HandsOnCourse.md#apache-zeppelin)
  - [Install and Ingest Kafka Topic](04-HandsOnCourse.md#install-and-ingest-kafka-topic)
  - [Processing Messages with Spark & SparkSQL](04-HandsOnCourse.md#processing-messages-with-spark-and-sparksql)
  - [Visualizing Data](04-HandsOnCourse.md#visualizing-data)
- [Switch Processing from Zeppelin to Spark](04-HandsOnCourse.md#switch-processing-from-zeppelin-to-spark)

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

| Podcast Episode: #068 How to Build a Budget Data Science PC
|------------------|
|In this podcast we look into conﬁguring a sub 1000 dollar PC for data engineering and machine learning.
| [Watch on YouTube](https://youtu.be/00NWR-II6ek) \ [Listen on Anchor](https://anchor.fm/andreaskayy/episodes/068-A-Budget-Data-Science-PC-Build-e45inh)|

A Look Into the Twitter API
---------------------------

| Podcast Episode: #081 Twitter API Research
|------------------|
|In this podcast we were looking into how the Twitter API works and how you get access to it.
| [Watch on YouTube](https://youtu.be/UnAXKxeIlyg)


Ingesting Tweets with Apache Nifi
---------------------------------

| Podcast Episode: #082 Reading Tweets With Apache Niﬁ & IaaS vs PaaS vs SaaS
|------------------|
|In this podcast we are trying to read Twitter Data with Niﬁ.
| [Watch on YouTube](https://youtu.be/pWuT4UAocUY)

| Podcast Episode: #085 Trying to read Tweets with Niﬁ Part 2
|------------------|
|We are looking into the Big Data landscape chart and we are trying to read Twitter Data with Niﬁ again.
| [Watch on YouTube](https://youtu.be/OLUwXr8-gAk)


Writing from Nifi to Apache Kafka
---------------------------------

| Podcast Episode: #086 How to Write from Niﬁ to Kafka Part 1
|------------------|
|I’ve been working a lot on the cookbook, because it’s so much fun. I gotta tell you what I added. Then we are trying to write the Tweets from Apache Niﬁ into Kafka. Also talk about Kafka basics.
| [Watch on YouTube](https://youtu.be/F7Y-ygnyJMg)

| Podcast Episode: #088 How to Write from Niﬁ to Kafka Part 2
|------------------|
|In this podcast we ﬁnally ﬁgure out how to write to Kafka from Niﬁ. The problem was the network conﬁguration of the Docker containers.
| [Watch on YouTube](https://youtu.be/pJbRnBQmoCs)


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
