# Trading Economic Calendar Scrap

## Introduction
Python Scripts which scrapes news events from the news calendar at tradingeconomics.com by High Impact News

## Installation
```bash
pip install requests
pip install bs4
```
## Usage
```typescript
#Set your calendar-importance=3 (3 = Means High Impact) & cal-timezone-offset=420
"Cookie": "calendar-importance=3; cal-timezone-offset=420",
```
```typescript
# Extract specific data from each cell (you can modify this according to your table structure)
date = cells[0].text.strip()
country = cells[1].text.strip()
events = cells[4].text.strip()
actual = cells[5].text.strip()
forecast = cells[8].text.strip()

# Do something with the extracted data
print(f"Result: {date} {country} {events} {actual} {forecast}")
```
## Result
![Screenshot_22](https://github.com/naufaljct48/TradingEconomicCalendarScrap/assets/30202760/34c8d347-1cde-4e4d-809e-7e89ca63d208)
