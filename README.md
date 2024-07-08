[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

# My Python Scripts Collection

This repository contains multiple Python scripts for various tasks. Each script is explained below. I wanted to create this repository to hold all the scripts I make in case a developer could use these in the future.

# Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

# Scripts

<details>
<summary>Volleyball Stats Script</summary>

### Volleyball Stats Cleaner

This script cleans and formats volleyball statistics data. The script reads raw data, cleans it, and outputs a structured DataFrame. Optionally, it can save the cleaned data to a CSV file.

#### Features

- Reads raw volleyball statistics data from a multi-line string.
- Cleans and formats the data into a pandas DataFrame.
- Outputs the clean data to a new CSV file.

#### Prerequisites

- Python 3.x
- pandas library

#### Installation

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install pandas**: Open your command line interface (CLI) or terminal and run the following command:

    ```bash
    pip install pandas
    ```

#### Usage

1. **Clone the repository**:

     ```bash
    git clone https://github.com/your-username/your-repo-name.git](https://github.com/JustJakee/PythonScripts.git
    cd PythonScripts
    ```

2. **Run the script**:

    ```bash
    python clean_volleyball_stats.py
    ```

#### Example Data Input

```plaintext
Jersey|MatchGamesPlayed|TotalServes|ServingAces|ServingErrors|ServingPoints|AttacksAttempts|AttacksKills|AttacksErrors|ServingReceivedSuccess|ServingReceivedErrors|BlocksSolo|BlocksAssists|BlocksErrors|BallHandlingAttempt|Assists|AssistsErrors|Digs|DigsErrors
3|5|18|1|3|8|0|0|0|28|0|0|0|0|6|0|0|13|0
4|3|0|0|0|0|5|1|2|0|0|0|2|0|0|0|0|1|0
```

#### Example Data Output

| Jersey | MatchGamesPlayed | TotalServes | ServingAces | ServingErrors | ServingPoints | AttacksAttempts | AttacksKills | AttacksErrors | ServingReceivedSuccess | ServingReceivedErrors | BlocksSolo | BlocksAssists | BlocksErrors | BallHandlingAttempt | Assists | AssistsErrors | Digs | DigsErrors |
|--------|-------------------|-------------|--------------|---------------|----------------|------------------|--------------|---------------|-------------------------|------------------------|-------------|----------------|--------------|----------------------|---------|----------------|------|------------|
| 3      | 5                 | 18          | 1            | 3             | 8              | 0                | 0            | 0             | 28                      | 0                      | 0           | 0              | 0            | 6                    | 0       | 0              | 13   | 0          |
| 4      | 3                 | 0           | 0            | 0             | 0              | 5                | 1            | 2             | 0                       | 0                      | 0           | 2              | 0            | 0                    | 0       | 0              | 1    | 0          |
| 5      | 2                 | 0           | 0            | 0             | 0              | 3                | 1            | 2             | 0                       | 0                      | 0           | 0              | 0            | 1                    | 0       | 1              | 0    | 0          |
| 7      | 5                 | 19          | 2            | 2             | 8              | 32               | 11           | 4             | 26                      | 1                      | 0           | 0              | 0            | 2                    | 1       | 1              | 9    | 0          |
| 8      | 5                 | 21          | 2            | 1             | 10             | 70               | 22           | 6             | 31                      | 0                      | 0           | 0              | 0            | 14                   | 7       | 0              | 22   | 0          |
| 9      | 5                 | 10          | 0            | 1             | 2              | 28               | 11           | 6             | 0                       | 0                      | 0           | 0              | 0            | 0                    | 0       | 0              | 2    | 0          |
| 10     | 4                 | 0           | 0            | 0             | 0              | 11               | 1            | 2             | 1                       | 0                      | 1           | 4              | 0            | 0                    | 0       | 0              | 3    | 0          |
| 11     | 5                 | 15          | 1            | 4             | 4              | 30               | 13           | 6             | 4                       | 0                      | 1           | 6              | 0            | 111                  | 41      | 0              | 12   | 0          |
| 12     | 5                 | 24          | 2            | 0             | 15             | 0                | 0            | 0             | 0                       | 0                      | 0           | 0              | 0            | 3                    | 1       | 0              | 8    | 0          |
| 13     | 5                 | 4           | 0            | 0             | 3              | 0                | 0            | 0             | 1                       | 0                      | 0           | 0              | 0            | 37                   | 10      | 1              | 5    | 0          |

</details>

<details>
<summary>CSV to JSON Converter</summary>

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/your-repo-name.git](https://github.com/JustJakee/PythonScripts.git
    cd PythonScripts
    ```

2. **Verify Python is installed** (Download and install Python from [python.org](https://www.python.org/downloads/) if applicable.):

3. **Create your CSV** (within your directory example: _MonopolyGoCards.csv_):
   
    ```csv
    card_name, card_set, card_number
    Starlit Ceremony,Opening Ceremony,1
    Blue Barons,Opening Ceremony,2
    Green Gladiators,Opening Ceremony,3
    Gold Stars,Opening Ceremony,4
    Orange Optimists,Opening Ceremony,5
    Pink Pioneers,Opening Ceremony,6
    Red Respect,Opening Ceremony,7
    Final Countdown,Opening Ceremony,8
    The Games Begin,Opening Ceremony,9
    ```
3. **Run the script**:

    ```bash
    python csv_to_json.py
    ```

4. **Verify the output** of your new file (example: _MonopolyGoCards.json_):
   
   ```json
    {
        "Opening Ceremony": [
            {
                "card_name": "Starlit Ceremony",
                "card_set": "Opening Ceremony",
                "card_number": 1
            },
            {
                "card_name": "Blue Barons",
                "card_set": "Opening Ceremony",
                "card_number": 2
            },
            {
                "card_name": "Green Gladiators",
                "card_set": "Opening Ceremony",
                "card_number": 3
            },
            {
                "card_name": "Gold Stars",
                "card_set": "Opening Ceremony",
                "card_number": 4
            },
            {
                "card_name": "Orange Optimists",
                "card_set": "Opening Ceremony",
                "card_number": 5
            },
            {
                "card_name": "Pink Pioneers",
                "card_set": "Opening Ceremony",
                "card_number": 6
            },
            {
                "card_name": "Red Respect",
                "card_set": "Opening Ceremony",
                "card_number": 7
            },
            {
                "card_name": "Final Countdown",
                "card_set": "Opening Ceremony",
                "card_number": 8
            },
            {
                "card_name": "The Games Begin",
                "card_set": "Opening Ceremony",
                "card_number": 9
            }
        ]
    }
    ```
</details>

<!-- Add more scripts here in a similar format

<details>
<summary>Volleyball Stats Cleaner</summary>
</details>

-->
