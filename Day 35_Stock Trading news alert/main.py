stock_name = "TSLA"
company_name = "Tesla Inc"

STOCK_START = "https://alphavantage.co/query"
STOCK_END = "https://newsapi.org/v2/everything"

STOCK_API_KEY = 
stock_paras = {
    "function": "TIME_SERIES_DAILY"
}
requests.get(STOCK_END, stock_paras)