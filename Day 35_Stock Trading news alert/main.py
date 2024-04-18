import requests

stock_name = "TSLA"
company_name = "Tesla Inc"

STOCK_ENDPOINT = "https://alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "2edb90f3b9214c2fa234da5f4ab67a79"

alphavantage_api = ""

stock_paras = {
    "function": "TIME_SERIES_DAILY",
    "symbol": stock_name,
    "apikey": STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, stock_paras)

# YESTERDAY'S STOCK PRICE
# yesterday_data = response.json()["Time Series (Daily)"]["2024-04-16"]["1. open"]
data1 = response.json()
print(data1)
# data = response.json()["Time Series (Daily)"]
# # print(data)
# data_list = [value for (key, value) in data.items()]
# yesterday_data = data_list[0]
# yesterday_closing_price = yesterday_data["4. close"]
# print(yesterday_closing_price)

# # DAY BEFORE YESTERDAY'S STOCK PRICE
# daybefore_yesterday_data = data_list[1]
# daybefore_yesterday_closing_price = daybefore_yesterday_data["4. close"]
# print(daybefore_yesterday_closing_price)

# # print(daybefore_yesterday_closing_price)

# print(response.json())

# # Increase/decrease in STOCK price
# difference = abs(float(yesterday_closing_price)-float(daybefore_yesterday_closing_price))
# # print(difference)
# average = (float(yesterday_closing_price)+float(daybefore_yesterday_closing_price))/2
# diff_percentage = (difference/average)*100
# print(diff_percentage)
