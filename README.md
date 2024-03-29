# Job Market Technology Analytics on dou.ua
This project allows you to analyze the job market on dou.ua.
***
## Installation
To get started with the project, clone the repository:

```bash
git clone https://github.com/SevKrok/dou-market-analytics.git
```
Create and activate the virtual environment:

```bash
python -m venv venv
```
```bash
source venv/bin/activate   # for Linux / MacOS
```
```bash
venv\Scripts\activate      # for Windows
```

Install the required packages:

```bash
pip install -r requirements.txt
```
***

## Usage
+ Run the dou.ua website scraper and save the results to the vacancies.csv file:

```bash
scrapy crawl vacancies -O vacancies.csv
```
### For analysis
+ Use the Jupyter Notebook. Open the dou_market.ipynb file in the "analyst" folder and execute all code cells.
***

## Features
With it, you can:

+ View statistics on technology demand in job vacancies.
+ Obtain information about companies with open job positions.
+ Discover the most popular places and cities for work.
***

## Technologies
+ Scrapy for job vacancy scraping
+ Selenium for interacting with dynamic content
+ Jupyter Notebook for data analysis and visualization
+ Pandas for data processing and analysis
+ Matplotlib for creating graphs
***

# Screenshots
***
![Top 30 required technologies for Python Dev on dou.ua vacancies](screenshots/1.jpg)
***

![Top 10 companies by count of vacancies](screenshots/2.jpg)
***

![Top 10 places for work by count of vacancies](screenshots/3.jpg)
***


## Please make sure all required libraries are installed before running the code.

**Note:** Keep in mind that for Selenium to work correctly, you need to have a web driver installed (e.g., ChromeDriver). Ensure that you are using the correct driver version for your browser.