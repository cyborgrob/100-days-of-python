import requests
from email.message import EmailMessage
import smtplib

# Set your stock ticket
STOCK = "TSLA"

# Get stock prices from alphavantage API
alpha_api_key = 'YOUR_API_KEY'
alpha_url = 'https://www.alphavantage.co/query'
alpha_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': alpha_api_key,
}

# Gets stock price data from website
alpha_resp = requests.get(url=alpha_url, params=alpha_params)
alpha_resp.raise_for_status()
alpha_data = alpha_resp.json()
# Converts response JSON into list so we can parse out last two closing prices
price_list = [value for (key, value) in alpha_data['Time Series (Daily)'].items()]
yesterday_price = float(price_list[0]['4. close'])
day_before_yesterday_price = float(price_list[1]['4. close'])
percent_change = (yesterday_price - day_before_yesterday_price) / day_before_yesterday_price

if abs(percent_change) >= .05:
    if percent_change > 0:
        up_down = "🔺"
    else:
        up_down = "🔻"

    # Get news from https://newsapi.org
    news_api_key = 'YOUR_NEWS_API_KEY'
    news_url = 'https://newsapi.org/v2/everything'
    news_params = {
        'apiKey': news_api_key,
        'q': 'Tesla',
        'language': 'en',
    }
    news_resp = requests.get(url=news_url, params=news_params)
    news_resp.raise_for_status()
    news_data = news_resp.json()
    news_titles = []
    news_articles = []
    # Put titles and descriptions of most recent three articles into corresponding lists
    for article in news_data['articles'][:3]:
        news_titles.append(article['title'])
        news_articles.append(article['description'])

    # Send an email alert with the percent change and the three most recent news headlines
    email = 'YOUR_EMAIL'
    password = 'YOUR_PASSWORD'
    rounded_change = round(percent_change * 100)

    # Construct body of email
    subject = f"{STOCK}{up_down}{rounded_change}%"
    body = f"{STOCK} saw major movement today. Here's the latest news headlines:\n" \
           f"{news_titles[0]}\n" \
           f"{news_articles[0]}\n\n" \
           f"{news_titles[1]}\n" \
           f"{news_articles[1]}\n\n" \
           f"{news_titles[2]}\n" \
           f"{news_articles[2]}"

    # Build out EmailMessage object for cleaner formatting
    message = EmailMessage()
    message.add_header("From", email)
    message.add_header("To", email)
    message.add_header("Subject", subject)
    message.set_payload(body, 'utf-8')

    # Send message with the appropriate host url. In this example, gmail
    with smtplib.SMTP('smtp-mail.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(msg=str(message).encode('utf-8'), from_addr=email, to_addrs=email)

else:
    print("Not over 5% movement.")
