# Sports Performance Analyzer
import os
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
2


def load_and_clean_data(file_name):
    """Load the CSV file and remove invalid score rows."""
    try:
        file_path = os.path.join(os.path.dirname(__file__), file_name)
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        print("Error: scores.csv file was not found.")
        return None
    required_columns = ["Player", "Match", "Score"]

    for column in required_columns:
        if column not in data.columns:
            print("Error: CSV must contain Player, Match and Score columns.")
            return None

    # Convert scores to numbers. Invalid text becomes NaN.
    data["Score"] = pd.to_numeric(data["Score"], errors="coerce")

    # Remove rows with missing names, matches, invalid scores or negative scores.
    data = data.dropna(subset=required_columns)
    data["Player"] = data["Player"].astype(str).str.strip()
    data["Match"] = data["Match"].astype(str).str.strip()
    data = data[
        (data["Player"] != "") &
        (data["Match"] != "") &
        (data["Score"] >= 0)
    ]

    return data


def show_player_stats(data):
    """Display average and best score for every player."""
    player_stats = data.groupby("Player")["Score"].agg(
        Average="mean",
        Best="max",
        Total="sum"
    )

    print("\nPLAYER PERFORMANCE")
    print(player_stats.round(2).to_string())

    top_player = player_stats["Average"].idxmax()
    top_average = player_stats.loc[top_player, "Average"]

    print("\nTop performer:", top_player)
    print("Average score:", round(top_average, 2))


def show_overall_stats(data):
    """Display overall statistics and draw charts."""
    scores = data["Score"]

    print("\nOVERALL STATISTICS")
    print("Mean:", round(np.mean(scores), 2))
    print("Median:", round(np.median(scores), 2))
    print("Standard Deviation:", round(np.std(scores), 2))
    print("Maximum Score:", np.max(scores))

    match_average = data.groupby("Match")["Score"].mean()
    player_average = data.groupby("Player")["Score"].mean()

    print("\nMATCH-WISE AVERAGE")
    print(match_average.round(2).to_string())

    # Line chart: average score in each match.
    plt.figure(figsize=(7, 4))
    plt.plot(match_average.index, match_average.values, marker="o")
    plt.title("Score Trend")
    plt.xlabel("Match")
    plt.ylabel("Average Score")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Bar chart: average score of each player.
    plt.figure(figsize=(7, 4))
    plt.bar(player_average.index, player_average.values)
    plt.title("Player Performance")
    plt.xlabel("Player")
    plt.ylabel("Average Score")
    plt.tight_layout()
    plt.show()


def main():
    print("================================")
    print("  SPORTS PERFORMANCE ANALYZER")
    print("================================")

    data = load_and_clean_data("scores.csv")

    if data is None:
        return

    if data.empty:
        print("\nNo valid data to analyze.")
        return

    print("\nValid records:", len(data))

    while True:
        print("\n1. Player Statistics")
        print("2. Overall Statistics and Charts")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_player_stats(data)
        elif choice == "2":
            show_overall_stats(data)
        elif choice == "3":
            print("Thank you for using the Sports Performance Analyzer!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()