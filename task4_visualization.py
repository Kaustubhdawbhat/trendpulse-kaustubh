import pandas as pd
import matplotlib.pyplot as plt
import os

def create_visualizations():
    # Setup
    file_path = "/content/trends_analysed.csv"
    if not os.path.exists(file_path):
        print("Error: trends_analysed.csv not found.")
        print("Please check csv file.")
        return

    df = pd.read_csv(file_path)

    if not os.path.exists('outputs'):
        os.makedirs('outputs')
        print("Directory 'outputs' created.")

    # Chart 1 - Top 10 Stories by Score
    plt.figure(figsize=(10, 6))

    top_10 = df.nlargest(10, 'score').copy()

    top_10['short_title'] = top_10['title'].apply(lambda x: x[:47] + "..." if len(x) > 50 else x)

    plt.barh(top_10['short_title'], top_10['score'], color='skyblue')
    plt.xlabel('Score (Upvotes)')
    plt.ylabel('Story Title')
    plt.title('Top 10 Stories by Score')
    plt.gca().invert_yaxis()
    plt.tight_layout()

    plt.savefig('outputs/chart1_top_stories.png')
    plt.show()

    # 2 - Stories per Category
    plt.figure(figsize=(10, 6))
    category_counts = df['category'].value_counts()


    colors = ['red', 'blue', 'green', 'orange', 'purple']
    category_counts.plot(kind='bar', color=colors[:len(category_counts)])

    plt.xlabel('Category')
    plt.ylabel('Number of Stories')
    plt.title('Distribution of Stories per Category')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig('outputs/chart2_categories.png')
    plt.show()

    # Chart 3 - Score vs Comments
    plt.figure(figsize=(10, 6))

    popular = df[df['is_popular'] == True]
    not_popular = df[df['is_popular'] == False]

    plt.scatter(not_popular['score'], not_popular['num_comments'], color='gray', label='Not Popular', alpha=0.6)
    plt.scatter(popular['score'], popular['num_comments'], color='gold', label='Popular', edgecolors='black')

    plt.xlabel('Score')
    plt.ylabel('Number of Comments')
    plt.title('Relationship: Score vs Comments')
    plt.legend()
    plt.tight_layout()

    plt.savefig('outputs/chart3_scatter.png')
    plt.show()

    fig, axs = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('TrendPulse Dashboard', fontsize=20)

    # 1. Top Stories (Horizontal Bar)
    axs[0, 0].barh(top_10['short_title'], top_10['score'], color='skyblue')
    axs[0, 0].set_title('Top 10 Stories')
    axs[0, 0].invert_yaxis()

    # 2. Category Distribution (Bar)
    category_counts.plot(kind='bar', ax=axs[0, 1], color=colors[:len(category_counts)])
    axs[0, 1].set_title('Stories per Category')

    # 3. Score vs Comments (Scatter)
    axs[1, 0].scatter(df['score'], df['num_comments'], c=df['is_popular'].map({True: 'gold', False: 'gray'}))
    axs[1, 0].set_title('Score vs Comments')
    axs[1, 0].set_xlabel('Score')
    axs[1, 0].set_ylabel('Comments')

    # 4. Hide the 4th subplot (empty)
    axs[1, 1].axis('off')
    axs[1, 1].text(0.1, 0.5, 'Pipeline Complete!', fontsize=15, fontweight='bold')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('outputs/dashboard.png')
    plt.show()

    print("\nVisualizations complete. Check the 'outputs/' folder for PNG files.")

if __name__ == "__main__":
    create_visualizations()
