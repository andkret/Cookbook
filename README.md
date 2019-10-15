<!--- # The Data Engineering Cookbook -->

<div align="center">
	<img width="341" height="426" src="images/CookbookCover.jpg" alt="Data Engineering Cookbook">
	<br>
	<br>
	<br>
</div>

<p align="center">
	<a href="Introduction.md">What is this Book?</a>&nbsp;&nbsp;&nbsp;
  <a href="https://github.com/andkret/Cookbook/raw/LaTex-Version-Deprecated/Data%20Engineering%20Cookbook.pdf">Download PDF</a>&nbsp;&nbsp;&nbsp;
  <a href="#how-to-contribute">How to Contribute</a>&nbsp;&nbsp;&nbsp;
  <a href="https://www.youtube.com/channel/UCY8mzqqGwl5_bTpBY9qLMAA">YouTube</a>&nbsp;&nbsp;&nbsp;
	<a
  <a href="https://twitter.com/andreaskayy">Twitter</a>&nbsp;&nbsp;&nbsp;
  <a href="https://www.amazon.com/shop/plumbersofdatascience">Amazon Shop</a>
</p>

<!---
I get asked super often how to become a Data Engineer.
That's why I decided to start this cookbook with all the topics you need to look into.

It's not only useful for beginners, professionals will definitely like the case study section.

If you look for the old PDF version it's [here](https://github.com/andkret/Cookbook/raw/LaTex-Version-Deprecated/Data%20Engineering%20Cookbook.pdf)

-->
<br>

