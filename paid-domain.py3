#!/usr/bin/env python3
from datetime import datetime
import whois
import sys

if len(sys.argv) > 1:
    domain = sys.argv[1]
else:
    exit(1)

if( domain.split('.')[1] not in whois.TLD_RE.keys() ):
    print("Wrong TLD")
else:
    current_date = datetime.date(datetime.now())
    domain = whois.query(domain)
    domain_expiration = datetime.date(domain.expiration_date)
    print((domain_expiration - current_date).days)

