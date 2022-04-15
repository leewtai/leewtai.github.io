import logging
from pathlib import Path

import requests
from glob import glob


logging.basicConfig(format="%(asctime)-15s %(message)s",
                    filename='parse_pdf2xml.log',
                    level=logging.INFO)

dir_path = 'prod_files/'
pdf_files = glob(dir_path + '*.pdf')


doc_paths = {'fail': Path('failed_grobid_parsed_pdf2xml.txt'),
             'success': Path('grobid_parsed_pdf2xml.txt')}
processed = []
for doc in doc_paths:
    if not doc_paths[doc].exists():
        doc_paths[doc].touch()
    processed.extend([fn for fn in doc_paths[doc].open('r').readlines()])
docs = {doc: doc_paths[doc].open('a') for doc in doc_paths}
# Running the Grobid service (depends on JVM8, gradle, grobid)
# https://grobid.readthedocs.io/en/latest/Grobid-service/
grobid_url = 'http://localhost:8070/api/processFulltextDocument'
for i, pdf_file in enumerate(pdf_files):
    if pdf_file in processed:
        logging.info('processed in past runs, skipping {}'.format(pdf_file))
        continue
    fp = Path(pdf_file)
    files = {'input': fp.open('rb'),
             'consolidateCitations': 1}

    logging.info('parsing file {}'.format(pdf_file))
    out = requests.post(url=grobid_url, files=files)
    if out.status_code != 200:
        docs['fail'].writelines('\n{}'.format(fp.name))
        continue
    with open('grobid_xml/{fn}.xml'.format(fn=fp.stem), 'w') as f:
        f.writelines(out.text)
    docs['success'].writelines('\n{}'.format(fp.name))


for doc in docs:
    docs[doc].close()
