import get_reviews
import analysis

# book = input("Enter the name of the book : ")
reviews,stars =get_reviews.fetch_reviews()
# cleaned_data = analysis.clean_text(reviews)
vaders = analysis.analyze(reviews)
analysis.plot(stars,vaders)
# analysis.plot2(vaders)

    