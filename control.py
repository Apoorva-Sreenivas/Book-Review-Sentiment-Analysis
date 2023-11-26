import get_reviews
import analysis

class Control:

    def call(self,book_name):
        reviews,stars,overall_rating,book_name_1,book_name_2,author_name =get_reviews.fetch_reviews(book_name)
        vaders = analysis.analyze(reviews)
        analysis.plot(stars,vaders)
        return overall_rating,book_name_1,book_name_2,author_name

    