## Contents:
- [Introduction](#introduction)
- [Basic Engineering Skills](#basic-engineering-skills)
- [Advanced Engineering Skills](#introduction)
- [Hands On Course](#Hands-on-course)‚
- [Case Studies](#case-studies)
- [1001 Interview Questions](#1001-interview-questions)
- [Recommended Books and Courses](BooksAndCourses.md)
<!-- -->

- [How To Contribute](#how-to-contribute)
- [Support What You Like](#support)
- [Important Links](#important-links)


##  Introduction
- [What is this Cookbook](Introduction.md#what-is-this-cookbook)
- [Data Engineer vs Data Scientist](Introduction.md#data-engineer-vs-data-scientist)
  - [Data Scientist](Introduction.md#data-scientist)
  - [Data Engineer](Introduction.md#data-engineer)
- [My Big Data Platform Blueprint](Introduction.md#my-big-data-platform-blueprint)
  - [Connect](Introduction.md#connect)
  - [Buffer](Introduction.md#buffer)
  - [Processing Framework](Introduction.md#processing-framework)
  - [Store](Introduction.md#store)
  - [Visualize](Introduction.md#visualize)
- [Who Companies Need](Introduction.md#who-companies-need)

## Basic Engineering Skills
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
- [Docker](BasicSkills.md#docker)
  - [What is Docker and How it Works](BasicSkills.md#what-is-docker-and-what-do-you-use-it-for)
    -  [Don't Mess Up Your System](BasicSkills.md#dont-mess-up-your-system)
    - [Preconfigured Images](BasicSkills.md#preconfigured-images)
    - [Take it With You](BasicSkills.md#take-it-with-you)
    - [Kubernetes Container Deployment](BasicSkills.md#kubernetes-container-deployment)
    - [How to Create Start and Stop a Container](BasicSkills.md#how-to-create-start-stop-a-container)
    - [Docker Micro Services](BasicSkills.md#docker-micro-services)
    - [Kubernetes](BasicSkills.md#kubernetes)
    - [Why and How To Do Docker Container Orchestration](BasicSkills.md#why-and-how-to-do-docker-container-orchestration)
    - [Userful Docker Commands](BasicSkills.md#useful-docker-commands)
- [The Cloud](BasicSkills.md#the-cloud)
  - [IaaS vs PaaS vs SaaS](BasicSkills.md#iaas-vs-paas-vs-saas)
  - [AWS Azure IBM Google IBM](BasicSkills.md#aws-azure-ibm-google)
  - [Cloud vs On-Premises](BasicSkills.md#cloud-vs-on-premises)
  - [Security](BasicSkills.md#security)
  - [Hybrid Clouds](BasicSkills.md#hybrid-clouds)
- [Security Zone Design](BasicSkills.md#security-zone-design)
  - [How to secure a multi layered application](BasicSkills.md#how-to-secure-a-multi-layered-application)
  - [Cluster security with Kerberos](BasicSkills.md#cluster-security-with-kerberos)

## Advanced Engineering Skills
- [Data Science Platform](AdvancedSkills.md#data-science-platform)
  - [Why a Good Data Platform Is Important](AdvancedSkills.md#why-a-good-data-platform-is-important)
  - [Big Data vs Data Science and Analytics](AdvancedSkills.md#Big-Data-vs-Data-Science-and-Analytics)
  - [The 4 Vs of Big Data](AdvancedSkills.md#the-4-vs-of-big-data)
  - [Why Big Data](AdvancedSkills.md#why-big-data)
    - [Planning is Everything](AdvancedSkills.md#planning-is-everything)
    - [The Problem with ETL](AdvancedSkills.md#the-problem-with-etl)
    - [Scaling Up](AdvancedSkills.md#scaling-up)
    - [Scaling Out](AdvancedSkills.md#scaling-out)
    - [When not to Do Big Data](AdvancedSkills.md#please-dont-go-big-data)
  - [Lambda and Kappa Architecture](AdvancedSkills.md#lambda-and-kappa-architecture)
  - [Batch Processing](AdvancedSkills.md#batch-processing)
  - [Stream Processing](AdvancedSkills.md#stream-processing)
    - [Three Methods of Streaming](AdvancedSkills.md#three-methods-of-streaming)
    - [At Least Once](AdvancedSkills.md#at-least-once)
    - [At Most Once](AdvancedSkills.md#at-most-once)
    - [Exactly Once](AdvancedSkills.md#exactly-once)
    - [Check The Tools](AdvancedSkills.md#check-the-tools)
  - [Should You do Stream or Batch Processing](AdvancedSkills.md#should-you-do-stream-or-batch-processing)
- [Hadoop Platforms](AdvancedSkills.md#hadoop-platforms)
  - [What is Hadoop](AdvancedSkills.md#what-is-hadoop)
  - [What makes Hadoop so popular](AdvancedSkills.md#what-makes-hadoop-so-popular)
  - [Hadoop Ecosystem Components](AdvancedSkills.md#hadoop-ecosystem-components)
  - [Hadoop is Everywhere?](AdvancedSkills.md#hadoop-is-everywhere)
  - [Should You Learn Hadoop?](AdvancedSkills.md#should-you-learn-hadoop)
  - [How to Select Hadoop Cluster Hardware](AdvancedSkills.md#how-to-select-hadoop-cluster-hardware)
- [Connect](AdvancedSkills.md#connect)
  - [REST APIs](AdvancedSkills.md#rest-apis)
    - [API Design](AdvancedSkills.md#api-design)
    - [Implemenation Frameworks](AdvancedSkills.md#implementation-frameworks)
    - [Security](AdvancedSkills.md#security)
  - [Apache Nifi](AdvancedSkills.md#apache-nifi)
  - [Logstash](AdvancedSkills.md#logstash)
- [Buffer](AdvancedSkills.md#buffer)
  - [Apache Kafka](AdvancedSkills.md#apache-kafka)
    - [Why a Message Queue Tool?](AdvancedSkills.md#why-a-message-queue-tool)
    - [Kafka Architecture](AdvancedSkills.md#kafka-architecture)
    - [Kafka Topics](AdvancedSkills.md#what-are-topics)
    - [Kafka and Zookeeper](AdvancedSkills.md#what-does-zookeeper-have-to-do-with-kafka)
    - [How to Produce and Consume Messages](AdvancedSkills.md#how-to-produce-and-consume-messages)
    - [Kafka Commands](AdvancedSkills.md#kafka-commands)
  - [Apache Redis Pub-Sub](AdvancedSkills.md#redis-pub-sub)
  - [AWS Kinesis](AdvancedSkills.md#apache-kafka)
  - [Google Cloud PubSub](AdvancedSkills.md#google-cloud-pubsub)
- [Processing Frameworks](AdvancedSkills.md#processing-frameworks)
  - [Is ETL still relevant for Analytics?](AdvancedSkills.md#is-etl-still-relevant-for-analytics)
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
  - [AWS Lambda](AdvancedSkills.md#apache-flink)  
  - [Apache Flink](AdvancedSkills.md#apache-flink)
  - [Elasticsearch](AdvancedSkills.md#elasticsearch)
  - [Apache Drill](AdvancedSkills.md#apache-drill)
  - [StreamSets](AdvancedSkills.md#streamsets)
- [Store](AdvancedSkills.md#store)
  - [Data Warehouse vs Data Lake](AdvancedSkills.md#data-warehouse-vs-data-lake)
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
- [Visualize](AdvancedSkills.md#visualize)
  - [Android and IOS](AdvancedSkills.md#android-and-ios)
  - [API Design for Mobile Apps](AdvancedSkills.md#how-to-design-apis-for-mobile-apps)
  - [Dashboards](AdvancedSkills.md#dashboards)
    - [Grafana](AdvancedSkills.md#grafana)
    - [Kibana](AdvancedSkills.md#kibana)
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


## Hands On Course

- [What We Want To Do](HandsOnCourse.md#what-we-want-to-do)
- [Thoughts On Choosing A Development Environment](HandsOnCourse.md#thoughts-on-choosing-a-development-environment)
- [A Look Into the Twitter API](HandsOnCourse.md#a-look-into-the-twiiter-api)
- [Ingesting Tweets with Apache Nifi](HandsOnCourse.md#ingesting-tweets-with-apache-nifi)
- [Writing from Nifi to Apache Kafka](HandsOnCourse.md#writing-from-nifi-to-kafka)
- [Apache Zeppelin Data Processing](HandsOnCourse.md#apache-zeppelin)
  - [Install and Ingest Kafka Topic](HandsOnCourse.md#install-and-ingest-kafka-topic)
  - [Processing Messages with Spark & SparkSQL](HandsOnCourse.md#processing-messages-with-spark-and-sparksql)
  - [Visualizing Data](HandsOnCourse.md#visualizing-data)
- [Switch Processing from Zeppelin to Spark](HandsOnCourse.md#switch-processing-from-zeppelin-to-spark)

## Case Studies

- [Data Science @Airbnb](CaseStudies.md#data-science-at-Airbnb)
- [Data Science @Amazon](CaseStudies.md#data-science-at-Amazon)
- [Data Science @Baidu](CaseStudies.md#data-science-at-Baidu)
- [Data Science @Blackrock](CaseStudies.md#data-science-at-Blackrock)
- [Data Science @BMW](CaseStudies.md#data-science-at-BMW)
- [Data Science @Booking.com](CaseStudies.md#data-science-at-Booking.com)
- [Data Science @CERN](CaseStudies.md#data-science-at-CERN)
- [Data Science @Disney](CaseStudies.md#data-science-at-Disney)
- [Data Science @DLR](CaseStudies.md#data-science-at-DLR)
- [Data Science @Drivetribe](CaseStudies.md#data-science-at-Drivetribe)
- [Data Science @Dropbox](CaseStudies.md#data-science-at-Dropbox)
- [Data Science @Ebay](CaseStudies.md#data-science-at-Ebay)
- [Data Science @Expedia](CaseStudies.md#data-science-at-Expedia)
- [Data Science @Facebook](CaseStudies.md#data-science-at-Facebook)
- [Data Science @Google](CaseStudies.md#data-science-at-Google)
- [Data Science @Grammarly](CaseStudies.md#data-science-at-Grammarly)
- [Data Science @ING Fraud](CaseStudies.md#data-science-at-ING-Fraud)
- [Data Science @Instagram](CaseStudies.md#data-science-at-Instagram)
- [Data Science @LinkedIn](CaseStudies.md#data-science-at-LinkedIn)
- [Data Science @Lyft](CaseStudies.md#data-science-at-Lyft)
- [Data Science @NASA](CaseStudies.md#data-science-at-NASA)
- [Data Science @Netflix](CaseStudies.md#data-science-at-Netflix)
- [Data Science @OLX](CaseStudies.md#data-science-at-OLX)
- [Data Science @OTTO](CaseStudies.md#data-science-at-OTTO)
- [Data Science @Paypal](CaseStudies.md#data-science-at-Paypal)
- [Data Science @Pinterest](CaseStudies.md#data-science-at-Pinterest)
- [Data Science @Salesforce](CaseStudies.md#data-science-at-Salesforce)
- [Data Science @Siemens Mindsphere](CaseStudies.md#data-science-at-Siemens-Mindsphere)
- [Data Science @Slack](CaseStudies.md#data-science-at-Slack)
- [Data Science @Spotify](CaseStudies.md#data-science-at-Spotify)
- [Data Science @Symantec](CaseStudies.md#data-science-at-Symantec)
- [Data Science @Tinder](CaseStudies.md#data-science-at-Tinder)
- [Data Science @Twitter](CaseStudies.md#data-science-at-Twitter)
- [Data Science @Uber](CaseStudies.md#data-science-at-Uber)
- [Data Science @Upwork](CaseStudies.md#data-science-at-Upwork)
- [Data Science @Woot](CaseStudies.md#data-science-at-Woot)
- [Data Science @Zalando](CaseStudies.md#data-science-at-Zalando)

## 1001 Interview Questions

- [Interview Questions](InterviewQuestions.md)

## Recommended Books and Courses

- [Books and Courses](BooksAndCourses.md)


## How To Contribute
If you have some cool links or topics for the cookbook, please become a contributor.

Simply pull the repo, add your ideas and create a pull request.
You can also open an issue and put your thoughts there.

Please use the "Issues" function for comments.

## Support

Everything is free, but please support what you like!
Join my Patreon and become a plumber yourself:
[Link to my Patreon](https://patreon.com/plumbersofds)

Or support me and send a message through Paypal.me:
[Link to my Paypal.me/feedthestream](https://paypal.me/feedthestream)
## Important Links

Subscribe to my Plumbers of Data Science YouTube channel for regular updates:
[Link to YouTube](https://www.youtube.com/channel/UCY8mzqqGwl5_bTpBY9qLMAA)

Check out my blog and get updated via mail by joining my mailing list:
[andreaskretz.com](https://andreaskretz.com)

I have a Medium publication where you can publish your data engineer articles to reach more people:
[Medium publication](https://link.medium.com/9oi1VDrhPW)
