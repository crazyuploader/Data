#!/usr/bin/env python3

# Orginal Post: https://towardsdatascience.com/web-scraping-5649074f3ead

# Import Libraries
import requests
from bs4 import BeautifulSoup
import pandas
from collections import OrderedDict

# Fetch IDs from 'Player_IDs.csv' file
Player_ID = pandas.read_csv("Player_IDs.csv")
Ids = Player_ID["IDs"]

# Create a base URL and an empty List
base_url = "https://www.fifa.com/worldcup/players/player/"
player_list = []

# 'for' iteration to scrap data of player(s) from fifa.com
for pages in Ids:
    # Using OrderedDict instead of Dict (See explaination)
    d=OrderedDict()
    # Fetching URLs one by one
    print(base_url+str(pages)+"/profile.html")
    request = requests.get(base_url+str(pages)+"/profile.html")
    # Data Processing
    content = request.content
    soup = BeautifulSoup(content,"html.parser")
    # Scraping Data
    # Name # Country # Role # Age # Height # International Caps # International Goals
    # Creating an exception handler just in case the page doesn't have any Data
    try:
        d['Name'] = soup.find("div",{"class":"fi-p__name"}).text.replace("\n","").strip()
    except:
        print("No Data Available for Player")
        continue
    print(d['Name'])
    d['Country'] = soup.find("div",{"class":"fi-p__country"}).text.replace("\n","").strip()
    d['Role'] = soup.find("div",{"class":"fi-p__role"}).text.replace("\n","").strip()
    d['Age'] = soup.find("div",{"class":"fi-p__profile-number__number"}).text.replace("\n","").strip()
    d['Height(cm)'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[1].text.replace("\n","").strip()
    d['International Caps'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[2].text.replace("\n","").strip()
    d['International Goals'] = soup.find_all("div",{"class":"fi-p__profile-number__number"})[3].text.replace("\n","").strip()
    player_list.append(d)
    # Create a pandas DataFrame to store data and save it to .csv
    df = pandas.DataFrame(player_list)
    df.to_csv('Players_Info.csv', index = False)

print("\nSuccess \n")
