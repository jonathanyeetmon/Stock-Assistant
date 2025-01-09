from flask import Flask, redirect, render_template, request, sessions, url_for
import os
import sys
import json

# Add this path to the system path
parent_dir = os.getcwd()  # Get the current working directory

if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from webscraper.main import run  # Import after adding the directory to path
from helpers import count_techs

app = Flask(__name__)
app.secret_key = 'shish'  # You must set a secret key for sessions to work

@app.route('/', methods=['GET'])
def run_scraper_route():
    if 'input_data' not in request.args:
        return render_template('form.html')
    # Example sentiment analysis recommendation
    input_data = request.args.get('input_data').upper()
    try:
        sentiment_recommendation = run(input_data)
    except Exception as e:
        return render_template('error.html', ticker= input_data)

    indicators_path = os.path.join(parent_dir, 'webscraper', 'indicators.json')
    # Load the indicators from the JSON file
    with open(indicators_path, 'r') as f:
        indicators = json.load(f)

    # Skip the first line of the JSON data (headers)
    indicators = indicators[1:] if len(indicators) > 1 else []
    
    rec = count_techs(indicators)

    # Render the template
    return render_template(
        'results.html',
        ticker= input_data,
        result="Evaluation Results",
        sentiment_recommendation=sentiment_recommendation,
        indicators=indicators,
        tech_rec = rec
    )


if __name__ == '__main__':
    app.run(debug=True)
