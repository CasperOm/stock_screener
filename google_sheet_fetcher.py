import requests

def get_custom_stocks_from_sheet():
    # Public CSV export of Google Sheet
    SHEET_URL = "https://docs.google.com/spreadsheets/d/1VlAOPU6GjcU-Aw5am0YQFw-k81i6bkjChqp-xg9POwo/export?format=csv"
    response = requests.get(SHEET_URL)
    lines = response.text.splitlines()
    return [line.strip() for line in lines if ".NS" in line]