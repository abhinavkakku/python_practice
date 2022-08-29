import requests
from bs4 import BeautifulSoup
import tldextract


# read the file # for reference taken file from cisco top websites
with open("C:\k\Projects\python_practice\web_scrapper\\top-1m.csv", 'r') as f:
    data = f.read()
    # print(data)

lines = data.split("\n")
print(len(lines))


uniqueURLs = {}
allURLs = []
for line in lines:
    url = 'https://' + line.split(",")[1]
    print(f"URL : {url} \n")
    new = tldextract.extract(url)
    new_url = new.domain + '.' + new.suffix
    uniqueURLs[new_url] = True
    allURLs.append(new_url)
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        headers = response.headers
        print(f'Title : {soup.title.string} \n')
        #print(f'headers : {headers} \n')
        # print(headers['X-Powered_by'])
    except Exception as e:
        print(f'Exception in getting header  : {e}')
print(
    f"Length : len(lines) {len(lines)} \n len(allURLs) : {len(allURLs)} \n len(uniqueURLs : {len(uniqueURLs)}")
