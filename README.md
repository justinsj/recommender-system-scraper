# Recommender System Scraper
This repository is used to acquire data from Amazon's search engine.
It uses Selenium webdriver to read product information from a list of links.
It is implemented in Python.

## Related repositories

- [recommender-system-ui](https://github.com/justinsj/recommender-system-ui): Main Amazon-like React Native testing app
- [recommender-system-analysis](https://github.com/justinsj/recommender-system-analysis): Scripts to perform metric computations 

## Installation
The installation is performed once when downloading the software.

Create a virtual environment at `env`
```
python -m venv env
```
Activate the virtual environment
```
cd env/Scripts
activate.bat
cd ../..
```
Install requirements from `requirements.txt` file

```
python -m pip install -r requirements.txt
```


## Startup
To start using the software, double-click the `start.bat` file

## Usage

```
python main.py -o out_path
```
This will write to {out_path} and tmp.{out_path}, default writes to `outfile`.
Requires that constants/data/data.py has data from executing the `JS/webscraper` in a browser with mobile dimensions (e.g. Samsung Note 20: 415 x 912).
