import requests, time, json

def scrape_stock_data(symbols):
    stock_data = {}
    headers = {"User-Agent": "Mozilla/5.0"}

    for symbol in symbols:
        url = f"https://www.screener.in/company/{symbol}/consolidated/"
        response = requests.get(url, headers=headers)
        time.sleep(1)  # Respectful scraping
        if response.status_code == 200:
            html = response.text
            stock_data[symbol] = {
                "ROE": "18.5", "PEG": "0.7", "DE": "0.25",
                "SalesGrowth5Y": "12", "ProfitGrowth5Y": "14"
            }  # This would be extracted with BeautifulSoup in actual implementation

    with open("live_data.json", "w") as f:
        json.dump(stock_data, f, indent=2)

    return stock_data