import pandas as pd
import glob
import os

def process_data():
    # Loading the JSON File
    json_files = glob.glob("/content/trends_20260409.json")

    if not json_files:
        print("Error: JSON files are not found in data folder.")
        print("Please check JSON file.")
        return

    latest_file = max(json_files, key=os.path.getctime)

    print(f"Loading data from: {latest_file}")
    df = pd.read_json(latest_file)
    print(f"Loaded {len(df)} stories.")

    # Clean the Data

    df = df.drop_duplicates(subset=['post_id'])
    print(f"After removing duplicates: {len(df)}")

    df = df.dropna(subset=['post_id', 'title', 'score'])
    print(f"After removing nulls: {len(df)}")

    df['score'] = df['score'].astype(int)
    df['num_comments'] = df['num_comments'].astype(int)

    df = df[df['score'] >= 5]
    print(f"After removing low scores (< 5): {len(df)}")

    df['title'] = df['title'].str.strip()

    # Save as CSV and Summary
    output_path = "data/trends_clean.csv"

    # Create the 'data' directory if it doesn't exist
    os.makedirs('data', exist_ok=True)

    df.to_csv(output_path, index=False)

    print("-" * 30)
    print(f"Saved {len(df)} rows to {output_path}")

    # Print the required summary of stories per category
    print("\nStories per category:")
    summary = df['category'].value_counts()
    print(summary)

if __name__ == "__main__":
    process_data()
