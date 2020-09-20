# conda create -n indeed python=3.7 requests jupyter beautifulsoup4

import json
from random import uniform
from time import sleep

import requests
from bs4 import BeautifulSoup

INDEED_URL = 'https://www.indeed.com'
NUM_PAGES = 5
OUTPUT_FILE = './indeed_job_descs_{}.json'

titles = ['ux+designer', 'recruiter', 'marketing', 'sales', 'office+manager', 'data+architect', 'frontend+developer', 'fullstack+engineer',
          'test+engineer', 'site+reliability+engineer', 'data+science+manager', 'human+resource+specialist', 'talent+management', 'engineering+manager',
          'scientist', 'technician']
for title in titles:
    request_params = {
        'q': title,
        'l': 'New York State',
        'jt': 'fulltime'}
    
    job_descs = []
    for i in range(NUM_PAGES):
        # Step 1, get the search page results
        request_params.update({'start': i * 10})
        indeed_response = requests.get(url=INDEED_URL + '/jobs',
                                       params=request_params)
    
        if indeed_response.status_code != 200:
            print('non-200 response for search page, skipping')
            continue
    
        indeed_search_html = indeed_response.text
        parsed_job_searches = BeautifulSoup(indeed_search_html, 'html.parser')
        posting_divs = parsed_job_searches.find_all(
            'div',
            attrs={"class": ["row", "result", "clickcard"]})
        job_ids = [div.attrs['data-jk'] for div in posting_divs]
    
        # Get the individual job descriptions
        for job_id in job_ids:
            posting_response = requests.get(url=INDEED_URL + '/viewjob',
                                            params={'jk': job_id})
            indeed_job_html = posting_response.text
            if posting_response.status_code != 200:
                print('non-200 response for job description page, skipping')
                continue
            parsed_job_post = BeautifulSoup(indeed_job_html, 'html.parser')
            job_div = parsed_job_post.find(
                'div',
                attrs={'class': 'jobsearch-JobComponent-description'})
            # Checks if there's data at all
            if job_div:
                job_descs.append(job_div.get_text())
    
            # Because you're scraping, this slows down your request!
            sleep(uniform(0.2, 1.2))
    
    
    json.dump({'request_params': request_params,
               'job_descriptions': job_descs},
              open(OUTPUT_FILE.format(request_params['q']), 'w'))
