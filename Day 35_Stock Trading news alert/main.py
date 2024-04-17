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
print(response)