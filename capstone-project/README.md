# Project

## Decision Process
*Q: Let's assume you have an active community site, similar to the Udacity forum, where users can post different information. You want to obtain some stats about user behaviour. Is is a good idea to use MapReduce/Hadoop to process the data?*

We need to consider the 3Vs of Big Data to decide:

- Volume: If we're using all of forum data and not a subset, and the dataset is sufficiently large, it is probably a good idea to use MapReduce/Hadoop to process it. What does sufficiently large mean? This [resource](https://www.chrisstucchio.com/blog/2013/hadoop_hatred.html) suggests anything over 10 GB presents a reasonable use case.
- Variety: Yes, two different formats of data - forum users and forum nodes. Performing table operations on a large amount of data is expensive.
- Velocity: This depends on how often users use the forum and if you're okay with using batch data. Given forum stats aren't life or death and probably doesn't vary much, batch data should be fine.

Given the volume and variety of our data, MapReduce/Hadoop is probably a good option.

## Exercises

### 1. Students and Posting Time on Forums

We have a lot of passionate students that bring a lot of value to forums. Forums also sometimes need a watchful eye on them, to make sure that posts are tagged in a way that helps to find them, that the tone on forums stays positive, and in general - they need people who can perform some management tasks - forum moderators. These are usually chosen from students who already have shown that they are active and helpful forum participants.

Our students come from all around the world, so we need to know both at what times of day the activity is the highest, and to know which of the students are active at that time.

In this exercise your task is to find for each student what is the hour during which the student has posted the most posts. Output from reducers should be:

`author_id    hour`

For example:

````
13431511\t13
54525254141\t21
````

If there is a tie: there are multiple hours during which a student has posted a maximum number of posts, please print the student-hour pairs on separate lines. The order in which these lines appear in your output does not matter.

You can ignore the time-zone offset for all times - for example in the following line: "2012-02-25 08:11:01.623548+00" - you can ignore the +00 offset.

In order to find the hour posted, please use the date_added field and NOT the last_activity_at field.

### 2. Post and Answer Length

We are interested to see if there is a correlation between the length of a post and the length of answers.

Write a mapreduce program that would process the forum_node data and output the length of the post and the average answer (just answer, not comment) length for each post. You will have to decide how to write both the mapper and the reducer to get the required result.

### 3. Top Tags

We are interested seeing what are the top tags used in posts.

Write a mapreduce program that would output Top 10 tags, ordered by the number of questions they appear in.

Please note that you should only look at tags appearing in questions themselves (i.e. nodes with node_type "question"), not on answers or comments.

## Search Functionality

*In Lesson 4 you built an index which included {\<word\>: \<forum entries that include the word\>}. This index can be used to search efficiently for forum posts that contain a specific word. Can you think of improvements you could make to the process of building an index by using the design patterns you learned in Lesson 4?*

We learned about filtering, summarization, and structural patterns.

Improvements might include:

- Improving the efficiency of the index by filtering out the shorter, less meaningful words (like **the**, **and**, and **but**)
- Changing the index to include only the absolute parent ID (i.e. the ID of the thread's first entry) rather than the individual entry IDs. We don't have to store as much data that way and can still easily access the thread containing the word.