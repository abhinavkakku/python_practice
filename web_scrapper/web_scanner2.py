import requests
from bs4 import BeautifulSoup


# read the file # for reference taken file from cisco top websites
with open("C:\k\Projects\python_practice\web_scrapper\\100_domains.csv", 'r') as f:
    data = f.read()
    # print(data)

lines = data.split("\n")
print(len(lines))


for line in lines:
    url = 'https://' + line.split(",")[1]
    print(f"URL : {url} \n")
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        headers = response.headers
        print(f'Title : {soup.title.string} \n')
        #print(f'headers : {headers} \n')
        # print(headers['X-Powered_by'])
    except Exception as e:
        print(f'Exception in getting header  : {e}')
