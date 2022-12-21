import os
import sys
import jsonlines
from afinn import Afinn
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import pandas as pd

sid_obj = SentimentIntensityAnalyzer()
afn = Afinn()

def vader(sentence):
    """Vader sentiment"""
    sentiment_dict = sid_obj.polarity_scores(sentence)
    return sentiment_dict


# def tblob(sentence):
#     """textblob sentiment"""
#     sentiment_dict = sid_obj.polarity_scores(sentence)
#     return sentiment_dict



def afinn(text):
    """Afinn sentiment"""
    score = afn.score(text)
    return score


files = [eval(arg) for arg in sys.argv[1:]]

folder = r'D:\FullCSV\New_dataset\Hydrated_output'
output_folder = r'D:\FullCSV\New_dataset\Hydrated_output\outputs'


for file in files:
    output_file =  os.path.join(output_folder, file.split('.')[0] + '_output.jsonl') 
    file = os.path.join(folder, file)    



    with jsonlines.open(output_file, mode='w') as writer: # output jsonl file MUST be created first
        with jsonlines.open(file) as f:
            for line in f.iter():
               if not "retweeted_status" in line:
                    
                    txt = line['full_text']
                    
                
                    vader_sentiment = vader(txt)
                    blob = TextBlob(txt)
                    
                    line['date'] = pd.to_datetime(line['created_at']).strftime('%Y-%m-%d')
                    line['polarity'] = blob.sentiment.polarity
                    line['subjectivity'] = blob.sentiment.subjectivity
                    line['vader_pos'] = vader_sentiment['pos']
                    line['vader_neg'] = vader_sentiment['neg']
                    line['vader_neu'] = vader_sentiment['neu']
                    line['vader_comp'] = vader_sentiment['compound']
                    line['afinn'] = afinn(txt)

                    writer.write(line)
