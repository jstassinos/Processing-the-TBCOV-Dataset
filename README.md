# Processing-the-TBCOV-Dataset

### Table of Contents:


### About the Project:

The goal of this project was to leverage the geolocated tweet dataset TBCOV into information about the relationship between COVID-19 tweet sentiment and the prevalence of the COVID-19 virus in a community.   

### Dataset:
The original TSV file with the TBCOV data for the United States of America can be found [HERE](https://crisisnlp.qcri.org/tbcov). See the Country Release download section. 

### Getting Started:

See [requirements.txt](/requirements.txt) for the libararies used in this repository. 

Starting point is a Tab Separated Values (TSV) file from the original geolocated tweet data set provided by (Imran et al., 2022). This file contains TweetID numbers, and the geolocation information created as part of Imran et al’s research. 

Additionally, users will need to have a twitter account and sign up for a developer access to use the twitter API for tweet hydration.
The original TSV does not come with tweet contents like text or links as this would violate Twitter’s terms of service. To get tweet contents we will use the TweetID numbers to request the contents from the Twitter API using the Hydrator app. 

The [Hydrator](https://github.com/DocNow/hydrator) app only takes a text file with each requested TweetID on a new line. To make this TweetID text file we will use [tweetidextractorforhydration.py](/tweetidextractorforhydration.py)  . This python script removes all retweets by checking for the existence of a RetweetID because for this research we are only interested in original tweets.

Sentiment calculaton [runner.py](/runner.py) calculates the sentiment using Textblob Vader Sentimetn and AFINN and appends the values to the end of each json line. 
In order to import this data to a SQL server ( I used Postgresql) the jsonlines format will need to be converted to a CSV using [jsonlinesconversion_original.py](/jsonlinesconversion_original.py).

The original tsv of the tweet ids has multiple sources for locations, and [tweetidandgeolocextractor.py](/tweetidandgeolocextractor.py) take the most accurate one and sets it as the location for that tweet and returns it in a table format with the tweetID as the key for joining to the sentiment table. 

The two datasets one containing sentiment information and the other containing geolocation information were both uploaded into a PostGreSQL server and SQL queries 


