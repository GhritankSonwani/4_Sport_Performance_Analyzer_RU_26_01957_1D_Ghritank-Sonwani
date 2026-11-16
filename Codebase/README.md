# Sports Performance Analyzer

**Project No.: 4**

## Introduction

My project is called Sports Performance Analyzer. I made it using Python. It takes the scores of players from a CSV file and helps to compare their performance in different matches.

## What the project does

- Reads player names, match numbers and scores from `scores.csv`.
- Checks the data and skips rows that have missing or invalid values.
- Displays each player's average score, highest score and total score.
- Shows which player has the highest average score.
- Calculates the mean, median, standard deviation and maximum score.
- Displays charts to compare match scores and player performance.

## Software and libraries used

- Python 3
- Pandas
- NumPy
- Matplotlib
- Visual Studio Code

## Project files

- `sports_performance_analyzer.py` – the main Python program.
- `scores.csv` – sample player score data used by the program.
- `requirements.txt` – list of Python libraries required for the project.

## How to run

1. Open the `Codebase` folder in VS Code.
2. Open the terminal in that folder.
3. Install the required libraries by running:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Run the program:

   ```bash
   python sports_performance_analyzer.py
   ```

If the `python` command does not work, try `py` instead. Keep `scores.csv` in the same folder as the Python file.

## Menu options

When the program starts, it shows these options:

1. **Player Statistics** – displays the average, highest and total score of each player.
2. **Overall Statistics and Charts** – displays the overall calculations and opens the charts.
3. **Exit** – closes the program.

## Sample data

The CSV file contains these sample entries:

| Player | Match | Score |
|---|---:|---:|
| Aman | 1 | 40 |
| Aman | 2 | 60 |
| Riya | 1 | 30 |
| Riya | 2 | 50 |

With this data, Aman has an average score of 50 and Riya has an average score of 40. So, Aman has the higher average in this sample.

## What I learned

While making this project, I practised reading data from a CSV file, using Python libraries, calculating basic statistics and making graphs. I also learned how to check the data before using it in the program.
