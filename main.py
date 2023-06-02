import requests
from bs4 import BeautifulSoup

# URL of the webpage containing the table
url = "https://tradingeconomics.com/calendar"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Cookie": "calendar-importance=3; cal-timezone-offset=420",
}

# Send a GET request to the webpage
response = requests.get(url, headers=headers)

# Create a BeautifulSoup object with the webpage content
soup = BeautifulSoup(response.content, "html.parser")

# Find the table with the class name "calendar__table"
table = soup.find("table", class_="table-condensed")

# Check if the table was found
if table:
    # Iterate over the rows in the table
    for row in table.find_all("tr"):
        # Extract the data from each cell in the row
        cells = row.find_all("td")
        if len(cells) >= 9:
            # Extract specific data from each cell (you can modify this according to your table structure)
            date = cells[0].text.strip()
            country = cells[1].text.strip()
            events = cells[4].text.strip()
            actual = cells[5].text.strip()
            forecast = cells[8].text.strip()

            # Do something with the extracted data
            print(f"Result: {date} {country} {events} {actual} {forecast}")

# Add any additional logic to process the extracted data here
else:
    print("Table not found on the webpage.")
