import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


def voter_info(member_node):
    tags = ['first_name', 'last_name', 'party', 'state']
    return {tag: member_node.findChild(tag).text for tag in tags}


def vote_to_num(member_vote):
    if member_vote == 'Yea':
        return 1
    elif member_vote == 'Nay':
        return -1
    elif member_vote == 'Not Voting':
        return 0
    else:
        return -9999


def retry_requests_get(url, max_retries=5):
    s = requests.Session()
    retries = Retry(
        total=max_retries,
        backoff_factor=0.5,
        status_forcelist=[500, 502, 503, 504])
    s.mount('https://www.senate.gov', HTTPAdapter(max_retries=retries))
    return s.get(url, headers={'User-Agent': 'Manual'})


def find_sponsor(sponsor_text, voters):
    for v in voters:
        sponsor_format = '{}, {}'.format(voters[v]['last_name'],
                                         voters[v]['first_name'])
        if sponsor_format in sponsor_text:
            return v
    return None


def update_voter_bill_map(voter_bill_map, voters, vote_xml_text, label):
    vote_soup = BeautifulSoup(vote_xml_text, features='html.parser')
    members = vote_soup.find_all('member')

    for member in members:
        vid = member.lis_member_id.text
        if vid not in voters:
            voters.update({vid: voter_info(member)})
        vote_history = voter_bill_map.get(vid, {})
        vote_history.update({label:
                             vote_to_num(member.vote_cast.text)})
        if vid not in voter_bill_map:
            voter_bill_map.update({vid: vote_history})

    return None


def update_bills(bill_html, bills, label, voters):
    bill_soup = BeautifulSoup(bill_html, features='html.parser')
    bill_summary = bill_soup.find('div', attrs={"id": 'bill-summary'})
    bill = bill_summary.find_all('p')
    bill_text = ' '.join([b.text for b in bill])
    sponsor = bill_soup.find('table', attrs={'class': 'standard01'})
    bills.update({
        label:
        {'sponsor': find_sponsor(sponsor.find('td').text, voters),
         'bill_text': bill_text}})

    return None
