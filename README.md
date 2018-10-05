# Pro Football Reference Data Scraper 

This is a Python Application that can manually scrape data from the website https://www.pro-football-reference.com and store that data into a PostgreSQL Database

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

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











### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
