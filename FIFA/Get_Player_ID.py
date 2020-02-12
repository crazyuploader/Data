#!/usr/bin/env python3

# Orginal Post: https://towardsdatascience.com/web-scraping-5649074f3ead

# Import Libraries
import requests
from bs4 import BeautifulSoup
import pandas

# Empty List
Player_ID = []

request = requests.get("https://www.fifa.com/worldcup/players/_libraries/byposition/[id]/_players-list")
soup = BeautifulSoup(request.content, "html.parser")

# 'for' iteration to find all IDs
for IDs in range(0, 5):
    all = soup.find_all("a", "fi-p--link")[IDs]
    Player_ID.append(all['data-player-id'])

# Data frame to store scrapped data
df = pandas.DataFrame({
    "IDs": Player_ID
})
df.to_csv('Player_IDs.csv', index=False)
print(df)
