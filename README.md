# The Data Engineering Cookbook
I get asked super often how to become a Data Engineer.
That's why I decided to start this cookbook with all the topics you need to look into.

It's not only useful for beginners, professionals will definitely like the case study section.

# Contents:
- [Introduction](#introduction)
- [Basic Engineering Skills](#basic-engineering-skills)
- [Advanced Engineering Skills](#introduction)
- [Hands On Course](#Hands-on-course)
- [1001 Interview Quesitons](#1001-interview-quesitons)


#  Introduction
- [How To Use This Cookbook](Introduction.md#how-to-use-this-cookbook)
- [Data Engineer vs Data Scientist](Introduction.md#data-engineer-vs-data-scientist)
  - [Data Scientist](Introduction.md#data-scientist)
  - [Data Engineer](Introduction.md#data-engineer)
  - [Who Companies Need](Introduction.md#who-companies-need)

# Basic Engineering Skills
- [Learn To Code](BasicSkills.md#learn-to-code)
- [Get Familiar With Git](BasicSkills.md#get-familiar-with-git)
- [Agile Development](BasicSkills.md#agile-development)
  - [Why is agile so important?](BasicSkills.md#Why-is-agile-so-important)
  - [Agile rules I learned over the years](BasicSkills.md#agile-rules-i-learned-over-the-years)
  - [Agile Frameworks](BasicSkills.md#agile-frameworks)
    - [Scrum](BasicSkills.md#scrum)
    - [OKR](BasicSkills.md#okr)
- [Software Engineering Culture](BasicSkills.md#software-engineering-culture)
- [Learn how a Computer Works](BasicSkills.md#learn-how-a-computer-works)
- [Data Network Transmission](BasicSkills.md#data-network-transmission)
- [Security and Privacy](BasicSkills.md#security-and-privacy)
  - [SSL Public and Private Key Certificates](BasicSkills.md#ssl-public-and-private-key-Certificates)
  - [JSON Web Tokens](BasicSkills.md#json-web-tokens)
  - [GDPR regulations](BasicSkills.md#gdpr-regulations)
- [Linux](BasicSkills.md#linux)
  - [OS Basics](BasicSkills.md#os-basics)
  - [Shell scripting](BasicSkills.md#shell-scripting)
  - [Cron Jobs](BasicSkills.md#cron-jobs)
  - [Packet Management](BasicSkills.md#packet-management)
- [The Cloud](BasicSkills.md#the-cloud)
  - [IaaS vs PaaS vs SaaS](BasicSkills.md#iaas-vs-paas-vs-saas)
  - [AWS Azure IBM Google IBM](BasicSkills.md#aws-azure-ibm-google)
  - [Cloud vs On-Premises](BasicSkills.md#cloud-vs-on-premises)
  - [Security](BasicSkills.md#security)
  - [Hybrid Clouds](BasicSkills.md#hybrid-clouds)
- [Security Zone Design](BasicSkills.md#security-zone-design)
  - [How to secure a multi layered application](BasicSkills.md#how-to-secure-a-multi-layered-application)
  - [Cluster security with Kerberos](BasicSkills.md#cluster-security-with-kerberos)

# Advanced Engineering Skills

- [Big Data](AdvancedSkills.md#big-data)
  - [What is Big Data](AdvancedSkills.md#what-is-big-data)
  - [The 4 Vs of Big Data](AdvancedSkills.md#the-4-vs-of-big-data)
  - [Why Big Data](AdvancedSkills.md#why-big-data)
    - [Planning is Everything](AdvancedSkills.md#planning-is-everything)
    - [The Problem with ETL](AdvancedSkills.md#the-problem-with-etl)
    - [Scaling Up](AdvancedSkills.md#scaling-up)
    - [Scaling Out](AdvancedSkills.md#scaling-out)
    - [When not to Do Big Data](AdvancedSkills.md#please-dont-go-big-data)
  - [My Big Data Platform Blueprint](AdvancedSkills.md#my-big-data-platform-blueprint)
    - [Ingest](AdvancedSkills.md#ingest)
    - [Analyse and Process](AdvancedSkills.md#analyse-and-process)
    - [Store](AdvancedSkills.md#store)
    - [Display](AdvancedSkills.md#display)
  - [Lambda Architecture](AdvancedSkills.md#lambda-architecture)
    - [Batch Processing](AdvancedSkills.md#batch-processing)
    - [Stream Processing](AdvancedSkills.md#stream-processing)
    - [Should You do Stream or Batch Processing](AdvancedSkills.md#should-you-do-stream-or-batch-processing)
  - [Kappa Architecture](AdvancedSkills.md#kappa-architecture)
  - [Why a Good Data Platform Is Important](AdvancedSkills.md#why-a-good-data-platform-is-important)
- [Data Warehouse vs Data Lake](AdvancedSkills.md#data-warehouse-vs-data-lake)
- [Hadoop Platforms](AdvancedSkills.md#hadoop-platforms)
  - [What is Hadoop](AdvancedSkills.md#what-is-hadoop)
  - [What makes Hadoop so popular](AdvancedSkills.md#what-makes-hadoop-so-popular)
  - [Hadoop Ecosystem Components](AdvancedSkills.md#hadoop-ecosystem-components)
  - [Hadoop is Everywhere?](AdvancedSkills.md#hadoop-is-everywhere)
  - [Should You Learn Hadoop?](AdvancedSkills.md#should-you-learn-hadoop)
  - [How to Select Hadoop Cluster Hardware](AdvancedSkills.md#how-to-select-hadoop-cluster-hardware)
- [Docker](AdvancedSkills.md#docker)
  - [What is Docker and How it Works](AdvancedSkills.md#what-is-docker-and-what-do-you-use-it-for)
    -  [Don't Mess Up Your System](AdvancedSkills.md#dont-mess-up-your-system)
    - [Preconfigured Images](AdvancedSkills.md#preconfigured-images)
    - [Take it With You](AdvancedSkills.md#take-it-with-you)
    - [Kubernetes Container Deployment](AdvancedSkills.md#kubernetes-container-deployment)
    - [How to Create Start and Stop a Container](AdvancedSkills.md#how-to-create-start-stop-a-container)
    - [Docker Micro Services](AdvancedSkills.md#docker-micro-services)
    - [Kubernetes](AdvancedSkills.md#kubernetes)
    - [Why and How To Do Docker Container Orchestration](AdvancedSkills.md#why-and-how-to-do-docker-container-orchestration)
    - [Userful Docker Commands](AdvancedSkills.md#useful-docker-commands)
- [REST APIs](AdvancedSkills.md#rest-apis)
  - [API Design](AdvancedSkills.md#api-design)
  - [Implemenation Frameworks](AdvancedSkills.md#implementation-frameworks)
  - [Security](AdvancedSkills.md#security)
- [Databases](AdvancedSkills.md#databases)
  - [SQL Databases](AdvancedSkills.md#sql-databases)
    - [PostgreSQL DB](AdvancedSkills.md#postgresql-db)
    - [Database Design](AdvancedSkills.md#database-design)
    - [SQL Queries](AdvancedSkills.md#sql-queries)
    - [Stored Procedures](AdvancedSkills.md#stored-procedures)
    - [ODBC/JDBC Server Connections](AdvancedSkills.md#odbc-jdbc-server-connections)
  - [NoSQL Stores](AdvancedSkills.md#nosql-stores)
    - [HBase KeyValue Store](AdvancedSkills.md#keyvalue-stores-hbase)
    - [HDFS Document Store](AdvancedSkills.md#document-stores-hdfs)
    - [MongoDB Document Store](AdvancedSkills.md#document-stores-mongodb)
    - [Elasticsearch Document Store](AdvancedSkills.md#Elasticsearch-search-engine-and-document-store)
    - [Hive Warehouse](AdvancedSkills.md#hive-warehouse)
    - [Impala](AdvancedSkills.md#impala)
    - [Kudu](AdvancedSkills.md#kudu)
    - [Apache Druid](AdvancedSkills.md#apache-druid)
    - [InfluxDB Time Series Database](AdvancedSkills.md#influxdb-time-series-database)
    - [Greenplum MPP Database](AdvancedSkills.md#mpp-databases-greenplum)
- [Data Processing and Analytics](AdvancedSkills.md#data-processing-and-analytics)
  - [Is ETL still relevant for Analytics?](AdvancedSkills.md#is-etl-still-relevant-for-analytics)
  - [Stream Procesing](AdvancedSkills.md#stream-processing)
    - [Three Methods of Streaming](AdvancedSkills.md#three-methods-of-streaming)
    - [At Least Once](AdvancedSkills.md#at-least-once)
    - [At Most Once](AdvancedSkills.md#at-most-once)
    - [Exactly Once](AdvancedSkills.md#exactly-once)
    - [Check The Tools](AdvancedSkills.md#check-the-tools)
  - [MapReduce](AdvancedSkills.md#mapreduce)
    - [How Does MapReduce Work](AdvancedSkills.md#How-does-mapreduce-work)
    - [MapReduce](AdvancedSkills.md#mapreduce)
    - [MapReduce Example](AdvancedSkills.md#example)
    - [MapReduce Limitations](AdvancedSkills.md#What-is-the-limitation-of-mapreduce)
  - [Apache Spark](AdvancedSkills.md#apache-spark)
    - [What is the Difference to MapReduce?](AdvancedSkills.md#what-is-the-difference-to-MapReduce)
    - [How Spark Fits to Hadoop](AdvancedSkills.md#how-does-spark-fit-to-hadoop)
    - [Spark vs Hadoop](AdvancedSkills.md#wheres-the-difference)
    - [Spark and Hadoop a Perfect Fit](AdvancedSkills.md#spark-and-hadoop-is-a-perfect-fit)
    - [Spark on YARn](AdvancedSkills.md#spark-on-yarn)
    - [My Simple Rule of Thumb](AdvancedSkills.md#my-simple-rule-of-thumb)
    - [Available Languages](AdvancedSkills.md#available-languages)
    - [Spark Driver Executor and SparkContext](AdvancedSkills.md#how-spark-works-driver-executor-sparkcontext)
    - [Spark Batch vs Stream processing](AdvancedSkills.md#spark-batch-vs-stream-processing)
    - [How Spark uses Data From Hadoop](AdvancedSkills.md#How-does-spark-use-data-from-hadoop)
    - [What are RDDs and How to Use Them](AdvancedSkills.md#what-are-rdds-and-how-to-use-them)
    - [SparkSQL How and Why to Use It](AdvancedSkills.md#available-languages)
    - [What are Dataframes and How to Use Them](AdvancedSkills.md#what-are-dataframes-how-to-use-them)
    - [Machine Learning on Spark (TensorFlow)](AdvancedSkills.md#machine-learning-on-spark-tensor-flow)
    - [MLlib](AdvancedSkills.md#mllib)
    - [Spark Setup](AdvancedSkills.md#spark-setup)
    - [Spark Resource Management](AdvancedSkills.md#spark-resource-management)
  - [Apache Nifi](AdvancedSkills.md#apache-nifi)
  - [StreamSets](AdvancedSkills.md#streamsets)
  - [Apache Kafka](AdvancedSkills.md#apache-kafka)
    - [Why a Message Queue Tool?](AdvancedSkills.md#why-a-message-queue-tool)
    - [Kafka Architecture](AdvancedSkills.md#kafka-architecture)
    - [Kafka Topics](AdvancedSkills.md#what-are-topics)
    - [Kafka and Zookeeper](AdvancedSkills.md#what-does-zookeeper-have-to-do-with-kafka)
    - [How to Produce and Consume Messages](AdvancedSkills.md#how-to-produce-and-consume-messages)
    - [Kafka Commands](AdvancedSkills.md#kafka-commands)
  - [Machine Learning](AdvancedSkills.md#machine-learning)
    - [How to do Machine Learning in production](AdvancedSkills.md#how-to-domachine-learning-in-production)
    - [Why machine learning in production is harder then you think](AdvancedSkills.md#why-machine-learning-in-production-is-harder-then-you-think)
    - [Models Do Not Work Forever](AdvancedSkills.md#models-do-not-work-forever)
    - [Where are The Platforms That Support Machine Learning](AdvancedSkills.md#where-are-the-platforms-that-support-this)
    - [Training Parameter Management](AdvancedSkills.md#training-parameter-management)
    - [How to Convince People That Machine Learning Works](AdvancedSkills.md#how-to-convince-people-machine-learning-works)
    - [No Rules No Physical Models](AdvancedSkills.md#no-rules-no-physical-models)
    - [You Have The Data. Use It!](AdvancedSkills.md#you-have-the-data-use-it)
    - [Data is Stronger Than Opinions](AdvancedSkills.md#data-is-stronger-than-opinions)
    - [AWS Sagemaker](AdvancedSkills.md#aws-sagemaker)
- [Data Visualization](AdvancedSkills.md#data-visualization)
  - [Android and IOS](AdvancedSkills.md#android-and-ios)
  - [API Design for Mobile Apps](AdvancedSkills.md#how-to-design-apis-for-mobile-apps)
  - [Webservers](AdvancedSkills.md#how-to-use-webservers-to-display-content)
    - [Tomcat](AdvancedSkills.md#tomcat)
    - [Jetty](AdvancedSkills.md#jetty)
    - [NodeRED](AdvancedSkills.md#nodered)
    - [React](AdvancedSkills.md#react)
  - [Business Intelligence Tools](AdvancedSkills.md#business-intelligence-tools)
    - [Tableau](AdvancedSkills.md#tableau)
    - [Power BI](AdvancedSkills.md#power-bi)
    - [Quliksense](AdvancedSkills.md#quliksense)
  - [Identity & Device Management](AdvancedSkills.md#Identity-and-device-management)
    - [What Is A Digital Twin](AdvancedSkills.md#what-is-a-digital-twin)
    - [Active Directory](AdvancedSkills.md#active-directory)

# Hands On Course

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

# 1001 Interview Questions

- [Interview Questions](InterviewQuesitons.md)

In part two you will learn the basic data engineering skills
Part three contains a real world data engineering example we currently work on
The fourth part contains over 30 case studies with links from companies like Netflix, Twitter, Spotify
Part five is a collection of one thousand and one interview questions (currently approx. 150)

## How to contribute
If you have some cool links or topics for the cookbook, please become a contributor.
Simply open an issue and add your links. Or pull the repo, add them and create a pull request.

Please pull only the "working-branch" branch. \
This way we keep the master branch clean and I don't have to mess around resolving conflicts. You just need to change the .tex file. I'll recompile it later when I merge the branch with the master

For comments please also use the "Issues" function.

## Support

Everything is free, but please support what you like! \
Join my Patreon and become a plumber yourself:
[Link to my Patreon](https://patreon.com/plumbersofds)

Or support me and send a message through Paypal.me:
[Link to my Paypal.me/feedthestream](https://paypal.me/feedthestream)
## Important links

Subscribe to my Plumbers of data science YouTube channel:
[Link to YouTube](https://www.youtube.com/channel/UCY8mzqqGwl5_bTpBY9qLMAA)

Check out my personal blog. Get updated via mail and get on my mailing list:
[andreaskretz.com](https://andreaskretz.com)

I have a Medium publication where you can publish your data engineer articles:
[Medium publication](https://link.medium.com/9oi1VDrhPW)
