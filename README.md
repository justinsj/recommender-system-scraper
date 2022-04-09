# Rec Sys Ui Scraper

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