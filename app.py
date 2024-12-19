from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_star_rating(class_name):
    """Convert star rating class to numeric value"""
    ratings = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    rating_text = class_name.split()[-1]
    return ratings.get(rating_text, 0)

def scrape_books():
    url = 'https://books.toscrape.com/'
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('article', class_='product_pod')
        
        five_star_books = []
        
        for book in books:
            star_rating = book.find('p', class_='star-rating')
            rating = get_star_rating(star_rating['class'][1])
            
            if rating == 5:
                title = book.h3.a['title']
                price = book.find('p', class_='price_color').text
                availability = book.find('p', class_='availability').text.strip()
                image_url = url + book.find('img')['src']
                
                book_data = {
                    'title': title,
                    'price': price,
                    'availability': availability,
                    'image_url': image_url,
                    'rating': '5 stars'
                }
                
                five_star_books.append(book_data)
                
        return five_star_books
    except Exception as e:
        print(f'An error occurred: {e}')
        return []

@app.route('/')
def index():
    books = scrape_books()
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run(debug=True) 