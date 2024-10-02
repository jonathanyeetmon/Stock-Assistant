# AI Powered Stock Assistant
## Overview

This stock assistant is a web application that combines sentiment analysis with technical indicators to provide data-driven trade recommendations. This app is designed to help traders make informed decisions by leveraging real time news sentiment and traditional technical analysis tools.

## Features

- **Sentiment Analysis**: Scrapes and analyzes news platforms to gauge the sentiment around a specific stock or cryptocurrency using fine tuned roBERTa model.
- **Technical Indicators**: Integrates popular technical indicators like Moving Averages (MA), Relative Strength Index (RSI), and Bollinger Bands to assess market conditions.
- **Recommendation Engine**: Based on the sentiment score and technical signals, the app suggests optimal buy/sell actions.
- **Real-time Updates**: The app provides real time analaysis using live data feeds.

## Tech Stack

- **Backend**: Python Flask for handling API requests and running sentiment analysis models.
- **Sentiment Analysis**: Natural Language Processing (NLP) using a LLM approach
- **Technical Indicators**: Webscraped live off of Trading View.
- **Data Sources**: Google news through Gnews api.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/jonathanyeetmon/Stock-Assistant.git

2. Install needed libraries in a env with Python 3.12 (or other versions)

    ```bash
    pip install selenium
    pip install gnews
    pip install Flask

3. Run the driver
   ```bash
   python run.py




   
