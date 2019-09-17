Introduction
============

How To Use This Cookbook
------------------------

What do you actually need to learn to become an awesome data engineer?
Look no further, you'll find it here.

If you are looking for AI algorithms and such data scientist things,
this book is not for you.

**How to use this document:**\
First of all, this is not a training! This cookbook is a collection of
skills that I value highly in my daily work as a data engineer. It's
intended to be a starting point for you to find the topics to look into
and become an awesome data engineer.

You are going to find ***Five Types of Content*** in this book: Articles
I wrote, links to my podcast episodes (video & audio), more than 200
links to helpful websites I like, data engineering interview questions
and case studies.

**This book is a work in progress!**\
As you can see, this book is not finished. I'm constantly adding new
stuff and doing videos for the topics. But obviously, because I do this
as a hobby my time is limited. You can help making this book even
better.

**Help make this book awesome!**\
If you have some cool links or topics for the cookbook, please become a
contributor on GitHub: <https://github.com/andkret/Cookbook>. Pull the
repo, add them and create a pull request. Or join the discussion by
opening Issues. You can also write me an email any time to
plumbersofdatascience\@gmail.com. Tell me your thoughts, what you value,
what you think should be included, or correct me where I am wrong.

**This Cookbook is and will always be free!**\
I don't want to sell you this book, but please support what you like and
join my Patreon: <https://www.patreon.com/plumbersofds>

Check out this podcast episode where I talk in detail why I decided to
share all this information for free: [\#079 Trying to stay true to
myself and making the cookbook public on
GitHub](https://youtu.be/k1bS5aSPos8)

Data Engineer vs Data Scientist
-------------------------------

  -- -----------------------------------------------------------------------------------------------------------------------------------

     [Click here to watch](https://youtu.be/64TYZETOEdQ)
     [Click here to listen](https://anchor.fm/andreaskayy/episodes/050-Data-Engineer-Scientist-or-Analyst-Which-One-Is-For-You-e45ibl)
  -- -----------------------------------------------------------------------------------------------------------------------------------

### Data Scientist

Data scientists aren't like every other scientist.

Data scientists do not wear white coats or work in high tech labs full
of science fiction movie equipment. They work in offices just like you
and me.

What differs them from most of us is that they are math experts. They
use linear algebra and multivariable calculus to create new insight from
existing data.

How exactly does this insight look?

Here's an example:

An industrial company produces a lot of products that need to be tested
before shipping.

Usually such tests take a lot of time because there are hundreds of
things to be tested. All to make sure that your product is not broken.

Wouldn't it be great to know early if a test fails ten steps down the
line? If you knew that you could skip the other tests and just trash the
product or repair it.

That's exactly where a data scientist can help you, big-time. This field
is called predictive analytics and the technique of choice is machine
learning.

Machine what? Learning?

Yes, machine learning, it works like this:

You feed an algorithm with measurement data. It generates a model and
optimises it based on the data you fed it with. That model basically
represents a pattern of how your data is looking. You show that model
new data and the model will tell you if the data still represents the
data you have trained it with. This technique can also be used for
predicting machine failure in advance with machine learning. Of course
the whole process is not that simple.

The actual process of training and applying a model is not that hard. A
lot of work for the data scientist is to figure out how to pre-process
the data that gets fed to the algorithms.

In order to train a algorithm you need useful data. If you use any data
for the training the produced model will be very unreliable.

A unreliable model for predicting machine failure would tell you that
your machine is damaged even if it is not. Or even worse: It would tell
you the machine is ok even when there is an malfunction.

Model outputs are very abstract. You also need to post-process the model
outputs to receive health values from 0 to 100.

![The Machine Learning
Pipeline[]{label="fig:Bild1"}](images/Machine-Learning-Pipeline.png){#fig:Bild1
width="90%"}

### Data Engineer

Data Engineers are the link between the management's big data strategy
and the data scientists that need to work with data.

What they do is building the platforms that enable data scientists to do
their magic.

These platforms are usually used in five different ways:

-   Data ingestion and storage of large amounts of data

-   Algorithm creation by data scientists

-   Automation of the data scientist's machine learning models and
    algorithms for production use

-   Data visualisation for employees and customers

-   Most of the time these guys start as traditional solution architects
    for systems that involve SQL databases, web servers, SAP
    installations and other "standard" systems.

But to create big data platforms the engineer needs to be an expert in
specifying, setting up and maintaining big data technologies like:
Hadoop, Spark, HBase, Cassandra, MongoDB, Kafka, Redis and more.

What they also need is experience on how to deploy systems on cloud
infrastructure like at Amazon or Google or on-premise hardware.

  -- ------------------------------------------------------------------------------------------------------------------------------

     [Click here to watch](https://youtu.be/pIZkTuN5AMM)
     [Click here to listen](https://anchor.fm/andreaskayy/episodes/048-From-Wannabe-Data-Scientist-To-Engineer-My-Journey-e45i2o)
  -- ------------------------------------------------------------------------------------------------------------------------------

### Who Companies Need

For a good company it is absolutely important to get well trained data
engineers and data scientists. Think of the data scientist as the
professional race car driver. A fit athlete with talent and driving
skills like you have never seen.

What he needs to win races is someone who will provide him the perfect
race car to drive. That's what the solution architect is for.

Like the driver and his team the data scientist and the data engineer
need to work closely together. They need to know the different big data
tools inside and out.

That's why companies are looking for people with Spark experience. It is
a common ground between both that drives innovation.

Spark gives data scientists the tools to do analytics and helps
engineers to bring the data scientist's algorithms into production.
After all, those two decide how good the data platform is, how good the
analytics insight is and how fast the whole system gets into a
production ready state.
