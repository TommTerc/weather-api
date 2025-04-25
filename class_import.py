# Making a basic API request
import requests
import json
import os
import sys
import time
import random
import math
import datetime
import re
import urllib.parse
import urllib.request
import urllib.error
import logging
import xml.etree.ElementTree as ET
import csv
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt         
api_key = 'eaf68ffb413d707283399af330d02c3f'

# Set up our request
weather_api_url = "https://api.openweathermap.org/data/2.5/weather"

# Parameters for our request
parameters = {
    "q": "New York,US",         # The city we want weather for
    "appid": api_key,    
    "units": "imperial"           # Get temperature in Celsius
}

# Make the request
response = requests.get(weather_api_url, params=parameters)

# Check if request was successful
if response.status_code == 200:
    # Parse the JSON response
    weather_data = response.json()
    
    # Extract and display some data
    city = weather_data["name"]
    temperature = weather_data["main"]["temp"]
    weather = weather_data["weather"][0]["description"]
    
    print(f"Current weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Conditions: {weather}")
else:
    print(f"Error: {response.status_code}")
    print(response.text)