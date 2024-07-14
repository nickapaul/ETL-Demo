# ETL-Demo

## Overview

This project is designed at a small level to demo and ETL project. I like retro video games and I found a site that had different data that I found interesting. I needed to extract that data, transform the data and flatten it a little, finally load it to a file that I can run different queries on the data (in this case a excel spreadsheet).

## How It Works
1. Makes a call to the GAMEYE API and gets all the Sega Genesis games that are in the US region.
2. Make repeated calls and save games to memory (API only returns 100 games at a time).
3. Remove all games that do not have pricing information.
4. Flatten object a little.
5. Change currency amount to rounded dollars.
6. Load games to a data frame.
7. Create spreadsheet.


## Getting Started
### Prerequisites 
- Python 3.11 installed

### Installation

- To get started with this project, clone the repository to your local machine:
    ```bash
    git clone https://github.com/nickapaul/ETL-Demo.git
    ```
- Next install all packages
    ```bash
    pip install -r requirements.txt
    ```
- You are good to go! Run the job!