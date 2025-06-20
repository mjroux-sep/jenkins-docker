from flask import Flask
from flask import render_template
import socket
import random
import os
import argparse

app = Flask(__name__)

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

def choose_color():
    color = os.environ.get('APP_COLOR')
    if not color:
        color = random.choice(list(color_codes.keys()))
        print(f"No environment variable set. Random color chosen: {color}")
    else:
        print(f"Environment variable APP_COLOR set to: {color}")
    
    if color not in color_codes:
        raise ValueError(f"Unsupported color '{color}'. Supported colors: {', '.join(color_codes.keys())}")
    
    return color

# Set the color globally
COLOR = choose_color()

@app.route("/")
def main():
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[COLOR])
