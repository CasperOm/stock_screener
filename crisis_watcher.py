import json

def run_crisis_strategy(stock_data):
    with open("config.json") as f:
        config = json.load(f)

    crisis_picks = []
    for symbol, metrics in stock_data.items():
        try:
            high_price = float(metrics.get("1Y_High", 0))
            current_price = float(metrics.get("CMP", 0))
            drawdown = 100 * (high_price - current_price) / high_price

            if (
                drawdown >= config["crisis_filters"]["panic_drawdown_percent"] and
                float(metrics["ROE"]) >= config["crisis_filters"]["min_roe"] and
                float(metrics["DE"]) <= config["crisis_filters"]["max_de_ratio"]
            ):
                crisis_picks.append((symbol, metrics, drawdown))
        except Exception as e:
            continue

    crisis_picks.sort(key=lambda x: x[2], reverse=True)

    msg = "🚨 <b>Crisis Watch: Hidden Gems in Panic Mode</b>\n"
    for symbol, m, drawdown in crisis_picks[:config["crisis_filters"]["pick_top_n"]]:
        msg += f"📉 <b>{symbol}</b>\n"
        msg += f"💰 <b>Current Price:</b> ₹{m['CMP']} (Down {round(drawdown)}% from peak)\n"
        msg += f"🔺 <b>All-Time High:</b> ₹{m['All_Time_High']}\n"
        msg += f"📈 <b>ROE:</b> {m['ROE']}% (Profit Efficiency)\n"
        msg += f"💼 <b>D/E:</b> {m['DE']} (Debt Load)\n"
        msg += f"📊 <b>PEG:</b> {m['PEG']} (Valuation)\n"
        msg += f"💸 <b>Dividend Yield:</b> {m.get('DividendYield', 'N/A')}%\n"
        msg += f"🔗 <a href='https://www.screener.in/company/{symbol}/'>View Details</a>\n\n"

    if not crisis_picks:
        msg += "❌ No fundamentally strong stocks in panic zone today.\n"

    msg += "\n📂 Based on panic-level valuation + strong fundamentals"
    return msg