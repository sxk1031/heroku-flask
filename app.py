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

app = Flask(__name__)
#from models import Result

@app.route('/',methods=['GET','POST'])
def index():
	errors = []
	results = []
	if request.method == 'POST':
		try:
			unique_authors = []
			journal_list = []
			start = 200
			total_papers = request.form['number']
			start_vals = np.arange(0,np.divmod(total_papers,start)[0])*start
			print('*****',vals,start_vals,total_papers)

			for vals in start_vals:
				url = f'https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term=&terms-0-field=all&classification-physics=y&classification-physics_archives=all&classification-include_cross_list=include&date-year=&date-filter_by=date_range&date-from_date=1993-01-01&date-to_date=&date-date_type=announced_date_first&abstracts=hide&size=200&order=announced_date_first&start={vals}'
				html = urequest.urlopen(url).read()
				soup = BeautifulSoup(html,features="html.parser")
				for script in soup(["script", "style"]):
					script.decompose()
				strips = list(soup.stripped_strings)

				auth_sw = 0    
				journal_sw = 0
				for string in strips:
					if (journal_sw == 1):           
						re_journ = re.search(r'[a-zA-Z\&.\s]+',string)
						if re_journ:
							re_journ_clean = re.sub(' ','',re_journ.group())
							re_journ_clean = re.sub(r'\.','',re_journ_clean)
							journal_list += [re_journ_clean.lower()]  
							journal_sw = 0
					if (auth_sw == 1):
						if (string != ',' and string != 'Submitted'):
							unique_authors += [string]  
					if (string == 'Authors:'):
						auth_sw = 1    
					if (string == 'Submitted'):
						auth_sw = 0
					if (string == 'Journal ref:'):    
						journal_sw = 1
#			results=unique_authors
			top_journals = Counter(journal_list).most_common(25)
#			results = {'a':1, 'b':2, 'c':3}
			results = top_journals
			print(top_journals)
		except:
			errors.append('url not found')     
	return render_template('index.html', results=results, errors=errors)

#@app.route('/about')
#def about():
#	return render_template('about.html')

if __name__ == '__main__':
	app.run(port=33507)
