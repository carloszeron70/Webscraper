import requests
from bs4 import BeautifulSoup

loop = 1
tempnum = 1

URL = ("https://books.toscrape.com/catalogue/page-1.html")


def scraper():
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="default")

    books = results.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

    for book in books:
        title_element = book.find("a", title=True)
        price_element = book.find("p", class_="price_color")
        link_url = book.find_all("a")[0]["href"]
        print(title_element["title"].strip())
        print(price_element.text.strip())

        if book.find("i", class_="icon-ok"):
            print("In Stock")
        else:
            print("Out of stock")

        if book.find("p", class_="star-rating One"):
            print("Rating:*")
        elif book.find("p", class_="star-rating Two"):
            print("Rating:**")
        elif book.find("p", class_="star-rating Three"):
            print("Rating:***")
        elif book.find("p", class_="star-rating Four"):
            print("Rating:****")
        elif book.find("p", class_="star-rating Five"):
            print("Rating:*****")

        print(f"View Book: https://books.toscrape.com/catalogue/{link_url}\n")

    print(f"Page {tempnum}")

scraper()

while loop==1:
    pagenumber = input("Back, Next, Cancel, or Page Number to Navigate:")

    if pagenumber.isnumeric():
        tempnum = int(pagenumber)

    elif pagenumber.lower() == "next":
        tempnum = int(tempnum) + 1

    elif pagenumber.lower() == "back":
        tempnum = int(tempnum) - 1

    elif pagenumber.lower() == "cancel":
        break

    if tempnum < 51:
        URL = (f"https://books.toscrape.com/catalogue/page-{tempnum}.html")
        scraper()









