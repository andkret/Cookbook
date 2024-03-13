
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
  - [Roadmap for Data Scientists](01-Introduction.md#roadmap-for-data-scientists)
  - [Roadmap for Software Engineers](01-Introduction.md#roadmap-for-software-engineers)
- [Data Engineers Skills Matrix](01-Introduction.md#data-engineers-skills-matrix)
- [How to Become a Senior Data Engineer](01-Introduction.md#how-to-become-a-senior-data-engineer)



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

I always advise my students to begin with familiar concepts and knowledge, then expand from there. As a data analyst working with data warehousing and report preparation, one might wonder where to start. Rather than diving into basics, it's beneficial to begin with understanding platform and pipeline fundamentals. This includes grasping the architecture of platforms and proceeding to more advanced topics.

For instance, if you're familiar with data warehousing, you might explore BigQuery for warehousing or delve into the lakehouse concept on Snowflake or Google Cloud Platform (GCP). The ease of setup with these platforms allows for immediate application of existing knowledge through data uploading and manipulation. Additionally, our course offerings, such as one on Snowflake with DBT, enable further exploration into data transformation within these environments.

The next step involves selecting appropriate data stores, understanding the differences between OLTP (Online Transaction Processing) databases and analytical data stores, including NoSQL and traditional relational databases. This understanding is crucial for effective data modeling, which we cover in our courses, offering insights into various database modeling techniques.

Moreover, for those interested in non-relational databases, MongoDB presents a valuable opportunity to skip relational data modeling in favor of document stores, leveraging prior knowledge in warehousing and dimensional modeling.

Python skills, even at a basic level, are essential for data engineers. Our Python for Data Engineers course aims to enhance understanding of data transformation tools and techniques. This knowledge, combined with insights into data warehousing, platform functionality, data modeling, and store selection, equips you with the skills to utilize Python in data engineering effectively.

For analysts ready to explore further, projects focusing on fundamental tools and platforms become the next step. Whether it's building streaming data pipelines in Azure that integrate with NoSQL databases like Cosmos DB, or diving into relational data modeling on GCP, there's a wealth of paths to explore. Our courses also cover modern data warehouses and lakehouses on both AWS and GCP, providing comprehensive knowledge on data integration and management.

Additionally, understanding Docker fundamentals opens up possibilities for containerization and machine learning projects, further enhancing your toolkit. From there, diving into Spark fundamentals, learning Kafka for data streaming, and mastering APIs can lead to developing end-to-end streaming projects with user interfaces.

In summary, the journey from understanding basic platform and pipeline concepts to mastering advanced data engineering tools and techniques is a gradual process. By focusing on familiar areas and progressively expanding your skill set, you can achieve a solid foundation in data engineering. This approach, especially if documented well, can set you apart in the field, even at an entry-level or junior position.

| Live Stream -> Roadmap: Data Engineering for Data Analysts!
|------------------|
|In this live stream I was showing step by step how to read this roadmap for Analysts, why I chose these tools and why I think this is the right way to do it. I also answered many questions from the audience.  
| [Watch on YouTube](https://youtube.com/live/w2t6SL5tQG0)|

### Roadmap for Data Scientists

![Building blocks of your curriculum](/images/Data-Engineering-Roadmap-for-Data-Scientists.jpg)

We’re going to tackle the data engineering roadmap for data scientists. It's a topic a lot of you have been curious about, especially after we explored the data analyst side of things. The goal here is to lay out a step-by-step path for those of you looking to make a pivot or deepen your understanding of data engineering.

The first thing I did was sit down and list out all the courses available in my academy. It’s designed to be super flexible, catering to different job roles. For a data scientist, your journey usually starts with a strong grasp of data science fundamentals, right? You know your way around machine learning, how to preprocess data, and maybe even deploy models on a basic level. But then, the question arises: How do you set up an entire platform or pipeline that takes data from ingestion to a point where it’s usable for others?

Here’s where it gets interesting. I thought about how we could structure this to really benefit data scientists. Starting with the basics, like platform and pipeline design, and then moving into choosing data storage solutions. We’re talking about understanding the differences between databases and when to use each type.

But it doesn’t stop there. I’ve included some optional topics, like platform security, because it’s always handy to know, even if you’re not directly responsible for it. And since you’re already familiar with data, why not dive deeper into data modeling? It’s all about making your data work for you in the most efficient way possible.

Now, let's talk about Docker. It's a game-changer for deploying your algorithms. And after that, mastering API fundamentals and streaming with Apache Kafka will open up new possibilities for your projects.

Depending on your interests or where you see yourself in the future, you might want to explore cloud services like AWS, GCP, or Azure. Or maybe you’re more intrigued by the idea of document streaming and creating user interfaces with MongoDB and Streamlit. The roadmap I’ve laid out includes paths for all these directions.

Monitoring and observability are crucial, too. You’ll want to keep an eye on your algorithms and the data flowing through your systems. Tools like Elasticsearch or InfluxDB paired with Grafana can give you those insights.

And don’t forget about orchestration with Airflow. It’s all about keeping your workflows organized and efficient.

So, this roadmap is more than just a list of topics. It’s about building a foundation that lets you, as a data scientist, expand into data engineering seamlessly. It’s about understanding the ecosystem around your data and how to leverage it to build robust, scalable solutions.

| Live Stream -> Roadmap: Data Engineering for Data Scientists!
|------------------|
|In this live stream you'll find even more details how to read this roadmap for Data Scientists, why I chose these tools and why I think this is the right way to do it. I also answered many questions from the audience.  
| [Watch on YouTube](https://youtube.com/live/fusLAtA1Eu4)|

### Roadmap for Software Engineers

![Building blocks of your curriculum](/images/Data-Engineering-Roadmap-for-Software-Engineers.jpg)


## Data Engineers Skills Matrix

![Data Engineer Skills Matrix](/images/Data-Engineer-Skills-Matrix.jpg)

If you're diving into the world of data engineering or looking to climb the ladder within this field, you're in for a treat with this enlightening YouTube video. Andreas kicks things off by introducing us to a very handy tool they've developed: the Data Engineering Skills Matrix. This isn't just any chart; it's a roadmap designed to navigate the complex landscape of data engineering roles, ranging from a Junior Data Engineer to the lofty heights of a Data Architect and Machine Learning Engineer.

| Live Stream -> Data Engineering Skills Matrix
|------------------|
|In this live stream you'll find even more details how to read this skills matrix for Data Engineers.  
| [Watch on YouTube](https://youtube.com/live/5E0UiBy0Kwo)|

Andreas takes us through the intricacies of this matrix, layer by layer. Starting with the basics, they discuss the minimum experience needed for each role. It's an eye-opener, especially when you see how experience requirements evolve from a beginner to senior levels. But it's not just about how many years you've spent in the field; it's about the skills you've honed during that time.

### Challenges & Responsibilities

As the conversation progresses, Andreas delves into the core responsibilities and main tasks associated with each role. You'll learn what sets a Junior Data Engineer apart from a Senior Data Engineer, the unique challenges a Data Architect faces, and the critical skills a Machine Learning Engineer must possess. This part of the video is golden for anyone trying to understand where they fit in the data engineering ecosystem or plotting their next career move.

### SQL & Soft Skills

Then there's the talk on SQL knowledge and its relevance across different roles. This segment sheds light on how foundational SQL is, irrespective of your position. But it's not just about technical skills; the video also emphasizes soft skills, like leadership and collaboration, painting a holistic picture of what it takes to succeed in data engineering.

For those who love getting into the weeds, Andreas doesn't disappoint. They discuss software development skills, debugging, and even dive into how data engineers work with SQL and databases. This part is particularly insightful for understanding the technical depth required at various stages of your career.

### Q&A

And here's the cherry on top: Andreas encourages interaction, inviting viewers to share their experiences and questions. This makes the video not just a one-way learning experience but a dynamic conversation that enriches everyone involved.

### Summary

By the end of this video, you'll walk away with a clear understanding of the data engineering field's diverse roles. You'll know the skills needed to excel in each role and have a roadmap for your career progression. Whether you're a recent graduate looking to break into data engineering or a seasoned professional aiming for a senior position, Andreas's video is a must-watch. It's not just a lecture; it's a guide to navigating the exciting world of data engineering, tailored by someone who's taken the time to lay out the journey for you.



## How to Become a Senior Data Engineer

Becoming a senior data engineer is a goal many in the tech industry aspire to. It's a role that demands a deep understanding of data architecture, advanced programming skills, and the ability to lead and communicate effectively within an organization. In this live stream series, I dove into what it takes to climb the ladder to a senior data engineering position. Here are the key takeaways. You can find the links to the videos and the shown images below.

### Understanding the Role
The journey to becoming a senior data engineer starts with a clear understanding of what the role entails. Senior data engineers are responsible for designing, implementing, and maintaining an organization's data architecture. They ensure data accuracy, accessibility, and security, often taking the lead on complex projects that require advanced technical skills and strategic thinking.

### Key Skills and Knowledge Areas
Based on insights from the live stream and consultations with industry experts, including GPT-3, here are the critical areas where aspiring senior data engineers should focus their development:

- **Advanced Data Modeling and Architecture:** Mastery of data modeling techniques and architecture best practices is crucial. This includes understanding of dimensional and Data Vault modeling, as well as expertise in SQL and NoSQL databases.
- **Big Data Technologies:** Familiarity with distributed computing frameworks (like Apache Spark), streaming technologies (such as Apache Kafka), and cloud-based big data technologies is essential.
Advanced ETL Techniques: Skills in incremental loading, data merging, and transformation are vital for efficiently processing large datasets.
- **Data Warehousing and Data Lake Implementation:** Building and maintaining scalable and performant data warehouses and lakes are fundamental responsibilities.
- **Cloud Computing:** Proficiency in cloud services from AWS, Azure, or GCP, along with platforms like Snowflake and Databricks, is increasingly important.
- **Programming and Scripting:** Advanced coding skills in languages relevant to data engineering, such as Python, Scala, or Java, are non-negotiable.
- **Data Governance and Compliance:** Understanding data governance frameworks and compliance requirements is critical, especially in highly regulated industries.
- **Leadership and Communication:** Beyond technical skills, the ability to lead projects, communicate effectively with both technical and non-technical team members, and mentor junior engineers is what differentiates a senior engineer.

### Learning Pathways
Becoming a senior data engineer requires continuous learning and real-world experience. Here are a few steps to guide your journey:

- **Educational Foundation:** Start with a strong foundation in computer science or a related field. This can be through formal education or self-study courses.
- **Gain Practical Experience:** Apply your skills in real-world projects. This could be in a professional setting, contributions to open-source projects, or personal projects.
- **Specialize and Certify:** Consider specializing in areas particularly relevant to your interests or industry needs. Obtaining certifications in specific technologies or platforms can also bolster your credentials.
- **Develop Soft Skills:** Work on your communication, project management, and leadership skills. These are as critical as your technical abilities.
- **Seek Feedback and Mentorship:** Learn from the experiences of others. Seek out mentors who can provide guidance and feedback on your progress.

### Video 1

| Live Stream -> How to become a Senior Data Engineer - Part 1
|------------------|
| In this part one I talked about Data Modeling, Big Data, ETL, Data Warehousing & Data Lakes as well as Cloud computing
| [Watch on YouTube](https://youtube.com/live/M-6xkTCKQQc)|

![Watch on YouTube](/images/Becoming-a-Senior-Data-Engineer-Video-1.jpg)

### Video 2

| Live Stream -> How to become a Senior Data Engineer - Part 2
|------------------|
| In part two I talked about real time data processing, programming & scripting, data governance, compliance and data security
| [Watch on YouTube](https://youtube.com/live/po96pzpjxvA)|

![Watch on YouTube](/images/Becoming-a-Senior-Data-Engineer-Video-2.jpg)

### Video 3

| Live Stream -> How to become a Senior Data Engineer - Part 3
|------------------|
| In part 3 I focused on everything regarding Leadership and Communication: team management, project management, collaboration, problem solving, strategic thinking, communication and leadership
| [Watch on YouTube](https://youtube.com/live/DMumpzSyRjI)|

![Watch on YouTube](/images/Becoming-a-Senior-Data-Engineer-Video-3.jpg)

### Final Thoughts
The path to becoming a senior data engineer is both challenging and rewarding. It requires a blend of technical prowess, continuous learning, and the development of soft skills that enable you to lead and innovate. Whether you're just starting out or looking to advance your career, focusing on the key areas outlined above will set you on the right path.
