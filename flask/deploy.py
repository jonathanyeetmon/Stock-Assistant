from flask import Flask, redirect, render_template, request, sessions, url_for
import os
import sys

# Add this path to the system path
parent_dir = os.getcwd()  # Get the current working directory

if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from webscraper.main import run  # Import after adding the directory to path
app = Flask(__name__)
app.secret_key = 'shish'  # You must set a secret key for sessions to work

@app.route('/', methods=['GET'])
def run_scraper_route():
    # Display the form if no input data has been submitted
    if 'input_data' not in request.args:
        return render_template('form.html')
    else:
        # Get input data from query string after form submission
        input_data = request.args.get('input_data')
        #sessions['ticker'] = input_data
        # Call the run function with the input data
        result = run(input_data)
        # Instead of returning jsonify, let's return a simple response for now
        return render_template('results.html', ticker=request.args.get('input_data'), result=result)



if __name__ == '__main__':
    app.run(debug=True)