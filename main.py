import numpy as np
import pandas as pd
import matplotlib
from sklearn import preprocessing
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split, KFold
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from matplotlib import pyplot as plt


data = pd.read_csv("../input/train.csv")
