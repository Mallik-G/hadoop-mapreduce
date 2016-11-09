# Project

## Decision Process
*Q: Let's assume you have an active community site, similar to the Udacity forum, where users can post different information. You want to obtain some stats about user behaviour. Is is a good idea to use MapReduce/Hadoop to process the data?*

We need to consider the 3Vs of Big Data to decide:

- Volume: If we're using all of forum data and not a subset, and the dataset is sufficiently large, it is probably a good idea to use MapReduce/Hadoop to process it. What does sufficiently large mean? This [resource](https://www.chrisstucchio.com/blog/2013/hadoop_hatred.html) suggests anything over 10 GB presents a reasonable use case.
- Variety: Yes, two different formats of data - forum users and forum nodes. Performing table operations on a large amount of data is expensive.
- Velocity: This depends on how often users use the forum and if you're okay with using batch data. Given forum stats aren't life or death and probably doesn't vary much, batch data should be fine.

Given the volume and variety of our data, MapReduce/Hadoop is probably a good option.

## Exercises

See code folder for mappers and reducers.

## Search Functionality
*In Lesson 4 you built an index which included {\<word\>: \<forum entries that include the word\>}. This index can be used to search efficiently for forum posts that contain a specific word. Can you think of improvements you could make to the process of building an index by using the design patterns you learned in Lesson 4?*

We learned about filtering, summarization, and structural patterns.

Improvements might include:

- Improving the efficiency of the index by filtering out the shorter, less meaningful words (like **the**, **and**, and **but**)
- Changing the index to include only the absolute parent ID (i.e. the ID of the thread's first entry) rather than the individual entry IDs. We don't have to store as much data that way and can still easily access the thread containing the word.