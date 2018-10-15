# Pro Football Reference Data Scraper 

This is a Python Application that can manually scrape data from the website https://www.pro-football-reference.com and store that data into a PostgreSQL Database

# TODO

- Update code to allow insertion of multiple rows as a batch
- Update code to either delete prior to insert, or update if exists
- Add Unit Testing code

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- An available PostgreSQL Database
- Python 3.6+
- Python Library - psycopg2 (http://initd.org/)
- Python Library - BeautifulSoup4 (https://pypi.org/project/beautifulsoup4/)

### Installing

- If not exists, create a new PostgreSQL database
- Execute Script DDL_nflplayer.table.sql on PostgreSQL database
- Execute Script DDL_nflplayer_passing_stats.table.sql on PostgreSQL database
- Update database.ini file with valid information:
  - host
  - database
  - user
  - password

## Execution

- Navigate to Python script directory;
- Execute Python script: python.exe pro_football_reference_get_players.py
- Execute Python script: python.exe pro_football_reference_get_passing_stats.py	
- Complete!

## Authors

* **Robert Cruz** - *Initial work* - (https://github.com/recruz02)

## Acknowledgments

Thanks to pro-football-reference.com for having good data. Please don't sue me :)
