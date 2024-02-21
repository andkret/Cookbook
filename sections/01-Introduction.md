
Introduction
============

## Contents

- [What is this Cookbook](01-Introduction.md#what-is-this-cookbook)
- [Data Engineers](01-Introduction.md#data-engineers)
- [My Data Science Platform Blueprint](01-Introduction.md#my-data-science-platform-blueprint)
  - [Connect](01-Introduction.md#connect)
  - [Buffer](01-Introduction.md#buffer)
  - [Processing Framework](01-Introduction.md#processing-framework)
  - [Store](01-Introduction.md#store)
  - [Visualize](01-Introduction.md#visualize)
- [Who Companies Need](01-Introduction.md#who-companies-need)
- [How to Learn Data Engineering](01-Introduction.md#how-to-learn-data-engineering)
  - [Building Blocks to Learn Data Engineering](01-Introduction.md#building-blocks-to-learn-data-engineering)
  - [Roadmap for Data  Analysts](01-Introduction.md#roadmap-for-data-analysts)
  - [Roadmap for Software Developers](01-Introduction.md#roadmap-for-data-analysts)

## What is this Cookbook

I get asked a lot:
"What do you actually need to learn to become an awesome data engineer?"

Well, look no further. You'll find it here!

If you are looking for AI algorithms and such data scientist things,
this book is not for you.

**How to use this Cookbook:**
This book is intended to be a starting point for you. It is not a training! I want to help you to identify the topics to look into to become an awesome data engineer in the process.

It hinges on my Data Science Platform Blueprint. Check it out below. Once you understand it, you can find in the book tools that fit into each key area of a Data Science platform (Connect, Buffer, Processing Framework, Store, Visualize).

Select a few tools you are interested in, then research and work with them.

Don't learn everything in this book! Focus.

**What types of content are in this book?**
You are going to find five types of content in this book: Articles
I wrote, links to my podcast episodes (video & audio), more than 200
links to helpful websites I like, data engineering interview questions
and case studies.

**This book is a work in progress!**
As you can see, this book is not finished. I'm constantly adding new
stuff and doing videos for the topics. But, obviously, because I do this
as a hobby, my time is limited. You can help make this book even
better.

**Help make this book awesome!**
If you have some cool links or topics for the cookbook, please become a
contributor on GitHub: <https://github.com/andkret/Cookbook>. Fork the
repo, add them, and create a pull request. Or join the discussion by
opening Issues. Tell me your thoughts, what you value,
what you think should be included, or correct me where I am wrong.
You can also write me an email any time to
plumbersofdatascience\@gmail.com anytime.

**This Cookbook is and will always be free!**


## If You Like This Book & Need More Help:
Check out my Data Engineering Academy at LearnDataEngineering.com

**Visit learndataengineering.com:** [Click Here](https://learndataengineering.com)

- Huge Step by step Data Engineering Academy with over 30 courses
- Unlimited access incl. future courses during subsciption
- Access to all courses and example projects in the Academy
- Associate Data Engineer Certification
- Data Engineering on AWS E-Commerce example project
- Microsoft Azure example project
- Document Streaming example project with Docker, FastAPI, Apache Kafka, Apache Spark,
- MongoDB and Streamlit
- Time Series example project with InfluxDB and Grafana
- Lifetime access to the private Discord Workspace
- Course certificates
- Currently over 54 hours of videos


## Support This Book For Free!
- **Amazon:** [Click Here](https://www.amazon.com/shop/plumbersofdatascience) buy whatever you like from Amazon using this link* (Also check out my complete podcast gear and books)


## How To Contribute
If you have some cool links or topics for the cookbook, please become a contributor.

Simply pull the repo, add your ideas and create a pull request.
You can also open an issue and put your thoughts there.

Please use the "Issues" function for comments.



Data Engineers
-------------------------------


Data Engineers are the link between the management's data strategy
and the data scientists or analysts that need to work with data.

What they do is build the platforms that enable data scientists to do
their magic.

These platforms are usually used in five different ways:

-   Data ingestion and storage of large amounts of data.

-   Algorithm creation by data scientists.

-   Automation of the data scientist's machine learning models and
    algorithms for production use.

-   Data visualization for employees and customers.

-   Most of the time these guys start as traditional solution architects
    for systems that involve SQL databases, web servers, SAP
    installations and other "standard" systems.

But, to create big data platforms, the engineer needs to be an expert in
specifying, setting up, and maintaining big data technologies like:
Hadoop, Spark, HBase, Cassandra, MongoDB, Kafka, Redis, and more.

What they also need is experience on how to deploy systems on cloud
infrastructure like at Amazon or Google, or on-premise hardware.


| Podcast Episode: #048 From Wannabe Data Scientist To Engineer My Journey
|------------------|
|In this episode Kate Strachnyi interviews me for her humans of data science podcast. We talk about how I found out that I am more into the engineering part of data science.  
| [Watch on YouTube](https://youtu.be/pIZkTuN5AMM) \ [Listen on Anchor](https://anchor.fm/andreaskayy/episodes/048-From-Wannabe-Data-Scientist-To-Engineer-My-Journey-e45i2o)|


## My Data Science Platform Blueprint

I have created a simple and modular big data platform
blueprint. It is based on what I have seen in the field and
read in tech blogs all over the internet.

Why do I believe it will be super useful to you?

Because, unlike other blueprints, it is not focused on technology.

Following my blueprint will allow you to create the big data platform
that fits exactly your needs. Building the perfect platform will allow
data scientists to discover new insights.

It will enable you to perfectly handle big data and allow you to make
data-driven decisions.

The blueprint is focused on the five key areas: Connect, Buffer, Processing Frameworks, Store, and Visualize.

![Data Science Platform Blueprint](/images/Data-Science-Blueprint-New.jpg)

Having the platform split like this turns it into a modular platform with
loosely coupled interfaces.

Why is it so important to have a modular platform?

If you have a platform that is not modular, you end up with something
that is fixed or hard to modify. This means you can not adjust the
platform to changing requirements of the company.

Because of modularity, it is possible to specifically select tools for your use case. It also allows you to replace every component, if you need it.

Now, lets talk more about each key area.

### Connect

Ingestion is all about getting the data in from the source and making it
available to later stages. Sources can be everything from tweets to server
logs, to IoT sensor data (e.g. from cars).

Sources send data to your API Services. The API is going to push the
data into temporary storage.

The temporary storage allows other stages simple and fast access to
incoming data.

A great solution is to use messaging queue systems like Apache Kafka,
RabbitMQ or AWS Kinesis. Sometimes people also use caches for
specialised applications like Redis.

A good practice is that the temporary storage follows the
publish-subscribe pattern. This way APIs can publish messages and
Analytics can quickly consume them.

### Buffer

In the buffer phase you have pub/sub systems like Apache Kafka, Redis, or other Cloud tools like Google pub/sub or AWS Kinesis.

These systems are more or less message Queues.
You put something in on one side and take it out on the other.

The idea behind buffers is to have an intermediate system for the incoming data.

How this works is, for instance, you're getting data in from from an API.
The API is publishing into the message queue. Data is buffered there until it is picked up by the processing.

If you don't have a buffer, you can run into problems when writing directly into a store or you're processing the data directly. You can always have peaks of incoming data that stall the systems.

Like, it's lunch break and people are working with your app way more than usual.
There's more data coming in very very fast, faster than the analytics of the storage can handle.

In this case, you would run into problems, because the whole system would stall. It would therefore take long to process the data, and your customers would be annoyed.

With a buffer, you buffer the incoming data. Processes for storage and analytics can take out only as much data as they can process. You are no longer in danger of overpowering systems.

Buffers are also really good for building pipelines.

You take data out of Kafka, pre-process it, and put it back into Kafka.
Then, with another analytics process, you take the processed data back out and put it into a store.

Ta-da! A pipeline.

### Processing Framework

The analyse stage is where the actual analytics is done in
the form of stream and batch processing.

Streaming data is taken from ingest and fed into analytics. Streaming
analyses the "live" data, thus generating fast results.

As the central and most important stage, analytics also has access to
the big data storage. Because of that connection, analytics can take a
big chunk of data and analyse it.

This type of analysis is called batch processing. It will deliver you
answers for the big questions.

For a short video about batch and stream processing and their use cases, click on the link below:

[Adding Batch to a Streaming Pipeline](https://www.youtube.com/watch?v=o-aGi3FmdfU)

The analytics process, batch or streaming, is not a one-way process.
Analytics can also write data back to the big data storage.

Oftentimes, writing data back to the storage makes sense. It allows you
to combine previous analytics outputs with the raw data.

Analytics give insights when you combine
raw data. This combination will often allow you to create even more
useful insights.

A wide variety of analytics tools are available. Ranging from MapReduce
or AWS Elastic MapReduce to Apache Spark and AWS lambda.

### Store

This is the typical big-data storage where you just store everything. It
enables you to analyse the big picture.

Most of the data might seem useless for now, but it is of utmost
importance to keep it. Throwing data away is a big no-no.

Why not throw something away when it is useless?

Although it seems useless for now, data scientists can work with the
data. They might find new ways to analyse the data and generate valuable
insights from it.

What kind of systems can be used to store big data?

Systems like Hadoop HDFS, Hbase, Amazon S3 or DynamoDB are a perfect fit
to store big data.

Check out my podcast how to decide between SQL and NoSQL:
<https://anchor.fm/andreaskayy/embed/episodes/NoSQL-Vs-SQL-How-To-Choose-e12f1o>

### Visualize

Displaying data is as important as ingesting, storing, and analysing it.
Visualizations enable business users to make data-driven decisions.

This is why it is important to have a good visual presentation of the
data. Sometimes you have a lot of different use cases or projects using
the platform.

It might not be possible to build the perfect UI that fits
everyone's needs. What you should do in this case is enable others to build the
perfect UI themselves.

How to do that? By creating APIs to access the data and making them
available to developers.

Either way, UI or API, the trick is to give the display stage direct
access to the data in the big-data cluster. This kind of access will
allow the developers to use analytics results as well as raw data to
build the perfect application.


## Who Companies Need

For a company, it is important to have well-trained data engineers.

That's why companies are looking for people with experience of tools in every part of the above platform blueprint. One common theme I see is cloud platform experience on AWS, Azure or GCP.

## How to Learn Data Engineering

### Building Blocks to Learn Data Engineering

The following Roadmaps all hinge on the courses in my Data Engineering Academy. They are designed to help students who come from many different professions and enable to build a customized curriculum.

Here are all the courses currently available February 2024:

**Colors:** Blue (The Basics), Green (Platform & Pipeline Fundamentals), Orange (Fundamental Tools), Red (Example Projects)

![Building blocks of your curriculum](/images/All-Courses-at-Learn-Data-Engineering.jpg)


### Roadmap for Data Analysts

![Building blocks of your curriculum](/images/Data-Engineering-Roadmap-for-Data-Analysts.jpg)

| Live Stream -> Roadmap: Data Engineering for Data Analysts!
|------------------|
|In this live stream I was showing step by step how to read this roadmap for Analysts, why I chose these tools and why I think this is the right way to do it. I also answered many questions from the audience.  
| [Watch on YouTube](https://youtube.com/live/w2t6SL5tQG0?feature=share)|

### Roadmap for Software Engineers

![Building blocks of your curriculum](/images/Data-Engineering-Roadmap-for-Software-Engineers.jpg)
