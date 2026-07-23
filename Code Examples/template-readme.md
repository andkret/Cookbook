# Title Of Your Project

Add a catchy title. Something where people immediately know what you are doing.

*The bullet prompts under each heading are instructions for you. Delete them as you fill the section in.*

# Introduction & Goals

Write this like an executive summary. It is the only part most people will read, so it has to stand on its own.

- What data are you working with
- What tools are you using
- What are you doing with these tools
- Once you are finished, come back and add the conclusion here as well

Then list your goals. Two or three is plenty. Each goal gets a line saying how you know it worked, and that line needs a number in it. "The pipeline should be fast" is not something anyone can check. "Data is queryable within 10 minutes of the API call" is.

**Goal 1:** [what the project has to achieve, in plain language]
**How I know it worked:** [the measurable version]

**Goal 2:** [...]
**How I know it worked:** [...]

> **Why this matters:** almost every portfolio project skips straight to the tools. Naming what the project had to achieve, before you name a single tool, is the thing that makes the rest of this document read like a professional wrote it.

## Architecture

![Architecture](images/architecture.png)

Draw this yourself, export it as a PNG and commit it into `/images`. Do not link to a Miro board that needs an account. If someone only looks at one thing in this repo, it will be this picture.

# Contents

- [The Data Set](#the-data-set)
- [Constraints](#constraints)
- [Used Tools](#used-tools)
  - [Connect](#connect)
  - [Buffer](#buffer)
  - [Processing](#processing)
  - [Storage](#storage)
  - [Visualization](#visualization)
- [Pipelines](#pipelines)
  - [Stream Processing](#stream-processing)
    - [Storing Data Stream](#storing-data-stream)
    - [Processing Data Stream](#processing-data-stream)
  - [Batch Processing](#batch-processing)
  - [Visualizations](#visualizations)
- [Demo](#demo)
- [What Breaks](#what-breaks)
- [Conclusion](#conclusion)
- [Follow Me On](#follow-me-on)
- [Appendix](#appendix)

# The Data Set

- Explain the data set
- Why did you choose it?
- What do you like about it?
- What is problematic?
- What do you want to do with it?

## How much data is it

Show the arithmetic, do not just say it is a lot. Walk the chain from the source to the total:

> 2,100 stations, polled every 5 minutes, is 288 polls a day per station, so 604,800 records a day. Each record is around 400 bytes of JSON, which is about 240 MB a day raw and 12 MB a day once it is in Parquet. Over 6 months that is 2.2 GB.

Do this and every tool choice further down has a number to point at. Skip it and your choices look arbitrary, because they are. It also means that when someone asks you in an interview what happens at 100x, you already have the number to multiply.

# Constraints

What you had to work with. Be straight about it, this is not an apology.

- Budget: [what you were willing to spend per month]
- Compute: [laptop, one small VM, free tier]
- Data you do not control: [rate limits, no history available, schema can change without warning]
- Time: [what you gave this]

"No budget, so everything runs on free tiers and my laptop" explains half your architecture in one line, and saying it plainly reads as confidence.

# Used Tools

- Explain which tools you use and why
- How do they work (don't go too deep into details, but add links)
- Why did you choose them
- How did you set them up

For each layer, also say what you considered and rejected. A choice with a rejected alternative next to it is worth ten times a choice on its own, and it is what an interviewer will actually ask about.

> **Storage: Postgres on the same box.** Considered DuckDB and the Snowflake free tier. The whole dataset is 2 GB, but the dashboard reads while the loader writes and DuckDB does not love that. Snowflake would work fine and would also be me picking a warehouse to have a warehouse on my CV.

Not every project has all five layers. If you have no buffer, say so and say why you did not need one. An empty section with an honest sentence in it is better than pretending.

## Connect
*Everything for data ingestion — pulling data or receiving it, and the tools and processing that make that happen.*

## Buffer
*Everything to do with message queues (e.g. Kafka, Kinesis, Pub/Sub) that sit between ingestion and processing.*

## Processing
*Everything with processing — Python scripts, Spark, dockerized apps, orchestration and observability.*

## Storage
*Where the data lands — OLAP and OLTP databases, data lakes and lakehouses.*

## Visualization
*How people and systems consume the data — apps, dashboards, BI tools and, of course, APIs for clients.*

# Pipelines

- Explain the pipelines you built
- Go through your development and link to the source code in `/sources`

Link to the files, do not paste the whole pipeline in here. The code already lives in the repo and a README that turns into a code dump stops being readable. Short snippets to show one interesting bit are good.

Say what the pipeline does when something goes wrong. Retries, what happens to a bad record, whether the job fails loudly or writes garbage quietly. This is the part people forget and it is exactly the part that separates a project from a tutorial.

## Stream Processing
## Batch Processing
## Visualizations

# Demo

- Add a demo video here
- Or link to your presentation video of the project

A two minute screen recording of the thing actually running does more than three paragraphs. A repo with no visible output is hard to tell apart from a repo that never worked.

# What Breaks

Three or four honest points. What you chose not to solve, what falls over if the data grows, and what you would change if you built it again.

You already have your volume numbers, so multiply them and say what breaks first. You do not have to fix it. Knowing where the ceiling is beats pretending there isn't one.

- **[What breaks first]** [At what point, and what you would do about it]
- **[What you deliberately skipped]** [Why it was not worth it at this size]
- **[Risk you accepted]** [What happens if it hits, and why you decided to live with it]

Deciding which risks to ignore is the part that only someone who has shipped something can do. Anyone can list risks.

If your data touches people, add one honest paragraph on it. One paragraph, not a compliance chapter. If there is nothing personal in the data, one line saying you checked is also a fine answer.

# Conclusion

Write a comprehensive conclusion.

- How did this project turn out
- What major things have you learned
- What were the biggest challenges

Then go back up to the introduction and paste the short version of this into the executive summary.

Make the lessons specific. "I would add more tests" says nothing because everyone writes it. "I partitioned by ingest date and should have partitioned by event date, because every query I actually write filters on event date and now they all scan everything" says you went back and looked at your own work.

# Follow Me On

Add the link to your LinkedIn profile.

# Appendix

This template comes from Andreas Kretz's Data Engineering Cookbook. If it helped you, point people back to it: [The Data Engineering Cookbook](https://github.com/andkret/Cookbook)