from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
    url_for,
    current_app
)
import urllib.request
from urllib.parse import urlparse,urljoin
from bs4 import BeautifulSoup
import requests, validators, json,uuid,pathlib,os
app = Flask(__name__)


@app.route("/",methods=("GET", "POST"), strict_slashes=False)
def index():
    # Actual parsing codes goes here
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
