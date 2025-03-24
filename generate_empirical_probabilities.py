from bs4 import BeautifulSoup
import json
import re
import requests


def parse_soup_seed(base_seed: str, soup: BeautifulSoup):
    """Given a specific NCAA bracket seed, parse the site to pull the records vs each seed."""
    # Locate the section with "Overall tournament record of #x seeds"
    section = soup.find("b", string=re.compile(f"Overall tournament record of #{base_seed}"))

    # Collect spans only until the next <b> tag
    data = {}
    current = section.find_next_sibling()
    while current and not (current.name == "b" and "Overall tournament record" in current.text):
        if current.name == "span" and "hovl" in current.get("class", []):
            text = current.text.strip()
            match = re.findall(r"vs\. #(\d+)\s+\((\d+)-(\d+)\)\s+([\d\.]+)%", text)
            if match:
                seed, wins, losses, pct = match[0]
                seed = int(seed)
                wins = int(wins)
                losses = int(losses)
                pct = float(pct)
                if seed >= int(base_seed):
                    if wins + losses == 0:
                        if int(base_seed) + 5 <= seed:
                            data[seed] = 99.0
                        else:
                            data[seed] = 50.0
                    else:
                        if pct >= 99.0:
                            data[seed] = 99.0
                        else:
                            data[seed] = pct
        current = current.find_next_sibling()  # Move to next element
    
    return data


def main():
    # URL of the site
    url = "https://mcubed.net/ncaab/seeds.shtml"

    # Send a GET request
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors

    # Parse the HTML
    soup = BeautifulSoup(response.text, "html.parser")
    
    seeds = [str(i) for i in range(1, 17)]
    full_dict = {}
    for seed in seeds:
        full_dict[int(seed)] = parse_soup_seed(base_seed=seed, soup=soup)
    
    with open('empirical_history_dict.json', 'w') as fp:
        json.dump(full_dict, fp)


if __name__ == "__main__":
    main()
