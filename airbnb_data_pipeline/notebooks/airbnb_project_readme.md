# Airbnb Data Deep Dive – Python + Pandas Project

## Overview
This project uses Python and Pandas to analyze Airbnb listings, automating data fetching, cleaning, and exploration.
We focus on New York City listings and build a reproducible data pipeline.

## Project Goals
- Automate downloading Airbnb datasets.
- Clean and preprocess raw data.
- Enrich data with calculated columns.
- Perform exploratory data analysis (EDA).
- Document workflow using Jupyter Notebook.

## Folder Structure
```
airbnb_data_pipeline/
├── data/                  # Raw datasets
├── notebooks/             # Jupyter notebooks per phase
├── scripts/               # Automation scripts (fetch_data.py, etc.)
├── results/               # Analysis outputs (charts, reports)
├── logs/                  # Logs of automated runs
└── README.md              # Project documentation
```

## Tools & Libraries
- Python – Main language
- Pandas – Data manipulation
- Requests – HTTP requests for downloading data
- BeautifulSoup4 – HTML parsing
- Jupyter Notebook – Interactive workflow

## Project Roadmap

### Phase 0 – Setup
- Create folders and subfolders.
- Install packages:
```bash
pip install pandas requests beautifulsoup4 notebook
```

### Phase 1 – Data Collection
- Scrape [Inside Airbnb](http://insideairbnb.com/get-the-data.html) to locate CSV.
- Download `new_york_listings.csv.gz` to `/data`.
- Log success or failures.

### Phase 2 – Data Cleaning
- Load CSV into Pandas.
- Clean price fields and parse dates.
- Handle missing values and remove irrelevant rows.

### Phase 3 – Data Enrichment
- Add `price_per_booking`.
- Categorize availability: Full-time, Part-time, Rare.

### Phase 4 – Analysis
- Top 10 most expensive neighborhoods.
- Average price and availability by room type.
- Host with most listings.
- Listings never reviewed.
- Summarize 3–5 key insights.

## Future Improvements
- Add Matplotlib / Seaborn visualizations.
- Build Streamlit dashboard.
- Schedule automated updates with Cron or Airflow.
- Extend analysis to multiple cities.

## How to Run
1. Clone repo / create project structure.
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Launch Jupyter Notebook:
```bash
jupyter notebook
```
4. Open notebooks in `/notebooks` and run cells sequentially.