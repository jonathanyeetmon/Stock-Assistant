from flask import Flask, render_template, request
import os
import sys

# Add this path to the system path
parent_dir = os.getcwd()  # Get the current working directory

print("Current sys.path:")
print(sys.path)
sys.path.append(parent_dir)
print("\nNew sys.path:")
print(sys.path)

from webscraper.main import run  # Import after adding the directory to path
