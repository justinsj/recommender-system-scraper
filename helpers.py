import re
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def validateInputDF(df, header):
    series = df[header]
    assert(len(series) > 0)

def get_company_url_index(url):
    return re.sub(r'^(https://|http://)','',url).split("/")[0]