from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()


text="""Can 35 Million Book Buyers Be Wrong? Yes.

Taking arms against Harry Potter, at this moment, is to emulate Hamlet taking arms against a sea of troubles. By opposing the sea, you won't end it. The Harry Potter epiphenomenon will go on, doubtless for some time, as J. R. R. Tolkien did, and then wane.

The official newspaper of our dominant counter-culture, The New York Times, has been startled by the Potter books into establishing a new policy for its not very literate book review. Rather than crowd out the Grishams, Clancys, Crichtons, Kings, and other vastly popular prose fictions on its fiction bestseller list, the Potter volumes will now lead a separate children's list. J. K. Rowling, the chronicler of Harry Potter, thus has an unusual distinction: She has changed the policy of the policy-maker.

Imaginative Vision

I read new children's literature, when I can find some of any value, but had not tried Rowling until now. I have just concluded the 300 pages of the first book in the series, "Harry Potter and the Sorcerer's Stone," purportedly the best of the lot. Though the book is not well written, that is not in itself a crucial liability. It is much better to see the movie, "The Wizard of Oz," than to read the book upon which it was based, but even the book possessed an authentic imaginative vision. "Harry Potter and the Sorcerer's Stone" does not, so that one needs to look elsewhere for the book's (and its sequels') remarkable success. Such speculation should follow an account of how and why Harry Potter asks to be read.

The ultimate model for Harry Potter is "Tom Brown's School Days" by Thomas Hughes, published in 1857. The book depicts the Rugby School presided over by the formidable Thomas Arnold, remembered now primarily as the father of Matthew Arnold, the Victorian critic-poet. But Hughes' book, still quite readable, was realism, not fantasy. Rowling has taken "Tom Brown's School Days" and re-seen it in the magical mirror of Tolkein. The resultant blend of a schoolboy ethos with a liberation from the constraints of reality-testing may read oddly to me, but is exactly what millions of children and their parents desire and welcome at this time.

In what follows, I may at times indicate some of the inadequacies of "Harry Potter." But I will keep in mind that a host are reading it who simply will not read superior fare, such as Kenneth Grahame's "The Wind in the Willows" or the "Alice" books of Lewis Carroll. Is it better that they read Rowling than not read at all? Will they advance from Rowling to more difficult pleasures?

Rowling presents two Englands, mundane and magical, divided not by social classes, but by the distinction between the "perfectly normal" (mean and selfish) and the adherents of sorcery. The sorcerers indeed seem as middle-class as the Muggles, the name the witches and wizards give to the common sort, since those addicted to magic send their sons and daughters off to Hogwarts, a Rugby school where only witchcraft and wizardry are taught. Hogwarts is presided over by Albus Dumbeldore as Headmaster, he being Rowling's version of Tolkein's Gandalf. The young future sorcerers are just like any other budding Britons, only more so, sports and food being primary preoccupations. (Sex barely enters into Rowling's cosmos, at least in the first volume.)
"""
res = sia.polarity_scores(text)
print(res)