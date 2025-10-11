# ProductInsightBot - Watch Analysis AI Agent

ProductInsightBot is an intelligent AI agent designed to analyze and provide insights about watch products. This project was developed as part of an AI Engineer Intern assignment, demonstrating skills in web scraping, data analysis, and natural language processing.

## Features
- **Web Scraping**: Automated data collection from e-commerce websites
- **Natural Language Processing**: Understands conversational queries about watches
- **Price Analysis**: Compares prices, finds expensive/affordable watches
- **Rating Filtering**: Filters products by customer ratings
- **Brand Comparison**: Analyzes and compares different watch brands
- **Category Insights**: Provides insights across Smartwatch, Luxury, Sports, Fashion, Digital, and Analog categories

## Technologies Used
- **Python 3.x** - Core programming language
- **Pandas** - Data manipulation and analysis
- **BeautifulSoup4** - Web scraping and HTML parsing
- **Requests** - HTTP requests for web scraping
- **SQLite** - Database storage
- **Regular Expressions** - Natural language pattern matching

## Project Structure
ProductInsightBot/
├── data_collector.py # Web scraping and data generation
├── product_insight_bot.py # Main AI agent with NLP capabilities
├── products.csv # Generated product data (CSV format)
├── products.db # Database file (SQLite format)
├── requirements.txt # Project dependencies
└── README.md # Project documentation


## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone https://github.com/GurmanpreetKaur23/ProductInsightBot.git
cd ProductInsightBot
```
### Step 2: Install Dependencies
``` bash
pip install -r requirements.txt
```
### Step 3: Generate Product Data
``` bash
python data_collector.py
```
### Step 4: Run the AI Agent
``` bash
python product_insight_bot.py
```

## Usage Examples
Once the bot is running, you can ask questions like:

### Price Queries
**"Which watch is the most expensive?"**

**"Show me watches under ₹10000"**

**"What is the average price of smartwatches?"**

### Rating Queries
**"Show me watches with rating above 4.5"**

**"Which Titan watches have the best ratings?"**

**"Highest rated sports watches"**

### Brand Analysis
**"Compare Titan and Casio prices"**

**"Samsung watch analysis"**

**"Apple vs Noise smartwatches"**

### Category Insights
**"Smartwatch average price"**

**"Luxury watches under ₹20000"**

**"Sports watches with most reviews"**

### General Queries
**"Show me all categories"**

**"Which watch has the most reviews?"**

**"Price range of all watches"**

## Data Collection Approach

### Web Scraping Strategy
**Attempts to scrape real watch data from Amazon India**

**Implements respectful scraping with delays between requests**

**Uses proper headers to mimic browser behavior**

**Handles errors gracefully with fallback mechanisms**

### Fallback Data Generation
**Generates realistic sample data if scraping fails**

**Includes 200+ watch products across 6 categories**

**Realistic pricing, ratings, and review counts**

**Covers popular brands like Titan, Casio, Apple, Samsung, etc.**

### Categories Covered

Category	Description	Popular Brands
Smartwatch	Fitness trackers, smart features	Apple, Samsung, Noise, Boat
Luxury	Premium, high-end watches	Titan, Fossil, Casio, Timex
Sports	Fitness and outdoor watches	Casio, G-Shock, Fastrack
Fashion	Style-focused, designer watches	Sonata, Maxima, Esprit
Digital	LED displays, digital features	Casio, Timex, Fastrack
Analog	Traditional watch designs	Titan, HMT, Timex

### Technical Implementation
## Data Collection (data_collector.py)
**Web scraping with error handling**

**Automatic category classification**

**Brand extraction from product names**

**CSV and SQLite database storage**

## AI Agent (product_insight_bot.py)
**Pattern-based natural language understanding**

**Category and brand recognition**

**Statistical analysis and filtering**

**User-friendly conversational interface**

### Troubleshooting
## Common Issues
**Web scraping fails:** The system automatically uses generated sample data

**Module not found:** Run pip install -r requirements.txt

**Database errors:** Delete products.db and run data_collector.py again

## Data Sources
**Primary:** Amazon India (web scraping)

**Fallback:** Generated sample data with realistic watch information
