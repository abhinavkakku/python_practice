import requests


r = requests.get(
    'https://ethicalhackx.com')

# print the response
html = r.text


# assign headers to a variable
headers = r.headers

# print headers
print(headers)

# get some header information and return a default value if not present
#print(headers.get('Content-Length', -1))
print(headers.get('Server', -1))

# Check for header if present and return a stamenet if true
if headers.get('Server', 'Apache') is None:
    print('Could not determine website server headers')

# try catch way of getting / header or exception in getting header
try:
    print(headers['X-Powered-By'])
except Exception as e:
    print(f"Exception in getting headder : {e}")
