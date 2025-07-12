import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from live_scraper_csv_version import scrape_stock_data
from google_sheet_fetcher import get_custom_stocks_from_sheet
from screener_engine import run_screener_strategy
from telegram_bot import send_telegram_message
from crisis_watcher import run_crisis_strategy
# Step 1: Get custom stocks from Google Sheet
custom_symbols = get_custom_stocks_from_sheet()

logger.info(f"Custom symbols: {custom_symbols}")

# Step 2: Scrape live data
data = scrape_stock_data(custom_symbols)

logger.info(f"Data: {data}")

# Step 3: Run filtering logic
message = run_screener_strategy(data)

logger.info(f"Message: {message}")

# Step 4: Send Telegram alert
send_telegram_message(message)

# Step 5: Run crisis logic
message = run_crisis_strategy(data)
logger.info(f"Message: {message}")

# Step 4: Send Telegram alert
send_telegram_message(message)