import os
import sys

def get_filename(filename):
    return os.path.basename(filename)[:-3]
    
def get_hostname(url):
    from urlparse import urlparse
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return domain
    
def p(pstr):
    print pstr
    sys.stdout.flush()