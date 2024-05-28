# WebScraper for Mortgage Agent Database

## Overview

This repository contains a web scraper designed to extract information about mortgage agents from a specified online database. The scraper is built using Python and leverages libraries such as BeautifulSoup for parsing HTML and requests for handling HTTP requests.

## Features

- Extracts agent names
- Extracts license numbers
- Extracts additional license information (e.g., license status, expiry date)
- Saves the scraped data into a structured format (CSV, JSON)

## Prerequisites

Before running the scraper, ensure you have the following installed:

- Python 3.x
- pip (Python package installer)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/cashly.git
    cd webscraper
    ```

2. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage


1. **Run the scraper:**
    ```bash
    python fsco.py
    ```

3. **Output:**
   - The scraped data will be saved to a a csv file called agents.csv
   - The default format is CSV, but this can be changed in excel 

## File Structure

- `fsco.py`: The main script for running the web scraper.
- `requirements.txt`: List of Python packages required to run the scraper.

