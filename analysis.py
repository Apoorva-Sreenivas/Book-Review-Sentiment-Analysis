import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

sia = SentimentIntensityAnalyzer()

# nltk.download('punkt')
# nltk.download('vader_lexicon')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')

def analyze(review_elements):
    dataset=[]
    for i, review_element in enumerate(review_elements):
        review = review_element.get_text(strip=True)
        dataset.append(review)
    res={}
    i=0
    for data in dataset:
        res[i]= sia.polarity_scores(data)
        i+=1
    vaders = pd.DataFrame(res).T
    
    return vaders

def plot(stars,vaders):
    x=[]
    y=[1,2,3,4,5]
    for i,stars in enumerate(stars[:5]):
        text = stars.get_text(strip=True)
        t_list = text.split()
        x.append(int(t_list[0].replace(",","")))

    x.reverse()
    plt.subplot(2,1,1)
    plt.bar(y,x,color="skyblue")
    plt.title("Star Rating Statistics")
    plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
    plt.xlabel("Stars")
    plt.ylabel("Number of reviews")

    compound_negetive = vaders.loc[vaders["compound"]<=-0.05]
    compound_positive = vaders.loc[vaders["compound"]>=0.05]
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
    plt.show(block=False)
    