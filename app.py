from flask import Flask, render_template, request, redirect
import numpy as np
import pandas as pd
import re
import urllib.request as request
from bs4 import BeautifulSoup
from collections import Counter
import time
import matplotlib.pyplot as plt
%matplotlib inline
import time
from matplotlib.backends.backend_pdf import PdfPages
import urllib.parse
import unidecode
import seaborn as sns
from collections import Counter
from numpy import percentile

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)
