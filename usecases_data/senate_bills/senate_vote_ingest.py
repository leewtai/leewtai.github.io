# Code is derived from
# https://www.senate.gov/legislative/LIS/roll_call_lists/vote_menu_115_1.htm

import json
import re
from itertools import groupby, product
from time import sleep

from bs4 import BeautifulSoup
from requests.adapters import RetryError

import senate_utils as utils


SENATE_URL = 'https://www.senate.gov/legislative/LIS/'
SENATE_ITEMS_URL = SENATE_URL + 'roll_call_lists/vote_menu_{congress_num}_{sess_num}.xml'
SENATE_VOTE_URL = SENATE_URL + 'roll_call_votes/vote{congress_num}{sess_num}/vote_{congress_num}_{sess_num}_{vote_num}.xml'
BILLS_URL = 'http://www.congress.gov/bill/{congress_num}th-congress/{bill_type}/{bill_num}'
voters = {}
bills = {}
voter_bill_map = {}

congress_nums = range(105, 116)
sessions = [1, 2]

for congress_num, session in product(congress_nums, sessions):
    sess_acts_url = SENATE_ITEMS_URL.format(congress_num=congress_num,
                                            sess_num=session)
    try:
        senate_req = utils.retry_requests_get(url=sess_acts_url, max_retries=2)
    except RetryError:
        print(sess_acts_url)
        print('senate vote request retry failed')
        continue

    if senate_req.status_code != 200:
        continue
    senate_soup = BeautifulSoup(senate_req.text, features='html.parser')
    votes = senate_soup.find_all('vote')
    # Only grab senate bills
    vote_bills = [(vote.issue.text, vote.vote_number.text)
                  for vote in votes
                  if (vote.issue.text.startswith('S. ')
                      or vote.issue.text.startswith('H.R. '))]
    vote_bills.sort(key=lambda x: x)
    bill_grp = groupby(vote_bills, key=lambda x: x[0])
    bill_last_votes = [max(dat) for grp, dat in bill_grp]

    # each bill can be voted on multiple times
    for last_vote in bill_last_votes:
        sleep(0.1)
        issue = last_vote[0]
        if issue.startswith('S. '):
            bill_type = 'senate-bill'
        else:
            bill_type = 'house-bill'
        last_vote_num = last_vote[1]
        bill_num = int(re.sub('[^0-9]', '', issue))
        label = '_'.join(map(str,
                             [congress_num, session, issue, last_vote_num]))
        # Get the votes
        vote_url = SENATE_VOTE_URL.format(
            congress_num=congress_num,
            sess_num=session,
            vote_num=last_vote_num)

        try:
            vote_req = utils.retry_requests_get(url=vote_url, max_retries=2)
        except RetryError:
            print('retry failed to get votes')
            print(label)
            continue

        try:
            utils.update_voter_bill_map(voter_bill_map,
                                        voters,
                                        vote_req.text,
                                        label)
        except:
            print('beautiful soup failed for voter_bill update')
            print(label)
            continue

        # Get the text
        bill_url = BILLS_URL.format(congress_num=congress_num,
                                    bill_type=bill_type,
                                    bill_num=bill_num)
        try:
            bill_req = utils.retry_requests_get(url=bill_url, max_retries=2)
        except RetryError:
            print(bill_url)
            print(label)
            print('bill text request retry failed')
            continue

        try:
            utils.update_bills(bill_req.text, bills, label, voters)
        except:
            print('beaitiful soup failed for updating bill')
            print(label)
            continue


print('there are {} senate bills'.format(len(bills)))
json.dump(bills, open('bills.json', 'w'))
json.dump(voter_bill_map, open('votes.json', 'w'))
json.dump(voters, open('voters.json', 'w'))
