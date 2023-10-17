from amz_review_scraper import *
import nltk
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
from nltk.stem import PorterStemmer
ps = PorterStemmer()
from nltk.sentiment import SentimentIntensityAnalyzer
sentimentIntensityAnalyser = SentimentIntensityAnalyzer()

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

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

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
def analyze_sentiments(sentences):
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
    print(score_list)
#it's better to use pandas for this. {message: USE PANDAS FOR PLOTTING, NOT LISTS}

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
sentiment_scores_list2 = analyze_sentiments(filtered_review_list2)
for i, sentiment in enumerate(sentiment_scores_list1):
    print(f"Sentence {i+1} sentiment scores: {sentiment}")
'''
'''
for review in filtered_review_list1:
    for i in range(len(filtered_review_list1)):
        print(sentimentIntensityAnalyser.polarity_scores(review))
'''
