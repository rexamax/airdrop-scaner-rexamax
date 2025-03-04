import requests
from bs4 import BeautifulSoup
import json

def fetch_airdrops():
    url = "https://airdrops.io/"  # You can add other sources
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Request error from airdrops.io")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    airdrops = []
    
    for card in soup.select(".airdrop-card"):
        title = card.select_one(".airdrop-title").text.strip()
        reward = card.select_one(".reward").text.strip() if card.select_one(".reward") else "N/A"
        network = card.select_one(".network").text.strip() if card.select_one(".network") else "Unknown"
        link = card.select_one("a")["href"]
        
        airdrops.append({
            "title": title,
            "reward": reward,
            "network": network,
            "link": link
        })
    
    return airdrops

if __name__ == "__main__":
    airdrop_data = fetch_airdrops()
    print(json.dumps(airdrop_data, indent=4, ensure_ascii=False))
