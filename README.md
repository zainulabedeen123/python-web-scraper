# Books To Scrape - 5 Star Books Scraper

A Python web scraper that extracts 5-star rated books from [Books to Scrape](https://books.toscrape.com/) and displays them in a beautiful web interface using Flask and TailwindCSS.

## 📚 Features

- Scrapes books with 5-star ratings from books.toscrape.com
- Extracts book details including:
  - Title
  - Price
  - Availability
  - Book cover image
  - Rating
- Modern web interface built with Flask and TailwindCSS
- Responsive design that works on mobile, tablet, and desktop
- Real-time data refresh capability

## 🚀 Installation

1. Clone the repository:
```bash
git https://github.com/zainulabedeen123/python-web-scraper.git
cd webscrapperpython
```

2. Create a virtual environment (recommended):
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 💻 Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Click the "Refresh Books" button to fetch the latest data.

## 🛠️ Project Structure

```
webscrapperpython/
├── app.py              # Flask application and scraping logic
├── requirements.txt    # Project dependencies
├── README.md          # Project documentation
└── templates/
    └── index.html     # Web interface template
```

## 📝 Dependencies

- Python 3.7+
- Flask
- BeautifulSoup4
- Requests
- TailwindCSS (CDN)

## 🌐 Web Proxy Service

For reliable web scraping, especially when dealing with rate limits or IP blocks, consider using a premium web proxy service. We recommend:

[Toolip.io Premium Proxies](https://toolip.io/?ref=themetaverseguy)

Features of Toolip.io:
- High-performance proxy servers
- Multiple locations
- Reliable uptime
- Perfect for web scraping projects

## ⚠️ Disclaimer

This scraper is for educational purposes only. Always check and respect the website's robots.txt file and terms of service before scraping. Consider implementing delays between requests to avoid overwhelming the server.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details. 