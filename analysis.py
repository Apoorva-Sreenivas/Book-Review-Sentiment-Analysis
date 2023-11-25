import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
# from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np
import re

sia = SentimentIntensityAnalyzer()

# nltk.download('punkt')
# nltk.download('vader_lexicon')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')

def analyze(cleaned_text):
    print(len(cleaned_text))
    res={}
    i=0
    for data in cleaned_text:
        res[i]= sia.polarity_scores(data)
        i+=1
    # print(res)
    vaders = pd.DataFrame(res).T
    # vaders = vaders.reset_index().rename(columns={'index': 'Id'})
    print(tabulate(vaders, headers = 'keys', tablefmt = 'psql'))
    # compound = vaders["compound"]
    
    return vaders

def plot(stars,vaders):
    x=[]
    y=[1,2,3,4,5]
    for i,stars in enumerate(stars[:5]):
        text = stars.get_text(strip=True)
        t_list = text.split()
        print(t_list)
        x.append(int(t_list[0].replace(",","")))
    print(x)
    x.reverse()
    plt.subplot(2,1,1)
    plt.bar(y,x,color="skyblue")
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.xlabel("Stars")
    plt.ylabel("Number of reviews")
    compound_negetive = vaders.loc[vaders["compound"]<=-0.05]
    compound_positive = vaders.loc[vaders["compound"]>=0.05]
    print(len(compound_negetive))
    print(len(compound_positive))
    print(len(vaders)-len(compound_negetive)-len(compound_positive))
    total_reviews = len(vaders)
    total_neg_reviews = (len(compound_negetive)/total_reviews)*100
    total_pos_reviews = (len(compound_positive)/total_reviews)*100
    total_neu_reviews = 100-(total_pos_reviews+total_neg_reviews)
    y = np.array([total_pos_reviews,total_neu_reviews,total_neg_reviews])
    mylabels = ["Positive Reviews","Neutral Reviews","Negetive Reviews"]  
    mycolors = ['green', 'lightgrey', 'red']  
    myexplode=[0.1,0,0]
    plt.subplot(2,1,2)
    plt.pie(y, labels = mylabels, explode = myexplode,colors=mycolors,shadow=True)
    plt.title("Sentiment Analysis on Reviews")
    plt.subplots_adjust(left=0.2,hspace=0.6)
    plt.show()
    
def clean_text(review_elements):
    dataset=[]
    for i, review_element in enumerate(review_elements):
        review = review_element.get_text(strip=True)
        dataset.append(review)
    
    clean_text_1=[]
    for data in dataset:
        clean_text_1.append(str.lower(data))
    
    # print(clean_text_1)
    # print("----------------------------------------")
    
    clean_text_2=[word_tokenize(i) for i in clean_text_1]


    # print(clean_text_2)
    # print("----------------------------------------")

    clean_text_3=[]
    for words in clean_text_2:
        clean=[]
        for w in words:
            res = re.sub(r'[^\w\s]',"",w)
            if res !="":
                clean.append(res)
        clean_text_3.append(clean)
    # print(clean_text_3)
    # print("----------------------------------------")

    clean_text_4=[]
    for words in clean_text_3:
        w=[]
        for word in words:
            if not word in stopwords.words('english'):
                w.append(word)
        clean_text_4.append(w)
    
    # print(clean_text_4)
    # print("----------------------------------------")

    pos_tag_1=[]
    for words in clean_text_4:
        pos_tag_1.append(pos_tag(words))
    # print(pos_tag_1)
    # print("----------------------------------------")

    wnet = WordNetLemmatizer()
    clean_text_5=[]
    for words in pos_tag_1:
        w=[]
        for word,tag in words:
            wntag = tag.lower()
            wntag= wntag[0]
            wntag = wntag if wntag in ['a','r','n','v'] else None
            if not wntag:
                w.append(word)
            else:
                w.append(wnet.lemmatize(word,wntag))
        clean_text_5.append(w)

    # print(clean_text_5)
    # print("----------------------------------------")

    cleaned_text =[]
    for words in clean_text_5:
        my_string = " ".join(words)
        cleaned_text.append(my_string)
        my_string=""
    # print(cleaned_text)
    return cleaned_text