from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

def fetch_reviews(book):
    url = f"https://www.goodreads.com/search?q={book}"
    driver = webdriver.Chrome()
    driver.get(url)

    first_search_item= driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[1]/td[2]/a[1]")
    book_link= first_search_item.get_attribute("href")
    driver.get(book_link)

    response = requests.get(book_link)

    if response.status_code == 200:

            soup = BeautifulSoup(response.text, 'html.parser')

            overall_rating = soup.find("div",class_="RatingStatistics__rating").get_text(strip=True)

            book_name_1 = soup.find("h3",class_="Text Text__title3 Text__italic Text__regular Text__subdued").get_text(strip=True)

            book_name_2 = soup.find("h1",class_="Text Text__title1").get_text(strip=True)
            
            author_name = soup.find("h3",class_="Text Text__title3 Text__regular").get_text(strip=True)

            star_reviews = soup.find_all("div",class_="RatingsHistogram__labelTotal")
                
            # Extract review elements
            review_elements = soup.find_all("section", class_="ReviewText__content")

    else:
        print(f"Failed to retrieve reviews. Status code: {response.status_code}")
        exit(1)
    return review_elements,star_reviews,overall_rating,book_name_1,book_name_2,author_name