from amz_review_scraper import *
import nltk
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))

from nltk.stem import PorterStemmer
ps = PorterStemmer()

from nltk.sentiment import SentimentIntensityAnalyzer
sentimentIntensityAnalyser = SentimentIntensityAnalyzer()

import pandas as pd
import matplotlib.pyplot as plt

print("In Sentiment Analyser:-")
print("Preprocessing BoW (product_reviews)....")
print()

review_list = []
for review in product_reviews.values():
    review_list.append(review)

review_list1 = review_list[0]
review_list2 = review_list[1]

tokenized_review_list1 = []
filtered_review_list1 = []

for text in review_list1:
    ps.stem(text)
    a = sent_tokenize(text.lower())
    tokenized_review_list1.append(a)

for review in tokenized_review_list1:
    filtered_sentences = [' '.join([word for word in a.split() if word not in stop_words]) for a in review]
    filtered_review_list1.append(filtered_sentences)

#print(filtered_review_list1)

#print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

tokenized_review_list2 = []
filtered_review_list2 = []

for text in review_list2:
    ps.stem(text)
    a = sent_tokenize(text.lower())
    tokenized_review_list2.append(a)

for review in tokenized_review_list2:
    filtered_sentences = [' '.join([word for word in a.split() if word not in stop_words]) for a in review]
    filtered_review_list2.append(filtered_sentences)

#print(filtered_review_list2)

print("Analysing sentiments...")
def analyze_sentiments(list1, list2):
    def process_list(sentences):
        sent_count = 0
        score_list = []

        for sublist in sentences:
            for sentence in sublist:
                sentiment = sentimentIntensityAnalyser.polarity_scores(sentence)
                score_list.append(sentiment)
                sent_count += 1

        df = pd.DataFrame(score_list)
        return df

    df1 = process_list(list1)
    df2 = process_list(list2)

    return df1, df2
print("Review list 1 and list 2 scores:")
sentiment_scores_list1, sentiment_scores_list2 = analyze_sentiments(filtered_review_list1, filtered_review_list2)

print(sentiment_scores_list1)
print(sentiment_scores_list2)

def sentiment_grapher(df1, df2):

    def calc_overall_sentiment(compound_df):

        mean_compound = compound_df['compound'].mean()
        #print(mean_compound)

        if mean_compound > 0.05 :
            return "Overall sentiment: Positive"

        elif mean_compound < -0.05 :
            return "Overall sentiment: Negative"

        else:
            return "Overall sentiment: Neutral"

    overall_sentiment1 = calc_overall_sentiment(sentiment_scores_list1)
    overall_sentiment2 = calc_overall_sentiment(sentiment_scores_list2)

    print("Product-1: ",overall_sentiment1)
    print("Product-2: ",overall_sentiment2)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (12, 4))

    x = df1.index
    ax1.scatter(x, df1['pos'], color = 'g', label = 'Positive Scores')
    ax1.scatter(x, df1['neg'], color = 'r', label = 'Negative Scores')
    ax1.scatter(x, df1['neu'], color = 'b', label = 'Neutral Scores')
    ax1.scatter(x, df1['compound'], color = 'purple', label = 'Compound Scores')
    ax1.set_xlabel('Indices')
    ax1.set_ylabel('Scores')
    ax1.set_title('Sentiment Scores for product 1')
    #ax1.text(2, 11, overall_sentiment1, fontsize = 12, color = 'black')
    ax1.legend()

    y = df2.index
    ax2.scatter(y, df2['pos'], color = 'g', label = 'Positive Scores')
    ax2.scatter(y, df2['neg'], color = 'r', label = 'Negative Scores')
    ax2.scatter(y, df2['neu'], color = 'b', label = 'Neutral Scores')
    ax2.scatter(y, df2['compound'], color = 'purple', label = 'Compound Scores')
    ax2.set_xlabel('Indices')
    ax2.set_ylabel('Scores')
    ax2.set_title('Sentiment Scores for product 2')
    #ax2.text(4, 7, overall_sentiment2, fontsize = 12, color = 'black')
    ax2.legend()

    plt.show()

sentiment_grapher(sentiment_scores_list1, sentiment_scores_list2)

'''def analyze_sentiments(sentences):
    sent_count = 0
    score_list = []

    for sublist in sentences:
        for sentence in sublist:
            sentiment = sentimentIntensityAnalyser.polarity_scores(sentence)
            score_list.append(sentiment)
            sent_count+=1
            print("Sentence","[",sent_count,"]", sentiment)

    print()
    print("Score list:-")
    #print(score_list)
    df = pd.DataFrame(score_list)
    print(df)
    print("index only:-")
    indices = df.index
    indices_series = pd.Series(indices)
    #print(indices_series)

    pos_scores = df['pos']
    neu_scores = df['neu']
    neg_scores = df['neg']
    comp_score = df['compound']
    print()
    #print("positive scores only:-")
    #print(pos_scores)
    return 0

print("Review list 1 scores:-")
print("========================")
sentiment_scores_list1 = analyze_sentiments(filtered_review_list1)
print()
print("Review list 2 scores:-")
print("========================")
sentiment_scores_list2 = analyze_sentiments(filtered_review_list2)
print()
print()
'''
'''
sentiment_scores_list2 = analyze_sentiments(filtered_review_list2)
for i, sentiment in enumerate(sentiment_scores_list1):
    print(f"Sentence {i+1} sentiment scores: {sentiment}")
'''
'''
for review in filtered_review_list1:
    for i in range(len(filtered_review_list1)):
        print(sentimentIntensityAnalyser.polarity_scores(review))
'''
