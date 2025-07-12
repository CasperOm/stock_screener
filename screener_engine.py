import json

def run_screener_strategy(data):
    with open("config.json") as f:
        config = json.load(f)

    picks = []
    for symbol, metrics in data.items():
        try:
            if float(metrics["PEG"]) <= config["daily_filters"]["max_peg"] and \
                float(metrics["ROE"]) >= config["daily_filters"]["min_roe"] and \
                float(metrics["DE"]) <= config["daily_filters"]["max_de_ratio"] and \
                float(metrics.get("DividendYield", 0)) >= config["daily_filters"].get("min_div_yield", 0) and \
                float(metrics["ROCE"]) >= 15 and float(metrics["ProfitVar"]) >= 10 and float(metrics["NetProfit"]) >= 5:
                    picks.append((symbol, metrics))
        except:
            continue

    msg = "📊 Handpicked Stocks to Watch Today!\n\n🧠 Based on:\n• Growth at Reasonable Price (GARP)\n• Value Investing 📉\n• High Quality Businesses 💎\n\n"
    for symbol, m in picks[:config["pick_top_n"]]:
        msg += f"✅ <b>{symbol}</b>\n"
        msg += f"💰 <b>Price:</b> ₹{m.get('CMP', 'N/A')}\n"
        msg += f"💸 <b>Dividend Yield:</b> {m.get('DividendYield', 'N/A')}%\n"
        msg += f"📈 <b>ROE:</b> {m['ROE']}% (Profitable)\n"
        msg += f"📉 <b>PEG:</b> {m['PEG']} (Valuation)\n"
        msg += f"💼 <b>Debt-to-Equity:</b> {m['DE']}\n"
        msg += f"🔗 <a href='https://www.screener.in/company/{symbol}/'>View on Screener</a>\n\n"

    msg += "🧪 Strategy: Mix of proven 10Y data 📊 + live market data 📡\n"
    msg += "💬 For more: @OmStockGuruBot"
    return msg