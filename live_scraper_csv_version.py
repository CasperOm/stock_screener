import pandas as pd

def scrape_stock_data(symbols=None):
    # 📌 Use your published Google Sheet CSV link here
    CSV_URL = "https://docs.google.com/spreadsheets/d/11lJoaea87vei3x2PoipA5aydq8VLteqc_Bi01NCi65o/export?format=csv"

    try:
        df = pd.read_csv(CSV_URL)
    except Exception as e:
        raise RuntimeError(f"Error fetching CSV: {e}")

    df.columns = [c.strip() for c in df.columns]

    stock_data = {}
    for _, row in df.iterrows():
        try:
            symbol = row["Name"].replace(" ", "").replace(".", "").upper()
            stock_data[symbol] = {
                "PEG": row.get("PEG", "N/A"),
                "ROE": row.get("ROE %", "N/A"),
                "DE": row.get("Debt / Eq", "N/A"),
                "DividendYield": row.get("Div Yld %", "N/A"),
                "ROCE": row.get("ROCE %", "N/A"),
                "ProfitVar": row.get("Qtr Profit Var %", "N/A"),
                "NetProfit": row.get("NP Qtr Rs.Cr.", "N/A"),
                "CMP": row.get("CMP", "N/A"),
                "1Y_High": row.get("1Y_High", "N/A")
            }
        except Exception as err:
            continue

    return stock_data