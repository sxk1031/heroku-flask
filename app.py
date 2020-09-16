from flask import Flask, render_template, request, redirect
import numpy as np
import pandas as pd
import re
import urllib.request as request
from bs4 import BeautifulSoup
from collections import Counter
import time
import matplotlib.pyplot as plt
import time
from matplotlib.backends.backend_pdf import PdfPages
import urllib.parse
import unidecode
import seaborn as sns
from collections import Counter
from numpy import percentile

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
  errors = []
  results = {}
  if request.method == 'POST'
  try:
       unique_authors = []
       journal_list = []
       start = 200
       total_papers = 10000
#       start_vals = np.arange(0,np.divmod(total_papers,start)[0])*start
       vals = 0
       url = f'https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term=&terms-0-field=all&classification-physics=y&classification-physics_archives=all&classification-include_cross_list=include&date-year=&date-filter_by=date_range&date-from_date=1993-01-01&date-to_date=&date-date_type=announced_date_first&abstracts=hide&size=200&order=announced_date_first&start={vals}'
  except:
         errors.append('url not found')     
  return render_template('index.html', errors=errors)

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)
