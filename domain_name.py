import tld

def get_domain_name(url):
    domain_name = tld.get_fld(url)
    return domain_name


