from selenium import webdriver
from selenium.webdriver.common.by import By
# import selenium
import requests
from bs4 import BeautifulSoup
# book = input("Enter book you want to search")
import analysis


def fetch_reviews(book="twilight"):
    # book ="twilight"
    url = f"https://www.goodreads.com/search?q={book}"
    driver = webdriver.Chrome()
    driver.get(url)

    first_search_item= driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[2]/a[1]")
    book_link= first_search_item.get_attribute("href")
    driver.get(book_link)
    # more_reviews_link=driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/main/div[1]/div[2]/div[3]/div/div[5]/div[4]/a[1]")
    # driver.get(more_reviews_link.get_attribute("href"))
    response = requests.get(book_link)
    driver.quit()
    if response.status_code == 200:

            print("Fetching data....")
            soup = BeautifulSoup(response.text, 'html.parser')

            overall_rating = soup.find("div",class_="RatingStatistics__rating").get_text(strip=True)
            print(overall_rating)
            
            star_reviews = soup.find_all("div",class_="RatingsHistogram__labelTotal")
            for i , stars in enumerate(star_reviews[:5]): 
                print(f"{i + 1} stars: {stars.get_text(strip=True)}")
                print("-" * 30)
            # Extract review elements
            review_elements = soup.find_all("section", class_="ReviewText__content")
            print(type(review_elements))
            print(type(star_reviews))
            
            # vaders = analysis.analyze(review_elements)
            # analysis.plot(vaders,star_reviews)

            # Display the specified number of reviews
            # for i, review_element in enumerate(review_elements[:50]):

            #     print(f"Review {i + 1}: {review_element.get_text(strip=True)}")
            #     print("-" * 30)

    else:
        print(f"Failed to retrieve reviews. Status code: {response.status_code}")
        exit(1)
    return review_elements,star_reviews