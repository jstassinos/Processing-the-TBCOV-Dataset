# Processing-the-TBCOV-Dataset


Introduction:


Steps:



Starting point is the Tab Seperated Values (TSV) file from the original geolocated tweet data set provided by Quazi et al Need Cite ****

Additionally users will need to have a twitter account and sign up for a developer access in order to use the twiiter api for tweet hydration


The TSV comes with tweetid numbers and some associated metadata but no tweet text as this would violate Twiiter's terms of service. Before tweet hydration begins we will remove anything with a RetweetID because for this research we are only interested in original tweets. 

The remove retweets PYTHON ****** file will return a text file with a new tweetid on each row. This tweet id file will then be fed into the Hydrator app ****** github hyper link here ******* and the hydrator app will return the raw tweet data as a json Lines (.jsonl) file. 

Sentiment calculaton ******* python senti file ****** calculates the sentiment using Textblob Vader Sentimetn and AFINN and appends the values to the end of each json line. 

In order to import this data to a SQL server ( I used Postgresql) the jsonlines format will need to be converted to a CSV using **** PYTON TO CSV ****


The original tsv of the tweet ids and there are multiple sources for the user locion but for our purposes we want to use the most accurate version. So for tweet swith g
