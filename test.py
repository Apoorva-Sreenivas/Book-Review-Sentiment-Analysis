# # import SentimentIntensityAnalyzer class
# # from vaderSentiment.vaderSentiment module.
# from nltk.sentiment import SentimentIntensityAnalyzer

# # function to print sentiments
# # of the sentence.
# def sentiment_scores(sentence):

# 	# Create a SentimentIntensityAnalyzer object.
# 	sid_obj = SentimentIntensityAnalyzer()

# 	# polarity_scores method of SentimentIntensityAnalyzer
# 	# object gives a sentiment dictionary.
# 	# which contains pos, neg, neu, and compound scores.
# 	sentiment_dict = sid_obj.polarity_scores(sentence)
	
# 	print("Overall sentiment dictionary is : ", sentiment_dict)
# 	print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
# 	print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
# 	print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")

# 	print("Sentence Overall Rated As", end = " ")

# 	# decide sentiment as positive, negative and neutral
# 	if sentiment_dict['compound'] >= 0.05 :
# 		print("Positive")

# 	elif sentiment_dict['compound'] <= - 0.05 :
# 		print("Negative")

# 	else :
# 		print("Neutral")



# # Driver code
# if __name__ == "__main__" :

# 	print("\n1st statement :")
# 	sentence = "Geeks For Geeks is the best portal for \
# 				the computer science engineering students."

# 	# function calling
# 	sentiment_scores(sentence)

# 	print("\n2nd Statement :")
# 	sentence = "study is going on as usual"
# 	sentiment_scores(sentence)

# 	print("\n3rd Statement :")
# 	sentence = "I am very sad today."
# 	sentiment_scores(sentence)

# import matplotlib.pyplot as plt

# # Create a figure object.
# fig = plt.figure()

# # Add a subplot to the figure object.
# ax1 = fig.add_subplot(1, 2, 1)

# # Plot the first plot on the subplot.
# ax1.plot([1, 2, 3], [4, 5, 6])

# # Add another subplot to the figure object.
# ax2 = fig.add_subplot(1, 2, 2)

# # Plot the second plot on the subplot.
# ax2.plot([7, 8, 9], [10, 11, 12])

# # Show the figure object.
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Create a bar chart
plt.bar(np.arange(50), np.logspace(0, 6))

# Set the y-limit to 1e6
plt.ylim((0, 1e6))

# Set the scilimits parameter
plt.ticklabel_format(scilimits=(0, 6))

# Show the plot
plt.show()