# -*- coding: utf-8 -*-
"""Untitled130.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zDwBzDJKisWbd2lN_TQxurIogfStIkRO
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd
import numpy as np

df = pd.read_csv('/content/drive/MyDrive/train (1).csv')
print(df.head())
print(df.shape)
print(df.isnull().sum())
print(df.duplicated().sum())

df.drop(columns=['keyword','location'],inplace=True)

df.head()

df['text'][6]

df['text']=df['text'].apply(lambda x:x.lower())

df['text'].str.lower()

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('wordnet')

def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = text.split()
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    cleaned_text = ' '.join(words)
    return cleaned_text
clean_text(df['text'][6])

df['text'] = df['text'].apply(clean_text)

df['text'].head()

from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(ngram_range=(1,3))

bow=cv.fit_transform(df['text'])

print(cv.vocabulary_)

tfidf = TfidfVectorizer(max_features=5000)
x = tfidf.fit_transform(df['text'])
y = df['target']

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

lr = LogisticRegression()
lr.fit(x_train,y_train)

print(lr.score(x_train,y_train))
print(lr.score(x_test,y_test))
