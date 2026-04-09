import requests
import json
import time
import os
from datetime import datetime

# Headers set
HEADERS = {"User-Agent": "TrendPulse/1.0"}

KEYWORDS = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

def main():
    if not os.path.exists('data'):
        os.makedirs('data')
        print("Directory 'data' created.")

    # Top 500 story IDs fetch
    try:
        top_ids_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        response = requests.get(top_ids_url, headers=HEADERS)

        if response.status_code != 200:
            print(f"Error fetching IDs: Status {response.status_code}")
            return

        all_ids = response.json()[:500]
        print(f"Fetched {len(all_ids)} story IDs from HackerNews.")
    except Exception as e:
        print(f"Failed to connect to API: {e}")
        return

    final_data = []

    # filtering data as par categories
    for category, words in KEYWORDS.items():
        print(f"Collecting stories for category: {category}...")
        category_count = 0

        for story_id in all_ids:
            if category_count >= 25:
                break

            try:
                item_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
                item_response = requests.get(item_url, headers=HEADERS)

                if item_response.status_code != 200:
                    continue

                story = item_response.json()

                if story and 'title' in story:
                    title_text = story['title'].lower()

                    if any(word in title_text for word in words):
                        record = {
                            "post_id": story.get('id'),
                            "title": story.get('title'),
                            "category": category,
                            "score": story.get('score', 0),
                            "num_comments": story.get('descendants', 0),
                            "author": story.get('by', 'Unknown'),
                            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        }
                        final_data.append(record)
                        category_count += 1
            except:
                print(f"Skipping ID {story_id} due to fetch error.")
                continue

        print(f"Category '{category}' done. Waiting 2 seconds...")
        time.sleep(2)

    # JSON File save
    today_str = datetime.now().strftime("%Y%m%d")
    output_file = f"data/trends_{today_str}.json"

    with open(output_file, 'w') as f:
        json.dump(final_data, f, indent=4)

    print("-" * 30)
    print(f"Collected {len(final_data)} stories. Saved to {output_file}")

if __name__ == "__main__":
    main()
