import requests

response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")

last_twenty_years = response.json()[1][:20]

for y in last_twenty_years:
    display_width = y["value"] // 10_000_000
    print(f'{y["date"]} {"="* display_width}')
