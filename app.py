from flask import Flask, render_template, request, redirect
import numpy as np
import pandas as pd
import re
import urllib.request as urequest
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
from journal_name_dictionary import journal_name_dict
import dill

app = Flask(__name__)
#from models import Result

@app.route('/',methods=['GET','POST'])
def index():
	errors = []
	results = {}
	if request.method == 'POST':
		unique_authors = dill.load(open('unique_authors.pkd', 'rb'))
		journal_list = dill.load(open('journal_list.pkd', 'rb'))
#		results=unique_authors
		n_journal = request.form['number']
		top_journals = Counter(journal_list).most_common(int(n_journal))
		results = top_journals
#		results = {journal_name_dict[i]:j for i,j in top_journals}
#		print(top_journals)
	return render_template('index.html', results=results)

#@app.route('/about')
#def about():
#	return render_template('about.html')

if __name__ == '__main__':
	app.run(port=33507)
