from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
    url_for,
    current_app
)
import json
import urllib.request
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import requests, validators, json, uuid, pathlib, os
app = Flask(__name__)


@app.route('/')
def get_beer():
    r = requests.get('https://api.punkapi.com/v2/beers/random')
    beerjson = r.json()
    beer = {
        'name': beerjson[0]['name'],
        'abv': beerjson[0]['abv'],
        'desc': beerjson[0]['description'],
        'foodpair': beerjson[0]['food_pairing'][0],
    }
    # print(beer)
    return render_template('index.html', beer=beer)


if __name__ == "__main__":
    app.run(debug=True)
