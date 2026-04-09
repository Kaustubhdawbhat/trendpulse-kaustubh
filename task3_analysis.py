import pandas as pd
import numpy as np
import os

def analyze_data():
    # Load and Explore
    file_path = "/content/trends_clean.csv"
    # file_path = "data/trends_clean.csv"

    if not os.path.exists(file_path):
        print("Error: trends_clean.csv are not found.")
        print("Please check csv file.")
        return

    df = pd.read_json(file_path) if file_path.endswith('.json') else pd.read_csv(file_path)
    df = pd.read_csv(file_path)

    print(f"Loaded data shape: {df.shape}")
    print("\nFirst 5 rows of the dataset:")
    print(df.head())

    # Calculating basic averages
    avg_score = df['score'].mean()
    avg_comments = df['num_comments'].mean()
    print(f"\nAverage Score: {avg_score:.2f}")
    print(f"Average Comments: {avg_comments:.2f}")

    # Analysis using NumPy
    print("\nNumPy Statistics: \n")

    # Using NumPy for statistical calculations
    scores_array = df['score'].to_numpy()

    mean_score = np.mean(scores_array)
    median_score = np.median(scores_array)
    std_score = np.std(scores_array)
    max_score = np.max(scores_array)
    min_score = np.min(scores_array)

    print(f"Mean Score: {mean_score:.2f}")
    print(f"Median Score: {median_score}")
    print(f"Standard Deviation: {std_score:.2f}")
    print(f"Highest Score: {max_score}")
    print(f"Lowest Score: {min_score}")

    # Finding category
    top_category = df['category'].value_counts().idxmax()
    top_cat_count = df['category'].value_counts().max()
    print(f"Most stories in: {top_category} ({top_cat_count} stories)")

    most_commented_idx = df['num_comments'].idxmax()
    most_commented_story = df.loc[most_commented_idx]

    print(f"Most commented story: \"{most_commented_story['title']}\" — {most_commented_story['num_comments']} comments")

    # Adding New Columns
    df['engagement'] = df['num_comments'] / (df['score'] + 1)

    df['is_popular'] = df['score'] > avg_score

    print("\nNew columns 'engagement' and 'is_popular' added successfully.")

    # Result save
    output_path = "data/trends_analysed.csv"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"\nAnalysis are complete.\nSaved updated data to {output_path}")

if __name__ == "__main__":
    analyze_data()
