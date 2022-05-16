#!/usr/local/bin/python3

import argparse
from io import StringIO
import re
import requests
from utils import read_fasta

parser = argparse.ArgumentParser()
parser.add_argument('dataset', type=argparse.FileType('r'))
args = parser.parse_args()

uniprot_ids = args.dataset.read().splitlines()
regex = re.compile(r'(?=N[^P][S|T][^P])')

for uniprot_id in uniprot_ids:
    uniprot_url = f'http://www.uniprot.org/uniprot/{uniprot_id}.fasta'
    try:
        r = requests.get(uniprot_url,allow_redirects=True)
        content = r.text
    except: 
        print('accession ID not valid')

    (name, seq) = next(read_fasta(StringIO(r.text)))

    locations = [match.start() + 1 for match in re.finditer(regex, seq)]

    if len(locations) > 0:
        print (uniprot_id)
        print (' '.join([str(x) for x in locations]))