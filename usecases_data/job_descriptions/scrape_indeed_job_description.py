# conda create -n indeed python=3.7 requests jupyter beautifulsoup4
import logging
import json
from random import uniform
from time import sleep
from datetime import datetime

import requests
from bs4 import BeautifulSoup

log_file = 'indeed_scrape.log'
logging.basicConfig(format="%(asctime)-15s %(message)s",
                    filename=log_file,
                    level=logging.INFO)
INDEED_URL = 'https://www.indeed.com'
NUM_PAGES = 3
today = datetime.today().strftime('%Y_%m_%d')
OUTPUT_FILE = './indeed_job_descs_{}.json'.format(today)

titles = ['ux+designer', 'recruiter', 'marketing', 'sales', 'office+manager',
          'frontend+developer', 'fullstack+engineer',
          'test+engineer', 'site+reliability+engineer', 'data+architect',
          'human+resource+specialist', 'business+analyst',
          'engineering+manager', 'researcher',
          'researcher', 'data+scientist', 'software+developer',
          'statistician', 'deep+learning', 'machine+learning+engineer',
          'actuary', 'financial+analyst', 'econmist', 'financial+engineer',
          'political+analyst', 'data+journalist']

all_jobs = []
for title in titles:
    request_params = {
        'q': title,
        'l': 'New York State',
        'jt': 'fulltime'}

    job_descs = {}
    for i in range(NUM_PAGES):
        # Step 1, get the search page results
        request_params.update({'start': i * 10})
        indeed_response = requests.get(url=INDEED_URL + '/jobs',
                                       params=request_params)

        if indeed_response.status_code != 200:
            logging.error(
                'non-200 response for title {}, page {}, skipping'.format(
                    title, i))
            continue

        indeed_search_html = indeed_response.text
        parsed_job_searches = BeautifulSoup(indeed_search_html, 'html.parser')
        posting_divs = parsed_job_searches.find_all(
            'div',
            attrs={"class": ["row", "result", "clickcard"]})
        job_ids = [div.attrs['data-jk'] for div in posting_divs]
        logging.info('for title {}, page {}, detecting {} ids'.format(
            title, i, len(job_ids)))

        # Get the individual job descriptions
        for job_id in job_ids:
            posting_response = requests.get(url=INDEED_URL + '/viewjob',
                                            params={'jk': job_id})
            indeed_job_html = posting_response.text
            if posting_response.status_code != 200:
                logging.error('non-200 response for job description page, skipping')
                continue
            parsed_job_post = BeautifulSoup(indeed_job_html, 'html.parser')
            job_div = parsed_job_post.find(
                'div',
                attrs={'class': 'jobsearch-JobComponent-description'})
            # Checks if there's data at all
            if job_div:
                job_descs.update({job_id: job_div.get_text()})

            # Because you're scraping, this slows down your request!
            sleep(uniform(2.2, 10.2))

    all_jobs.append({'request_params': request_params,
                     'job_descriptions': job_descs})

json.dump(all_jobs, open(OUTPUT_FILE, 'w'))
