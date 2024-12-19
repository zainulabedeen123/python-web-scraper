import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

def get_star_rating(class_name):
    """Convert star rating class to numeric value"""
    ratings = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    # Extract the rating from the class name (e.g., 'star-rating Three')
    rating_text = class_name.split()[-1]
    return ratings.get(rating_text, 0)

def scrape_books():
    # URL of the website
    url = 'https://books.toscrape.com/'
    
    try:
        # Send HTTP GET request
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all book articles
        books = soup.find_all('article', class_='product_pod')
        
        five_star_books = []
        
        for book in books:
            # Get star rating
            star_rating = book.find('p', class_='star-rating')
            rating = get_star_rating(star_rating['class'][1])
            
            # Only process 5-star books
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
        
        # Save results to a JSON file with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'five_star_books_{timestamp}.json'
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(five_star_books, f, indent=2, ensure_ascii=False)
            
        print(f'Found {len(five_star_books)} books with 5-star ratings')
        print(f'Results saved to {filename}')
        
        # Print the results in console
        for book in five_star_books:
            print('\n---')
            print(f"Title: {book['title']}")
            print(f"Price: {book['price']}")
            print(f"Availability: {book['availability']}")
            print(f"Image URL: {book['image_url']}")
            
    except requests.RequestException as e:
        print(f'Error fetching the webpage: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    scrape_books() 